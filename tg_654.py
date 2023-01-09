# -*- coding: utf-8 -*-
import telebot
from telebot import types
import wikipedia

bot = telebot.TeleBot('5285391763:AAHgHDTu4Ea3gRFs8kPy3_eeqlICsB-nE_M')
language = "ru"
wikipedia.set_lang(language)
exhibit_dict = {'12': ['Граната РГД-13', 'https://disk.yandex.ru/d/NQjiV0B5fvGlCA', 'РГД-33 — советская ручная граната, \
                разработанная в 1933 году на основе гранаты Рдултовского образца 1914/30 года, использовавшейся во время Первой мировой войны.'],
                '13': ['Часы с корабля, воевавшего на Балтийском море', 'https://wampi.ru/image/RJYzZT7',
                       'Часы были переданы музею участниками обороны полуострова Гангут (Ханко).'],
                '14': ['Папаха Генерала Кашубы', 'https://wampi.ru/image/RJYzoRq',
                       'Папаха генерала танковых войск, Героя Советского Союза В.Н. Кашубы была передана школе сыном героя Б.В.Кашубой. Комсомольская организация школы с 1965 года носила имя В.Н.Кашубы.'],
                '15': ['Солдатская шинель водителя', 'https://wampi.ru/image/RJYGEV4',
                       'Шинель водителя "Дороги жизни" А.И. Мудрецова, в которой он две блокадные зимы вел автобус по Ладожскому озеру.'],
                '16': ['Боевое знамя 17 Краснознаменной Бобруйской стрелковой дивизии', 'https://imgur.com/a/HBY1XFB',
                       'Точная копия боевого знамени 17 Краснознаменной Бобруйской стрелковой дивизии. Передана школе советом ветеранов дивизии в 1978 году как символ связи поколений.'],
                '17': ['Офицерский планшет Д. С. Фридмана (Зам. Командира 980 арт-полка 17-ой дивизии)',
                       'https://wampi.ru/image/RJY7llV',
                       "С этим планшетом Д.С. Фридман прошел всю войну: в июле 1941 он в ушел в 17 дивизию народного ополчения Москворецкого района, в составе этой дивизии в мае 1945 встретил победу в Восточной Пруссии."],
                '18': ['Автограф Константина Симонова, с его прикрепленными фотографиями',
                       'https://wampi.ru/image/RJYMoR0',
                       'Автограф Константина Симонова в книге отзывов школьного музея и фотография из личного архива писателя.'],
                '19': ['Портрет Генерала Кашубы', 'https://wampi.ru/image/RJYgb2a',
                       'Портрет генерала танковых войск В.Н.Кашубы, написан маслом в 5О-е годы.'],
                '20': ['Щиток от пулемёта "Максим"', 'https://wampi.ru/image/RJYTrKg',
                       'Система Максим (МСВ) - станковый пулемёт, разработанный британским оружейником американского происхождения Хайремом Стивенсом Максимом в 1883 году. Самый распространненый вид вооружения времен II мировой.'],
                '21': ['Винтовка Токарева', 'https://wampi.ru/image/RJYabw8',
                       'Винтовка Токарева - модификация советской самозарядной винтовки, разработанной Ф. В. Токаревым. CВТ была разработана в качестве замены автоматической винтовки Симонова и 26 февраля 1939 принята на вооружение Красной армии. Первая СВТ образца 1938 года была выпущена 16 июля 1939 года. С 1 октября 1939 года начался валовый выпуск на Тульском, а с 1940 года — на Ижевском оружейном заводе.'],
                '22': ['Винтовка Мосина', 'https://wampi.ru/image/RJYE8Nq',
                       'Русская 3-линейная (7,62-мм) винтовка Мосина образца 1891 года — магазинная винтовка, принятая на вооружение Русской императорской армии в 1891 году.'],
                '23': ['Чернильница фронтового писаря', 'https://wampi.ru/image/RuqLIWP',
                       'Чернильница - была передана музею выпускниками - членами поискового отряда. Найдена в районе города Вязьмы.'],
                '24': ['Компас Героя Советского Союза И. Е. Качалко', 'https://wampi.ru/image/RuqPcxs',
                       'Компас был передан музею семьёй Героя Советского Союза И.Е. Качалко. Личная вещь героя, необходимая на фронте офицеру инженерных войск.'],
                '25': ['Остов пулемёта Дегтярёва', 'https://wampi.ru/image/RuqP5y8',
                       'ДП (Дегтярёва пехотный, индекс ГАУ — 56-Р-321) — ручной пулемёт калибра 7,62 мм, разработанный Василием Алексеевичем Дегтярёвым. ДП стал одним из первых образцов стрелкового оружия, созданных в СССР.'],
                '26': ['Пистолет-пулемёт Шпагина', 'https://wampi.ru/image/RuqPYUr',
                       '7,62-мм пистолет-пулемёт образца 1941 года системы Шпагина (ППШ) — советский пистолет-пулемёт, разработанный в 1940 году конструктором Г. С. Шпагиным под патрон 7,62×25 мм ТТ и принятый на вооружение Красной Армии 21 декабря 1940 года. ППШ наряду с ППС-43 являлся основным пистолетом-пулемётом советских Вооружённых Сил в Великой Отечественной войне.']}
