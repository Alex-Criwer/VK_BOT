import vk_api
import random
import commands
from commands import CODES
from commands import REFERENCES
from commands import WEEK
from PIL import Image
from vk_api.longpoll import VkLongPoll, VkEventType
from tokens import main_token
from bs4 import BeautifulSoup
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = main_token

session = vk_api.VkApi(token=token)

longpoll = VkLongPoll(session)

class VkBot:

    def make_button(self, keyboard, name):
        keyboard.add_button(name, color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

    def initialization_of_main_keyboard(self, keyboard):
        self.make_button(keyboard, 'Расписание')
        self.make_button(keyboard, 'Ближайшая пара')
        keyboard.add_button('Ссылки по предметам', color=VkKeyboardColor.POSITIVE)

    def initialization_of_week_keyboard(self,  keyboard):
        self.make_button(keyboard, 'Понедельник')
        self.make_button(keyboard, 'Вторник')
        self.make_button(keyboard, 'Среда')
        self.make_button(keyboard, 'Четверг')
        self.make_button(keyboard, 'Пятница')
        self.make_button(keyboard, 'Суббота')
        keyboard.add_button('Воскресенье', color=VkKeyboardColor.POSITIVE)

    def initialization_of_subject_keyboard(self,  keyboard):
        self.make_button(keyboard, 'Матан')
        self.make_button(keyboard, 'Аналмех')
        self.make_button(keyboard, 'БД')
        self.make_button(keyboard, 'ТПМС')
        keyboard.add_button('Диффуры', color=VkKeyboardColor.POSITIVE)

    def __init__(self, user_id):
        self.USER_ID = user_id
        self.MAIN_KEYBOARD = VkKeyboard(one_time=False, inline=False)
        self.initialization_of_main_keyboard(self.MAIN_KEYBOARD)
        self.WEEK_KEYBOARD = VkKeyboard(one_time=True, inline=False)
        self.initialization_of_week_keyboard(self.WEEK_KEYBOARD)
        self.SUBJECT_KEYBOARD = VkKeyboard(one_time=True, inline=False)
        self.initialization_of_subject_keyboard(self.SUBJECT_KEYBOARD)
        self.TIMETABLE = commands.timetable_pictures()

    def send_message(self, user_id, message, my_keyboard):
        session.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 10000),
                                         'keyboard': my_keyboard.get_keyboard()})

    def get_user_name_from_id(self, user_id):
        data = session.method('users.get', {'user_id': user_id})
        name = data[0]['first_name']
        return name

    def send_photo(self, user_id, message, my_keyboard, code):
        session.method('messages.send', {'user_id': user_id, 'random_id': random.randint(0, 10000), 'message': message,
                                         'keyboard': my_keyboard.get_keyboard(), 'attachment': code})

    def new_message(self, message):
        if message.upper() == 'расписание'.upper():
            self.send_message(self.USER_ID, self.get_user_name_from_id(self.USER_ID) + ", выбери день недели",
                                     self.WEEK_KEYBOARD)

        elif message.upper() == 'начать'.upper():
            self.send_message(self.USER_ID, "ниже приведены возможные функции", self.MAIN_KEYBOARD)

        elif message.upper() == 'ссылки по предметам'.upper():
            self.send_message(self.USER_ID, "выбери предмет", self.SUBJECT_KEYBOARD)

        elif message.upper() == 'понедельник'.upper():
            self.send_photo(self.USER_ID, 'понедельник', self.MAIN_KEYBOARD, CODES['понедельник'])

        elif message.upper() == 'вторник'.upper():
            self.send_photo(self.USER_ID, 'вторник', self.MAIN_KEYBOARD, CODES['вторник'])

        elif message.upper() == 'среда'.upper():
            self.send_photo(self.USER_ID, 'среда', self.MAIN_KEYBOARD, CODES['среда'])

        elif message.upper() == 'четверг'.upper():
            self.send_photo(self.USER_ID, 'четверг', self.MAIN_KEYBOARD, CODES['четверг'])

        elif message.upper() == 'пятница'.upper():
            self.send_photo(self.USER_ID, 'пятница', self.MAIN_KEYBOARD, CODES['пятница'])

        elif message.upper() == 'суббота'.upper():
            self.send_photo(self.USER_ID, 'суббота', self.MAIN_KEYBOARD, CODES['суббота'])

        elif message.upper() == 'воскресенье'.upper():
            self.send_photo(self.USER_ID, 'воскресенье', self.MAIN_KEYBOARD, CODES['воскресенье'])

        elif message.upper() == 'матан'.upper():
            self.send_message(self.USER_ID,
                              "табличка с баллами Орел: " + REFERENCES['матан_opел'] + "\n" +
                              "classroom с дз: " + REFERENCES['матан_дз'],
                              self.MAIN_KEYBOARD)

        elif message.upper() == 'аналмех'.upper():
            self.send_message(self.USER_ID,
                              "табличка с баллами: " + REFERENCES['аналмех'],
                              self.MAIN_KEYBOARD)

        elif message.upper() == 'бд'.upper():
            self.send_message(self.USER_ID,
                              "ссылка на записи лекций: " + REFERENCES['бд'] + '\n' +
                              "ссылка на оценки: " + REFERENCES['бд оценки'],
                              self.MAIN_KEYBOARD)

        elif message.upper() == 'диффуры'.upper():
            self.send_message(self.USER_ID,
                              "ссылка на записи лекций: " + REFERENCES['диффуры'],
                              self.MAIN_KEYBOARD)

        elif message.upper() == 'ТПМС'.upper():
            self.send_message(self.USER_ID,
                              "ссылка на записи семинаров: " + REFERENCES['ТПМС'],
                              self.MAIN_KEYBOARD)

        else:
            self.send_message(self.USER_ID, "не понимаю, о чем вы", self.MAIN_KEYBOARD)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            user_id = event.user_id

            bot = VkBot(user_id)
            bot.new_message(event.text)
