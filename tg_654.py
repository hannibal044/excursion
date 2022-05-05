import telebot
from telebot import types
import wikipedia

bot = telebot.TeleBot('5285391763:AAHgHDTu4Ea3gRFs8kPy3_eeqlICsB-nE_M')
language = "ru"
wikipedia.set_lang(language)
exhibit_dict = {'Граната РГД-13': ['https://disk.yandex.ru/d/NQjiV0B5fvGlCA', 'РГД-33 — советская ручная граната, \
разработанная в 1933 году на основе гранаты Рдултовского образца 1914/30 года, использовавшейся во время Первой мировой войны.'],
                'Часы с корабля, воевавшего на Балтийском море': 'https://wampi.ru/image/RJYzZT7',
                'Папаха Генерала Кашубы': 'https://wampi.ru/image/RJYzoRq',
                'Шинель офицера водителя': ['https://wampi.ru/image/RJYGEV4',
                                            'Шинель шофера "Дороги жизни" А.И. Мудрецова, в которой он две блокадные зимы вел автобус по Ладожскому озеру.'],
                'Подлинный флаг корабля, который воевал на Балтийском море': ['https://wampi.ru/image/RJY7GXJ',
                                                                              'Точная копия боевого знамени 17 Краснознаменной Бобруйской  стрелковой дивизии. Передана  школе советом ветеранов дивизии  в 1978 году как символ связи поколений.'],
                'Офицерский планшет Д. С. Фридмана (Зам. Командира 980 арт-полка 17-ой дивизии)': 'https://wampi.ru/image/RJY7llV',
                'Автограф Константина Симонова, с его прикрепленными фотографиями': ['https://wampi.ru/image/RJYMoR0',
                                                                                     'Автограф Константина Симонова в книге отзывов школьного музея и фотография из личного архива писателя.'],
                'Портрет Генерала Кашубы': ['https://wampi.ru/image/RJYgb2a',
                                            'Портрет генерала танковых войск В.Н.Кашубы, написан маслом в 5О-е годы.'],
                'Щиток от пулемёта "Максим"': ['https://wampi.ru/image/RJYTrKg',
                                               'Система Максим (МСВ) - станковый пулемёт, разработанный британским оружейником американского происхождения Хайремом Стивенсом Максимом в 1883 году. Самый распространненый вид вооружения времен II мировой.'],
                'Винтовка Токарева': ['https://wampi.ru/image/RJYabw8',
                                      'Винтовка Токарева - модификация советской самозарядной винтовки, разработанной Ф. В. Токаревым. CВТ была разработана в качестве замены автоматической винтовки Симонова и 26 февраля 1939 принята на вооружение Красной армии. Первая СВТ образца 1938 года была выпущена 16 июля 1939 года. С 1 октября 1939 года начался валовый выпуск на Тульском, а с 1940 года — на Ижевском оружейном заводе.'],
                'Винтовка Мосина': ['https://wampi.ru/image/RJYE8Nq',
                                    'Русская 3-линейная (7,62-мм) винтовка Мосина образца 1891 года — магазинная винтовка, принятая на вооружение Русской императорской армии в 1891 году.'],
                'Чернильница фронтового писаря': 'https://wampi.ru/image/RuqLIWP',
                'Компас Героя Советского Союза И. Е. Качалко': 'https://wampi.ru/image/RuqPcxs',
                'Остов Пулемета Дегтярева': ['https://wampi.ru/image/RuqP5y8',
                                             'ДП (Дегтярёва пехотный, индекс ГАУ — 56-Р-321) — ручной пулемёт калибра 7,62 мм, разработанный Василием Алексеевичем Дегтярёвым. ДП стал одним из первых образцов стрелкового оружия, созданных в СССР.'],
                'Пистолет-пулемет Шпагина': ['https://wampi.ru/image/RuqPYUr',
                                             '7,62-мм пистолет-пулемёт образца 1941 года системы Шпагина (ППШ) — советский пистолет-пулемёт, разработанный в 1940 году конструктором Г. С. Шпагиным под патрон 7,62×25 мм ТТ и принятый на вооружение Красной Армии 21 декабря 1940 года. ППШ наряду с ППС-43 являлся основным пистолетом-пулемётом советских Вооружённых Сил в Великой Отечественной войне.']}