heroes_dict = {'0': ["Мартынов Моисей Никитович", 'http://skrinshoter.ru/s/270322/HtKXnXFd?a'],
               '1': ["Дориков Максим Григорьевич", 'http://skrinshoter.ru/s/270322/7kN6zpKg?a'],
               '2': ["Кустов Федор Михайлович", 'http://skrinshoter.ru/s/270322/nhP3s3GJ?a'],
               '3': ["Клочков Николай Леонтьевич", 'http://skrinshoter.ru/s/270322/QsKprTTM?a'],
               '4': ["Ермолаев Петр Алексеевич", 'http://skrinshoter.ru/s/270322/HiItgUdH?a'],
               '5': ["Кашуба Владимир Несторович", 'http://skrinshoter.ru/s/270322/g3E4ZeBD?a'],
               '6': ["Черновский Сергей Акимович", 'http://skrinshoter.ru/s/270322/ltn2FbeC?a'],
               '7': ["Качалко Иван Елизарович", 'http://skrinshoter.ru/s/270322/9mfY7F7v?a'],
               '8': ["Колесов Александр Андреевич", 'http://skrinshoter.ru/s/270322/aPzoWVsH?a'],
               '9': ["Никитин Иван Никитович", 'http://skrinshoter.ru/s/270322/w6kxsduI'],
               '10': ["Бочаров Иван Иванович", 'http://skrinshoter.ru/s/270322/nUyRSCsZ?a'],
               '11': ['Романов Пётр Иванович', 'http://skrinshoter.ru/s/280322/6TDl1mTW?a']}


@bot.message_handler(commands=["start"])
def start(message, res=False):
    m = f'<b>👋 Здравствуй, {message.from_user.first_name}! \nЯ бот-экскурсовод по музею Героической истории России ГБОУ Школы №654 им. А. Д. Фридмана. </b>\n' \
        'Нажмите на "/menu" для начала работы!'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('/menu')
    markup.add(item)
    bot.send_message(message.chat.id, m, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=["menu"])
def menu(m, res=False):
    keyboard = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Герои Советского Союза", callback_data='h')
    item2 = types.InlineKeyboardButton(text="Экспонаты музея", callback_data='e')
    keyboard.add(item1)
    keyboard.add(item2)
    bot.send_message(m.chat.id, "Выберите, что Вам интересно  ⬇️", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda message: True)
