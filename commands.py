from PIL import Image
import pandas

path = "C:\\Users\\Asus\\PycharmProjects\\BOT\\Timetable"


def timetable_pictures():
    timetable = dict()
    timetable['вторник'] = Image.open(path + '\Tuesday.JPG')
    timetable['среда'] = Image.open(path + '\Wednesday.JPG')
    timetable['четверг'] = Image.open(path + '\Thursday.JPG')
    timetable['пятница'] = Image.open(path + '\Friday.JPG')
    timetable['суббота'] = Image.open(path + '\Saturday.JPG')
    timetable['кот'] = Image.open(path + '\cat.jpg')
    return timetable


COMMANDS = {'понедельник': 'понедельник',
            'вторник': 'вторник',
            'среда': 'среда',
            'четверг': 'четверг',
            'пятница': 'пятница',
            'суббота': 'суббота',
            'воскресенье': 'воскресенье',
            'расписание': 'расписание',
            'ближайшая пара': 'ближайшая пара',
            'ссылки по предметам': 'ссылки по предметам',
            'матан': 'матан',
            'аналмех': 'аналмех',
            'бд': 'бд',
            'ТПМС': 'ТПМС',
            'диффуры': 'диффуры',
            'начать': 'начать'}

CODES = {'понедельник': 'photo-202430314_457239025',
         'вторник': 'photo-202430314_457239036',
         'среда': 'photo-202430314_457239037',
         'четверг': 'photo-202430314_457239035',
         'пятница': 'photo-202430314_457239033',
         'суббота': 'photo-202430314_457239034',
         'воскресенье': 'photo-202430314_457239025'}


REFERENCES = {'матан_opел': 'https://docs.google.com/spreadsheets/d/1LMnxWxTEieGpdWQe1UdMTfxw9HBcwqU6quJlu3f5qpE/edit#gid=876215785',
         'матан_дз': 'https://classroom.google.com/u/0/c/MTYyOTc2MzE3MTMx',
         'аналмех': 'https://docs.google.com/spreadsheets/d/1Rp0Fo6hZs5Z4claThuNFY4uj_vz79PfAgSKE49e_bLY/edit#gid=0',
         'бд': 'https://drive.google.com/drive/folders/174_vQYw2NZNfLc8f4flr-kc3T5EMyQlc',
         'диффуры': 'https://mipt.ru/education/chair/mathematics/study/d_obuch/vesenniy-semestr/2021/2-kurs/%D0%9B_%D0%94%D0%A3_%D0%94%D1%83%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F.php',
         'ТПМС': 'https://disk.yandex.ru/d/1qbKQsL01K_2DA/screen?w=1'}