heroes_dict = {"Мартынов Моисей Никитович": 'http://skrinshoter.ru/s/270322/HtKXnXFd?a',
               "Дориков Максим Григорьевич": 'http://skrinshoter.ru/s/270322/7kN6zpKg?a',
               "Кустов Федор Михайлович": 'http://skrinshoter.ru/s/270322/nhP3s3GJ?a',
               "Клочков Николай Леонтьевич": 'http://skrinshoter.ru/s/270322/QsKprTTM?a',
               "Ермолаев Петр Алексеевич": 'http://skrinshoter.ru/s/270322/HiItgUdH?a',
               "Кашуба Владимир Несторович": 'http://skrinshoter.ru/s/270322/g3E4ZeBD?a',
               "Черновский Сергей Акимович": 'http://skrinshoter.ru/s/270322/ltn2FbeC?a',
               "Качалко Иван Елизарович": 'http://skrinshoter.ru/s/270322/9mfY7F7v?a',
               "Колесов Александр Андреевич": 'http://skrinshoter.ru/s/270322/aPzoWVsH?a',
               "Никитин Иван Никитович": 'http://skrinshoter.ru/s/270322/w6kxsduI',
               "Бочаров Иван Иванович": 'http://skrinshoter.ru/s/270322/nUyRSCsZ?a',
               'Романов Пётр Иванович': 'http://skrinshoter.ru/s/280322/6TDl1mTW?a'}


@bot.message_handler(commands=["start"])
def start(message, res=False):
    m = f'<b>👋 Здравствуй, {message.from_user.first_name}! \nЯ бот-экскурсовод по музею боевой славы в ГБОУ Школа №654 им. А. Д. Фридмана. </b>\n' \
        'Нажмите на "/menu" для начала работы!'
    bot.send_message(message.chat.id, m, parse_mode='html')


@bot.message_handler(commands=["menu"])
def menu(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Герои Советского Союза")
    item2 = types.KeyboardButton("Экспонаты музея")
    markup.add(item1, item2)
    bot.send_message(m.chat.id,
                     'Выберите, что Вам интересно  ⬇️',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Герои Советского Союза':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for i in range(0, len(list(heroes_dict)) - 2, 3):
            markup1.add(types.KeyboardButton(list(heroes_dict)[i]), types.KeyboardButton(list(heroes_dict)[i + 1]),
                        types.KeyboardButton(list(heroes_dict)[i + 2]))
        bot.send_message(message.chat.id, 'Выберите героя, о котором хотите узнать',
                         reply_markup=markup1)
        bot.register_next_step_handler(message, heroes)
    elif message.text.strip() == 'Экспонаты музея':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for i in range(0, len(list(exhibit_dict)) - 2, 3):
            markup1.add(types.KeyboardButton(list(exhibit_dict)[i]), types.KeyboardButton(list(exhibit_dict)[i + 1]),
                        types.KeyboardButton(list(exhibit_dict)[i + 2]))
        bot.send_message(message.chat.id, 'Выберите экспонат',
                         reply_markup=markup1)
        bot.register_next_step_handler(message, exhibit)
    else:
        bot.send_message(message.chat.id, 'Мне жаль, но у меня нет такой экскурсии')
        bot.register_next_step_handler(message, handle_text)


def exhibit(message):
    if message.text.strip() in list(exhibit_dict):
        if isinstance(exhibit_dict[message.text], list):
            bot.send_photo(message.chat.id, exhibit_dict[message.text][0])
            bot.send_message(message.chat.id, exhibit_dict[message.text][1])
        else:
            bot.send_photo(message.chat.id, exhibit_dict[message.text])
    else:
        bot.send_message(message.chat.id, 'У нас нет такого экспоната')
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    siu = types.KeyboardButton("/menu")
    markup2.add(siu)
    bot.send_message(message.chat.id, 'Нажмите "/menu", чтобы вернуться в начало.', reply_markup=markup2)


def heroes(message):
    global result, page, content, c, z
    if message.text.strip() in list(heroes_dict):
        result = wikipedia.search(f"{message.text.split()[0]}, {message.text.split()[1]} {message.text.split()[2]}")

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
        bot.send_message(message.chat.id, ''.join(z))
    else:
        bot.send_message(message.chat.id, 'У нас нет такого героя')
    bot.send_photo(message.chat.id, heroes_dict[message.text])
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    siu = types.KeyboardButton("/menu")
    markup2.add(siu)
    bot.send_message(message.chat.id, 'Нажмите "/menu", чтобы вернуться в начало.', reply_markup=markup2)


bot.polling(none_stop=True, interval=0)