def handle_text(message):
    if message.data == 'h':
        markup1 = types.InlineKeyboardMarkup()
        for i in range(0, 6, 2):
            markup1.add(types.InlineKeyboardButton(text=heroes_dict[str(i)][0], callback_data=str(i)))
            markup1.add(types.InlineKeyboardButton(text=heroes_dict[str(i + 1)][0], callback_data=str(i+1)))
        markup1.add(types.InlineKeyboardButton(text='➡️', callback_data='+'))
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Выберите героя, о котором хотите узнать",
                              reply_markup=markup1)
    elif message.data == '+':
        markup1 = types.InlineKeyboardMarkup()
        for i in range(6, 12, 2):
            markup1.add(types.InlineKeyboardButton(text=heroes_dict[str(i)][0], callback_data=str(i)))
            markup1.add(types.InlineKeyboardButton(text=heroes_dict[str(i + 1)][0], callback_data=str(i+1)))
        markup1.add(types.InlineKeyboardButton(text='⬅️', callback_data='h'))
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Выберите героя, о котором хотите узнать",
                              reply_markup=markup1)
    elif message.data == '-':
        markup2 = types.InlineKeyboardMarkup()
        for i in range(19, 27, 2):
            markup2.add(types.InlineKeyboardButton(text=exhibit_dict[str(i)][0], callback_data=str(i)))
            markup2.add(types.InlineKeyboardButton(text=exhibit_dict[str(i + 1)][0], callback_data=str(i)))
        markup2.add(types.InlineKeyboardButton(text='⬅️', callback_data='e'))
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Выберите экспонат ⬇️",
                              reply_markup=markup2)
    elif message.data == 'e':
        markup2 = types.InlineKeyboardMarkup()
        for i in range(12, 19, 2):
            markup2.add(types.InlineKeyboardButton(text=exhibit_dict[str(i)][0], callback_data=str(i)))
            markup2.add(types.InlineKeyboardButton(text=exhibit_dict[str(i + 1)][0], callback_data=str(i)))
        markup2.add(types.InlineKeyboardButton(text='➡️', callback_data='-'))
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Выберите экспонат ⬇️",
                              reply_markup=markup2)
    elif message.data in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
        result = wikipedia.search(
            f"{(heroes_dict[message.data][0]).split()[0]}, {(heroes_dict[message.data][0]).split()[1]} {(heroes_dict[message.data][0]).split()[2]}")
        page = wikipedia.page(result[0])
        content = page.content
        c = -1
        for i in range(len(content) - 28):
            c += 1
            if content[i:i + 15] == '== Источники ==' or content[i:i + 13] == '== Галерея ==' or content[
                                                                                                 i:i + 16] == '== Литература ==' or content[
                                                                                                                                    i:i + 13] == '== Награды ==' or content[
                                                                                                                                                                    i:i + 12] == '== Память ==' or content[
                                                                                                                                                                                                   i:i + 16] == '== Примечания ==' or content[
                                                                                                                                                                                                                                      i:i + 28] == '== Советско-финская война ==':
                break
        z = list(content)
        del z[c - 3:]
        bot.send_message(chat_id=message.message.chat.id, text=''.join(z))
        bot.send_photo(chat_id=message.message.chat.id, photo=heroes_dict[message.data][1])
        bot.send_message(chat_id=message.message.chat.id, text='Нажмите "/menu", чтобы вернуться в начало.')
    elif message.data in ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']:
        if message.data:
            bot.send_photo(chat_id=message.message.chat.id, photo=exhibit_dict[message.data][1])
            bot.send_message(chat_id=message.message.chat.id, text=exhibit_dict[message.data][2])
            bot.send_message(chat_id=message.message.chat.id, text='Нажмите "/menu", чтобы вернуться в начало.')
        else:
            bot.send_message(chat_id=message.message.chat.id, text='У нас нет такого экспоната')


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text:
        bot.send_message(message.chat.id, 'Извините, я Вас не понимаю. Воспользуйтесь кнопками!')


bot.polling(none_stop=True, interval=0)
