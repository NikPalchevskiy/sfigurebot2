import math
import telebot
from telebot import types
import datetime
import requests

TOKEN = "1869487110:AAG_IlM8Sd9ctVtuk69BYxvxL3geZFzQd1s"
bot = telebot.TeleBot(TOKEN)
metric = "мм"
a = 0
b = 0
c = 0
p = 0
P = 0
r = 0
R = 0
ae1 = 0
ae2 = 0
ae3 = 0
h = 0
hideBoard = types.ReplyKeyboardRemove()

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECiQJg4waZldrNhbnjWQ2txQmmTcBWWQACqA4AAs4cqEjmHBhNWFATtSAE')
    cid = message.chat.id
    cn1 = message.from_user.first_name
    cn2 = message.from_user.last_name
    cname = message.chat.username
    today = datetime.datetime.today()
    with open('log.txt','a',encoding="utf-8") as f:
        f.write(str(cn1) + ";" + str(cn2) + ";" + str(cid) + ";" + str(cname) + ";" + "    ")
        f.write(str(today.strftime("%Y-%m-%d-%H.%M.%S")) + " \n")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('/start')
    btn2 = types.KeyboardButton('/metric')
    markup.add(btn1, btn2)
    start_handler = f"Привет {message.from_user.first_name}, что именно тебя интересует?"
    keyboard_start = types.InlineKeyboardMarkup()
    key_three = types.InlineKeyboardButton(text = 'Произвольный треугольник', callback_data='three')
    keyboard_start.add(key_three)
    key_rect = types.InlineKeyboardButton(text = 'Четырехугольник', callback_data='rect')
    keyboard_start.add(key_rect)
    key_circ = types.InlineKeyboardButton(text = 'Круг', callback_data='circ')
    keyboard_start.add(key_circ)
    key_n = types.InlineKeyboardButton(text = 'Правильный n-угольник', callback_data='n')
    keyboard_start.add(key_n)
    bot.send_message(message.from_user.id, start_handler, reply_markup=markup)
    bot.send_message(message.from_user.id, text = "Выберите фигуру", parse_mode='html',reply_markup=keyboard_start)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id, "Этот бот умеет считать площадь и периметр фигур\n Доступные команды:")
    bot.send_message(message.from_user.id, "/start - начало вычисления\n /help - справочник\n /metric - изменить единицы измерения расстояния (по дефолту - мм")

@bot.message_handler(commands=['metric'])
def send_metric(message):
    keyboard_metric = types.InlineKeyboardMarkup()
    key_mm = types.InlineKeyboardButton(text = 'Миллиметры', callback_data='мм')
    keyboard_metric.add(key_mm)
    key_sm = types.InlineKeyboardButton(text = 'Сантиметры', callback_data='см')
    keyboard_metric.add(key_sm)
    key_m = types.InlineKeyboardButton(text = 'Метры', callback_data='м')
    keyboard_metric.add(key_m)
    key_km = types.InlineKeyboardButton(text = 'Километры', callback_data='км')
    keyboard_metric.add(key_km)
    bot.send_message(message.from_user.id, text = "Выберите предпочитаемые единицы измерения расстояния для ввода",reply_markup=keyboard_metric)

def v_three(message):
    keyboard_three = types.InlineKeyboardMarkup()
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/sqt/sqt1.png')
    bot.send_message(message.from_user.id,"a = 1 сторона \n b = 2 сторона \n c = 3 сторона \n h(a) = высота опущенная на сторону a \n R - Радиус описанной окружности \n r - Радиус вписанной окружности \n alpha - угол между a и b \n beta - угол между a и c \n gamma - 3 угол \n p - полупериметр")
    key_t1 = types.InlineKeyboardButton(text='a, b, alpha', callback_data='t1')
    key_t2 = types.InlineKeyboardButton(text='a, b, c', callback_data='t2')
    key_t3 = types.InlineKeyboardButton(text='a, h(a)', callback_data='t3')
    key_t4 = types.InlineKeyboardButton(text='a, alpha, beta', callback_data='t4')
    key_t5 = types.InlineKeyboardButton(text='p, r', callback_data='t5')
    key_t6 = types.InlineKeyboardButton(text='alp,bet,gam,R', callback_data='t6')
    key_t7 = types.InlineKeyboardButton('342')
    keyboard_three.add(key_t1,key_t2,key_t3,key_t4,key_t5,key_t6)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_three)

def v_rect(message):
    keyboard_rect = types.InlineKeyboardMarkup()
    key_r1 = types.InlineKeyboardButton(text='Прямоугольник', callback_data='r1')
    key_r2 = types.InlineKeyboardButton(text='Параллелограмм', callback_data='r2')
    key_r3 = types.InlineKeyboardButton(text='Квадрат', callback_data='r3')
    key_r4 = types.InlineKeyboardButton(text='Ромб', callback_data='r4')
    key_r5 = types.InlineKeyboardButton(text='Трапеция', callback_data='r5')
    key_r6 = types.InlineKeyboardButton(text='Дельтоид', callback_data='r6')
    key_r7 = types.InlineKeyboardButton(text='Произвольный выпуклый четырёхугольник', callback_data='r7')
    key_r8 = types.InlineKeyboardButton(text='Вписанный четырёхугольник', callback_data='r8')
    keyboard_rect.add(key_r1, key_r2, key_r3, key_r4, key_r5, key_r6, key_r7, key_r8)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect)

def v_circ(message):
    keyboard_circ = types.InlineKeyboardMarkup()
    key_c1 = types.InlineKeyboardButton(text='S круга', callback_data='c1')
    key_c2 = types.InlineKeyboardButton(text='S сектора', callback_data='c2')
    key_c3 = types.InlineKeyboardButton(text='S сегмента', callback_data='c3')
    keyboard_circ.add(key_c1, key_c2, key_c3)
    bot.send_message(message.from_user.id, text="Что хотите узнать?", reply_markup=keyboard_circ)

def v_n(message):
    keyboard_n = types.InlineKeyboardMarkup()
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/regular/reg1.png')
    bot.send_message(message.from_user.id,"a = сторона \n n = Кол-во сторон \n R - Радиус описанной окружности \n r - Радиус вписанной окружности")
    key_n1 = types.InlineKeyboardButton(text='a', callback_data='n1')
    key_n2 = types.InlineKeyboardButton(text='r', callback_data='n2')
    key_n3 = types.InlineKeyboardButton(text='R', callback_data='n3')
    keyboard_n.add(key_n1, key_n2, key_n3)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_n)

def n_1_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, n_1_a1)
        else:
            bot.reply_to(message, "Введите n")
            bot.register_next_step_handler(message, n_1_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, n_1_a1)

def n_1_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, n_1_a2)
        else:
            n_1_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, n_1_a2)


def n_1_s(message):
    global a, b,metric, P, ae1, c, R
    ae1 = 180/b
    s = ((a**2)*b)/((math.sin(ae1*math.pi/180)/math.cos(ae1*math.pi/180))*4)
    bot.send_message(message.from_user.id, "a = " + str(a) + metric + "\n n = " + str(b))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')


def n_2_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, n_2_a1)
        else:
            bot.reply_to(message, "Введите n")
            bot.register_next_step_handler(message, n_2_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, n_2_a1)

def n_2_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, n_2_a2)
        else:
            n_2_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, n_2_a2)

def n_2_s(message):
    global a, b,metric, P, ae1, c, R
    ae1 = 180/b
    s = (a**2)*b*((math.sin(ae1*math.pi/180)/math.cos(ae1*math.pi/180)))
    bot.send_message(message.from_user.id, "r = " + str(a) + metric + "\n n = " + str(b))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def n_3_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, n_3_a1)
        else:
            bot.reply_to(message, "Введите n")
            bot.register_next_step_handler(message, n_3_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, n_3_a1)

def n_3_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, n_3_a2)
        else:
            n_3_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, n_3_a2)

def n_3_s(message):
    global a, b,metric, P, ae1, c, R
    ae1 = 360/b
    s = (a**2)*b*(math.sin(ae1*math.pi/180))/2
    bot.send_message(message.from_user.id, "r = " + str(a) + metric + "\n n = " + str(b))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def circ_c1_a1(message):
    global R
    try:
        R = float(message.text)
        if R <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, circ_c1_a1)
        else:
            circ_c1_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, circ_c1_a1)

def circ_c1_s(message):
    global a, b,metric, P, ae1, c, R
    s = math.pi*(R**2)
    P = R**2
    bot.send_message(message.from_user.id, "R = " + str(R) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2" + " или " + str(P) +(" Pi"))
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def circ_c2_a1(message):
    global R
    try:
        R = float(message.text)
        if R <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, circ_c2_a1)
        else:
            bot.reply_to(message, "Введите угол между диагоналями")
            bot.register_next_step_handler(message, circ_c2_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, circ_c2_a1)

def circ_c2_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 180:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, circ_c2_ae1)
        else:
            circ_c2_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, circ_c2_ae1)

def circ_c2_s(message):
    global a, b,metric, P, ae1, c, R
    s = math.pi*(R**2)*ae1/360
    P = (R**2)*ae1/360
    bot.send_message(message.from_user.id, "R = " + str(R) + metric + "\n Alpha = " + str(ae1))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2" + " или " + str(P) +(" Pi"))
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def circ_c3_a1(message):
    global R
    try:
        R = float(message.text)
        if R <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, circ_c3_a1)
        else:
            bot.reply_to(message, "Введите угол между диагоналями")
            bot.register_next_step_handler(message, circ_c3_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, circ_c3_a1)

def circ_c3_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 180:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, circ_c3_ae1)
        else:
            circ_c3_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, circ_c3_ae1)

def circ_c3_s(message):
    global a, b,metric, P, ae1, c, R
    s = 0.5*((math.pi*ae1/180)-math.sin(ae1*math.pi/180))*(R**2)
    bot.send_message(message.from_user.id, "R = " + str(R) + metric + "\n Alpha = " + str(ae1))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')


def v_rect_r1(message):
    keyboard_rect_r1 = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id,"a - 1 сторона \n b - 2 сторона \n d - диагональ \n R - Радиус описанной окружности \n fi - угол между диагоналями")
    key_r11 = types.InlineKeyboardButton(text='a, b', callback_data='r11')
    key_r21 = types.InlineKeyboardButton(text='d, fi', callback_data='r21')
    key_r31 = types.InlineKeyboardButton(text='R, fi', callback_data='r31')
    keyboard_rect_r1.add(key_r11, key_r21, key_r31)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect_r1)

def rect_r11_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r11_a1)
        else:
            bot.reply_to(message, "Введите вторую сторону")
            bot.register_next_step_handler(message, rect_r11_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r11_a1)

def rect_r11_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r11_a2)
        else:
            rect_r11_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r11_a2)

def rect_r11_s(message):
    global a, b,metric, P
    s = a*b
    P = a*2+b*2
    bot.send_message(message.from_user.id, "1 сторона = "+ str(a) + metric +"\n 2 сторона = " + str(b) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r21_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r21_a1)
        else:
            bot.reply_to(message, "Введите угол между диагоналями")
            bot.register_next_step_handler(message, rect_r21_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r21_a1)

def rect_r21_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r21_ae1)
        else:
            rect_r21_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r21_ae1)

def rect_r21_s(message):
    global a, b,metric, P, ae1, c
    s = a**2*math.sin(ae1*math.pi/180)/2
    c = math.sqrt((a/2) ** 2 + (a/2) ** 2 - 2 * (a/2) * (a/2) * math.cos(ae1 * math.pi / 180))
    b = s/c
    P = c*2 + b*2
    bot.send_message(message.from_user.id, "Диагональ = " + str(a) + metric + "\n Угол между диагоналями " + str(ae1))
    bot.send_message(message.from_user.id, "1 сторона = "+ str(b) + metric +"\n 2 сторона = " + str(c) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r31_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r31_a1)
        else:
            bot.reply_to(message, "Введите угол между диагоналями")
            bot.register_next_step_handler(message, rect_r31_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r31_a1)

def rect_r31_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r31_ae1)
        else:
            rect_r31_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r31_ae1)

def rect_r31_s(message):
    global a, b,metric, P, ae1, c
    s = 2*(a**2)*math.sin(ae1*math.pi/180)
    c = math.sqrt(a ** 2 + a ** 2 - 2 * a * a * math.cos(ae1 * math.pi / 180))
    b = s/c
    P = c*2 + b*2
    bot.send_message(message.from_user.id, "Диагональ = " + str(a) + metric + "\n Угол между диагоналями " + str(ae1))
    bot.send_message(message.from_user.id, "1 сторона = "+ str(b) + metric +"\n 2 сторона = " + str(c) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def v_rect_r2(message):
    keyboard_rect_r2 = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id,"a - 1 сторона \n b - 2 сторона \n d1 - 1 диагональ \n d2 - 2 диагональ \n alpha - угол между a и b \n fi - угол между диагоналями")
    key_r12 = types.InlineKeyboardButton(text='a, h(a)', callback_data='r12')
    key_r22 = types.InlineKeyboardButton(text='a, b, alpha', callback_data='r22')
    key_r32 = types.InlineKeyboardButton(text='d1,d2,fi', callback_data='r32')
    keyboard_rect_r2.add(key_r12, key_r22, key_r32)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect_r2)

def rect_r12_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r12_a1)
        else:
            bot.reply_to(message, "Введите высоту опущенную на эту сторону")
            bot.register_next_step_handler(message, rect_r12_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r12_a1)

def rect_r12_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r12_a2)
        else:
            rect_r12_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r12_a2)

def rect_r12_s(message):
    global a, b,metric, P
    s = a*b
    bot.send_message(message.from_user.id, "сторона = "+ str(a) + metric +"\n высота = " + str(b) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r22_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r22_a1)
        else:
            bot.reply_to(message, "Введите 2 сторону")
            bot.register_next_step_handler(message, rect_r22_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r22_a1)

def rect_r22_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r22_a2)
        else:
            bot.reply_to(message, "Введите угол между сторонами")
            bot.register_next_step_handler(message, rect_r22_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r22_a2)

def rect_r22_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r22_ae1)
        else:
            rect_r22_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r22_ae1)

def rect_r22_s(message):
    global a, b,metric, P, ae1
    s = a*b*math.sin(ae1*math.pi/180)
    P = 2*a + b*2
    bot.send_message(message.from_user.id, "1 сторона = "+ str(a) + metric +"\n 2 сторона = " + str(b) + metric +"\n угол между ними = " + str(ae1))
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r32_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r32_a1)
        else:
            bot.reply_to(message, "Введите 2 диагональ")
            bot.register_next_step_handler(message, rect_r32_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r32_a1)

def rect_r32_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r32_a2)
        else:
            bot.reply_to(message, "Введите угол между диагоналями")
            bot.register_next_step_handler(message, rect_r32_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r32_a2)

def rect_r32_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r32_ae1)
        else:
            rect_r32_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r32_ae1)

def rect_r32_s(message):
    global a, b,metric, P, ae1
    s = a*b*math.sin(ae1*math.pi/180)/2
    bot.send_message(message.from_user.id, "1 диагональ = "+ str(a) + metric +"\n 2 диагональ = " + str(b) + metric +"\n угол между ними = " + str(ae1))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def v_rect_r3(message):
    keyboard_rect_r3 = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id,"a - сторона \n r - радиус вписанной окружности \n R - Радиус описанной окружности \n d - диагональ")
    key_r13 = types.InlineKeyboardButton(text='a', callback_data='r13')
    key_r23 = types.InlineKeyboardButton(text='r', callback_data='r23')
    key_r33 = types.InlineKeyboardButton(text='d', callback_data='r33')
    key_r43 = types.InlineKeyboardButton(text='R', callback_data='r43')
    keyboard_rect_r3.add(key_r13, key_r23, key_r33, key_r43)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect_r3)

def rect_r13_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r13_a1)
        else:
            rect_r13_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r13_a1)

def rect_r13_s(message):
    global a, b,metric, P, ae1
    s = a**2
    P = 4*a
    bot.send_message(message.from_user.id, "сторона = "+ str(a) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r23_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r23_a1)
        else:
            rect_r23_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r23_a1)

def rect_r23_s(message):
    global a, b,metric, P, ae1
    s = 4*(a**2)
    P = 8*a
    bot.send_message(message.from_user.id, "сторона = "+ str(a) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r33_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r33_a1)
        else:
            rect_r33_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r33_a1)

def rect_r33_s(message):
    global a, b,metric, P, ae1
    s = (a**2)/2
    b = math.sqrt(s)
    P = b*4
    bot.send_message(message.from_user.id, "сторона = "+ str(b) + metric + " \n диагональ = "+ str(a) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r43_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r43_a1)
        else:
            rect_r43_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r43_a1)

def rect_r43_s(message):
    global a, b,metric, P, ae1
    s = (a**2)*2
    b = math.sqrt(s)
    P = b*4
    bot.send_message(message.from_user.id, "сторона = "+ str(b) + metric + " \nРадиус = "+ str(a) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def v_rect_r4(message):
    keyboard_rect_r4 = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id,"a - сторона \n a(h) - высота опущенная на сторону а \n fi - любой с 4-х углов \n r - радиус вписанной окружности \n d1, d2 - диагонали")
    key_r14 = types.InlineKeyboardButton(text='a, h(a)', callback_data='r14')
    key_r24 = types.InlineKeyboardButton(text='a, fi', callback_data='r24')
    key_r34 = types.InlineKeyboardButton(text='d1, d2', callback_data='r34')
    key_r44 = types.InlineKeyboardButton(text='a, r', callback_data='r44')
    key_r54 = types.InlineKeyboardButton(text='r, fi', callback_data='r54')
    keyboard_rect_r4.add(key_r14, key_r24, key_r34, key_r44, key_r54)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect_r4)

def rect_r14_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r14_a1)
        else:
            bot.reply_to(message, "Введите высоту опущенную на эту сторону")
            bot.register_next_step_handler(message, rect_r14_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r14_a1)

def rect_r14_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r14_a2)
        else:
            rect_r14_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r14_a2)

def rect_r14_s(message):
    global a, b,metric, P, ae1
    s = a*b
    P = a*4
    bot.send_message(message.from_user.id, "сторона = "+ str(a) + metric + " \nВысота = "+ str(b) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r24_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r24_a1)
        else:
            bot.reply_to(message, "Введите любой угол")
            bot.register_next_step_handler(message, rect_r24_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r24_a1)

def rect_r24_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r24_ae1)
        else:
            rect_r24_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r24_ae1)

def rect_r24_s(message):
    global a, b,metric, P, ae1
    s = (a**2)*math.sin(ae1*math.pi/180)
    P = a*4
    bot.send_message(message.from_user.id, "Сторона = "+ str(a) + metric + " \n Угол = "+ str(ae1) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r34_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r34_a1)
        else:
            bot.reply_to(message, "Введите вторую диагональ")
            bot.register_next_step_handler(message, rect_r34_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r34_a1)

def rect_r34_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r34_a2)
        else:
            rect_r34_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r34_a2)

def rect_r34_s(message):
    global a, b,metric, P, ae1, c
    s = a*b/2
    c = math.sqrt((a/2)**2+(b/2)**2)
    P = c*4
    bot.send_message(message.from_user.id, "Сторона = "+ str(c) + metric + " \n Первая диагональ = "+ str(a) + metric + " \n Вторая диагональ = "+ str(b) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r44_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r44_a1)
        else:
            bot.reply_to(message, "Введите радиус вписанной окружности")
            bot.register_next_step_handler(message, rect_r44_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r44_a1)

def rect_r44_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r44_a2)
        else:
            rect_r44_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r44_a2)


def rect_r44_s(message):
    global a, b,metric, P, ae1, c
    s = 2*a*b
    P = a*4
    bot.send_message(message.from_user.id, "Сторона = "+ str(a) + metric + " \n Радиус вписанной окружности = "+ str(b) + metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r54_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r54_a1)
        else:
            bot.reply_to(message, "Введите любой угол")
            bot.register_next_step_handler(message, rect_r54_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r54_a1)

def rect_r54_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r54_ae1)
        else:
            rect_r54_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r54_ae1)

def rect_r54_s(message):
    global a, b,metric, P, ae1, c
    s = 4*(a**2)/math.sin(ae1*math.pi/180)
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')
    bot.send_message(message.from_user.id, "Угол = "+ str(ae1) + " \n Радиус вписанной окружности = "+ str(a) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")

def v_rect_r5(message):
    keyboard_rect_r5 = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id,"a - 1 основание \nb - 2 основание\n m - средняя линия\nc,d - боковые стороны\n h - высота опущенная на основание \n fi - любой с 4-х углов между диагоналями \n d1, d2 - диагонали")
    key_r15 = types.InlineKeyboardButton(text='a, b, h', callback_data='r15')
    key_r25 = types.InlineKeyboardButton(text='m, h', callback_data='r25')
    key_r35 = types.InlineKeyboardButton(text='d1, d2, fi', callback_data='r35')
    key_r45 = types.InlineKeyboardButton(text='a,b,c,d', callback_data='r45')
    keyboard_rect_r5.add(key_r15, key_r25, key_r35, key_r45)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect_r5)

def rect_r15_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r15_a1)
        else:
            bot.reply_to(message, "Введите второе основание")
            bot.register_next_step_handler(message, rect_r15_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r15_a1)

def rect_r15_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r15_a2)
        else:
            bot.reply_to(message, "Введите второе основание")
            bot.register_next_step_handler(message, rect_r15_a3)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r15_a2)

def rect_r15_a3(message):
    global h
    try:
        h = float(message.text)
        if h <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r15_a3)
        else:
            rect_r15_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r15_a3)

def rect_r15_s(message):
    global a, b,metric, P, ae1, c
    s = (a+b)*h/2
    bot.send_message(message.from_user.id, "Первое основание = "+ str(a) + metric + " \n Второе основание = "+ str(b) + metric + " \n Высота = "+ str(h) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r25_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r25_a1)
        else:
            bot.reply_to(message, "Введите высоту")
            bot.register_next_step_handler(message, rect_r25_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r25_a1)

def rect_r25_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r25_a2)
        else:
            rect_r25_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r25_a2)

def rect_r25_s(message):
    global a, b,metric, P, ae1, c
    s = a*b
    bot.send_message(message.from_user.id, "Средняя линия = "+ str(a) + metric + " \n Высота = "+ str(b) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r35_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r35_a1)
        else:
            bot.reply_to(message, "Введите высоту")
            bot.register_next_step_handler(message, rect_r35_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r35_a1)

def rect_r35_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r35_a2)
        else:
            bot.reply_to(message, "Введите любой угол между диагоналями")
            bot.register_next_step_handler(message, rect_r35_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r35_a2)

def rect_r35_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r35_ae1)
        else:
            rect_r35_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r35_ae1)

def rect_r35_s(message):
    global a, b,metric, P, ae1, c
    s = math.sin(ae1*math.pi/180)*a*b/2
    bot.send_message(message.from_user.id, "Первая диагональ =  "+ str(a) + metric + " \n Вторая диагональ = "+ str(b) + metric + " \n Угол между диагоналями = "+ str(ae1))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r45_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r45_a1)
        else:
            bot.reply_to(message, "Введите второе основание")
            bot.register_next_step_handler(message, rect_r45_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r45_a1)

def rect_r45_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r45_a2)
        else:
            bot.reply_to(message, "Введите первую боковую сторону")
            bot.register_next_step_handler(message, rect_r45_a3)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r45_a2)

def rect_r45_a3(message):
    global c
    try:
        c = float(message.text)
        if c <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r45_a3)
        else:
            bot.reply_to(message, "Введите вторую боковую сторону")
            bot.register_next_step_handler(message, rect_r45_a4)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r45_a3)

def rect_r45_a4(message):
    global h
    try:
        h = float(message.text)
        if h <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r45_a4)
        else:
            rect_r45_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r45_a4)

def rect_r45_s(message):
    global a, b,metric, P, ae1, c, h
    s = ((a+b)/2)*math.sqrt((c**2)-((((a-b)**2) + (c**2) - (h**2))/(2*(a-b)))**2)
    if s == 0:
        bot.send_message(message.from_user.id, "Такой трапеции не существует")
    else:
        bot.send_message(message.from_user.id, "Первое основание =  "+ str(a) + metric + " \n Второе основание = "+ str(b) + metric + " \n Первая боковая сторона = "+ str(c) + metric + " \nВторая боковая сторона = "+ str(h) + metric)
        bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
        bot.send_sticker(message.from_user.id,'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def v_rect_r6(message):
    keyboard_rect_r6 = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id,"a, b - неравные стороны \nfi - угол между a i b\n fi1 - угол между сторонами, равными a \nfi2 -  угол между сторонами, равными b\n r - радиус вписанной окружности\n d1, d2 - диагонали")
    key_r16 = types.InlineKeyboardButton(text='a, b, fi', callback_data='r16')
    key_r26 = types.InlineKeyboardButton(text='a, b, fi1, fi2', callback_data='r26')
    key_r36 = types.InlineKeyboardButton(text='a, b, r', callback_data='r36')
    key_r46 = types.InlineKeyboardButton(text='d1, d2', callback_data='r46')
    keyboard_rect_r6.add(key_r16, key_r26, key_r36, key_r46)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect_r6)



def rect_r16_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r16_a1)
        else:
            bot.reply_to(message, "Введите b")
            bot.register_next_step_handler(message, rect_r16_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r16_a1)

def rect_r16_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r16_a2)
        else:
            bot.reply_to(message, "Введите fi")
            bot.register_next_step_handler(message, rect_r16_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r16_a2)

def rect_r16_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r16_ae1)
        else:
            rect_r16_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r16_ae1)

def rect_r16_s(message):
    global a, b,metric, P, ae1, c, h
    s = a*b*math.sin(ae1*math.pi/180)
    bot.send_message(message.from_user.id, "a =  "+ str(a) + metric + " \n b = "+ str(b) + metric + " \n fi = "+ str(ae1))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r26_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r26_a1)
        else:
            bot.reply_to(message, "Введите b")
            bot.register_next_step_handler(message, rect_r26_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r26_a1)

def rect_r26_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r26_a2)
        else:
            bot.reply_to(message, "Введите fi1")
            bot.register_next_step_handler(message, rect_r26_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r26_a2)

def rect_r26_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r26_ae1)
        else:
            bot.reply_to(message, "Введите fi2")
            bot.register_next_step_handler(message, rect_r26_ae2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r26_ae1)

def rect_r26_ae2(message):
    global ae2
    try:
        ae2 = int(message.text)
        if ae2 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r26_ae2)
        else:
            rect_r26_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r26_ae2)

def rect_r26_s(message):
    global a, b,metric, P, ae1, c, h
    s = (((a**2)*math.sin(ae1*math.pi/180))/2)+(((b**2)*math.sin(ae2*math.pi/180))/2)
    bot.send_message(message.from_user.id, "a =  "+ str(a) + metric + " \n b = "+ str(b) + metric + " \n fi1 = "+ str(ae1) + " \n fi2 = "+ str(ae2))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r36_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r36_a1)
        else:
            bot.reply_to(message, "Введите b")
            bot.register_next_step_handler(message, rect_r36_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r36_a1)

def rect_r36_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r36_a2)
        else:
            bot.reply_to(message, "Введите r")
            bot.register_next_step_handler(message, rect_r36_a3)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r36_a2)

def rect_r36_a3(message):
    global c
    try:
        c = float(message.text)
        if c <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r36_a3)
        else:
            rect_r36_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r36_a3)

def rect_r36_s(message):
    global a, b,metric, P, ae1, c, h
    s = (a+b)*c
    bot.send_message(message.from_user.id, "a =  "+ str(a) + metric + " \n b = "+ str(b) + metric + " \n r = "+ str(c) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def rect_r46_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r46_a1)
        else:
            bot.reply_to(message, "Введите d2")
            bot.register_next_step_handler(message, rect_r46_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r46_a1)

def rect_r46_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r46_a2)
        else:
            rect_r46_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r46_a2)

def rect_r46_s(message):
    global a, b,metric, P, ae1, c, h
    s = a*b/2
    bot.send_message(message.from_user.id, "d1 =  "+ str(a) + metric + " \n d2 = "+ str(b) + metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def v_rect_r7(message):
    keyboard_rect_r7 = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id,"d1,d2 - диагонали \nfi - любой угол между ними")
    key_r17 = types.InlineKeyboardButton(text='d1, d2, fi', callback_data='r17')
    keyboard_rect_r7.add(key_r17)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect_r7)

def rect_r17_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r17_a1)
        else:
            bot.reply_to(message, "Введите d2")
            bot.register_next_step_handler(message, rect_r17_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r17_a1)

def rect_r17_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r17_a2)
        else:
            bot.reply_to(message, "Введите fi")
            bot.register_next_step_handler(message, rect_r17_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r17_a2)

def rect_r17_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, rect_r17_ae1)
        else:
            rect_r17_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r17_ae1)

def rect_r17_s(message):
    global a, b,metric, P, ae1, c, h
    s = a*b*math.sin(ae1*math.pi/180)/2
    bot.send_message(message.from_user.id, "d1 =  "+ str(a) + metric + " \n d2 = "+ str(b) + metric + " \n fi = "+ str(ae1))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def v_rect_r8(message):
    keyboard_rect_r8 = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id,"a,b,c,d - длины сторон четырёхугольника")
    key_r18 = types.InlineKeyboardButton(text='a,b,c,d', callback_data='r18')
    keyboard_rect_r8.add(key_r18)
    bot.send_message(message.from_user.id, text="Что вам дано?", reply_markup=keyboard_rect_r8)

def rect_r18_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r18_a1)
        else:
            bot.reply_to(message, "Введите b")
            bot.register_next_step_handler(message, rect_r18_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r18_a1)

def rect_r18_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r18_a2)
        else:
            bot.reply_to(message, "Введите c")
            bot.register_next_step_handler(message, rect_r18_a3)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r18_a2)

def rect_r18_a3(message):
    global c
    try:
        c = float(message.text)
        if c <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r18_a3)
        else:
            bot.reply_to(message, "Введите d")
            bot.register_next_step_handler(message, rect_r18_a4)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r18_a3)

def rect_r18_a4(message):
    global h
    try:
        h = float(message.text)
        if h <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, rect_r18_a4)
        else:
            rect_r18_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, rect_r18_a4)

def rect_r18_s(message):
    global a, b,metric, P, ae1, c, h
    p = (a+b+c+h)/2
    s = math.sqrt((p-a)*(p-b)*(p-c)*(p-h))
    bot.send_message(message.from_user.id, "a =  "+ str(a) + metric + " \n b = "+ str(b) + metric + " \n c = "+ str(c)+ metric + " \n d = "+ str(h)+ metric)
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def three_t1_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t1_a1)
        else:
            bot.reply_to(message, "Введите вторую сторону")
            bot.register_next_step_handler(message, three_t1_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t1_a1)



def three_t1_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t1_a2)
        else:
            bot.reply_to(message, "Введите угол между ними")
            bot.register_next_step_handler(message, three_t1_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t1_a2)

def three_t1_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, three_t1_ae1)
        else:
            three_t1_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t1_ae1)

def three_t1_s(message):
    global a, b, ae1, c, metric, P
    s = (a*b*math.sin(ae1*math.pi/180))/2
    c = math.sqrt(a**2 + b**2 - 2*b*a*math.cos(ae1*math.pi/180))
    P = a+b+c
    bot.send_message(message.from_user.id, "1 сторона = "+ str(a) + metric +"\n 2 сторона = " + str(b) + metric +"\n 3 сторона = " + str(c)+ metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/sqt/sqt2.gif')
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def three_t2_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t2_a1)
        else:
            bot.reply_to(message, "Введите второе сторону")
            bot.register_next_step_handler(message, three_t2_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t2_a1)

def three_t2_a2(message):
    global b
    try:
        b = float(message.text)
        if b <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t2_a2)
        else:
            bot.reply_to(message, "Введите третью сторону")
            bot.register_next_step_handler(message, three_t2_a3)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t2_a2)

def three_t2_a3(message):
    global c
    try:
        c = float(message.text)
        if c <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t2_a3)
        else:
            three_t2_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t2_a3)

def three_t2_s(message):
    global a, b, ae1, c, metric, P, p
    P = a+b+c
    p = P/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    bot.send_message(message.from_user.id, "1 сторона = "+ str(a) + metric +"\n 2 сторона = " + str(b) + metric +"\n 3 сторона = " + str(c)+ metric)
    bot.send_message(message.from_user.id, "Периметр = " + str(P) + metric)
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/geron/g1.gif')
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/geron/g2.gif')
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def three_t3_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t3_a1)
        else:
            bot.reply_to(message, "Введите высоту опущенную на эту сторону")
            bot.register_next_step_handler(message, three_t3_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t3_a1)

def three_t3_a2(message):
    global h
    try:
        h = float(message.text)
        if h <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t3_a1)
        else:
            three_t3_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t3_a1)

def three_t3_s(message):
    global a, b, ae1, c, metric, P, p
    s = a*h/2
    bot.send_message(message.from_user.id, "сторона = "+ str(a) + metric +"\n высота = " + str(h) + metric)
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/sqt/sqt1.gif')
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def three_t4_a1(message):
    global a
    try:
        a = float(message.text)
        if a <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t4_a1)
        else:
            bot.reply_to(message, "Введите первый прилегающий угол")
            bot.register_next_step_handler(message, three_t4_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t4_a1)

def three_t4_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, three_t4_ae1)
        else:
            bot.reply_to(message, "Введите второй прилегающий угол")
            bot.register_next_step_handler(message, three_t4_ae2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t4_ae1)

def three_t4_ae2(message):
    global ae2
    try:
        ae2 = int(message.text)
        if ae2 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, three_t4_ae2)
        else:
            three_t4_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t4_ae2)

def three_t4_s(message):
    global a, b, ae1, ae2, c, metric, P, p
    s = (a**2)/(2*((math.cos(ae1*math.pi/180)/math.sin(ae1*math.pi/180))+(ae2*math.pi/180)/math.sin(ae2*math.pi/180)))
    bot.send_message(message.from_user.id, "1 сторона = "+ str(a) + metric +"\n 1 угол = " + str(ae1) + metric +"\n 2 угол = " + str(ae2)+ metric)
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/sqt/sqt3.gif')
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def three_t5_a1(message):
    global P
    try:
        P = float(message.text)
        if P <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t5_a1)
        else:
            bot.reply_to(message, "Введите r вписанной окружности")
            bot.register_next_step_handler(message, three_t5_a2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t5_a1)

def three_t5_a2(message):
    global r
    try:
        r = float(message.text)
        if r <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t5_a2)
        else:
            three_t5_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t5_a2)

def three_t6_a1(message):
    global R
    try:
        R = float(message.text)
        if R <= 0:
            bot.reply_to(message, "Вы ввели отрицательное число (или 0). Попробуйте ещё раз")
            bot.register_next_step_handler(message, three_t6_a1)
        else:
            bot.reply_to(message, "Введите 1 угол")
            bot.register_next_step_handler(message, three_t6_ae1)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t6_a1)

def three_t6_ae1(message):
    global ae1
    try:
        ae1 = int(message.text)
        if ae1 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, three_t6_ae1)
        else:
            bot.reply_to(message, "Введите 2 угол")
            bot.register_next_step_handler(message, three_t6_ae2)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t6_ae1)

def three_t6_ae2(message):
    global ae2
    try:
        ae2 = int(message.text)
        if ae2 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, three_t6_ae2)
        else:
            bot.reply_to(message, "Введите 3 угол")
            bot.register_next_step_handler(message, three_t6_ae3)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t6_ae2)

def three_t6_ae3(message):
    global ae3
    try:
        ae3 = int(message.text)
        if ae3 <= 0 or ae1 > 179:
            bot.reply_to(message, "Ошибка")
            bot.register_next_step_handler(message, three_t6_ae2)
        else:
            three_t6_s(message)
    except:
        bot.reply_to(message, "Ошибка ввода. Попробуйте ещё раз")
        bot.register_next_step_handler(message, three_t6_ae2)


def three_t5_s(message):
    global a, b, ae1, c, metric, P, p, r
    p = P/2
    s = p*r
    bot.send_message(message.from_user.id, "Периметр = "+ str(P) + metric +"\n Радиус вписанной окружности = " + str(r))
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/sqt/sqt4.gif')
    bot.send_photo(message.from_user.id, 'https://www.resolventa.ru/sprris/planimetry/geron/g2.gif')
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')

def three_t6_s(message):
    global a, b, ae1, c, metric, P, p, r, ae2, ae3, R
    s = 2*(R**2)*math.sin(ae1*math.pi/180)*math.sin(ae2*math.pi/180)*math.sin(ae3*math.pi/180)
    bot.send_message(message.from_user.id, "Радиус описанной окружности "+ str(R) + metric +"\n 1 угол = " + str(ae1)+"\n 2 угол = " + str(ae2)+"\n 3 угол = " + str(ae3))
    bot.send_message(message.from_user.id, "Площадь = " + str(s) + metric + "^2")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAECiRBg4wdtLtHd1wsxHMlx6nwWmjfHOgACzg0AAoaSqUi4lcvk-fNpmiAE')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker_metric(call):
    global metric
    if call.data == "мм" or call.data == "см" or call.data == "м" or call.data == "км":
        metric = str(call.data)
        bot.send_message(call.message.chat.id, "Сохранено")
        bot.send_sticker(call.message.chat.id,'CAACAgIAAxkBAAECiPVg4wX7JUv-aOZpQRIU7wkSB-qR8AACQw4AAt9koEhG5Y-_Y25_eiAE')


    if call.data == "three":
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAECiRRg4wd7Wn6APMIt-HxT8Z9hDnHG_wACrxAAAvA_oEiUQHEdeFxSMSAE')
        v_three(call)
    elif call.data == "rect":
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAECiRRg4wd7Wn6APMIt-HxT8Z9hDnHG_wACrxAAAvA_oEiUQHEdeFxSMSAE')
        v_rect(call)
    elif call.data == "circ":
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAECiRRg4wd7Wn6APMIt-HxT8Z9hDnHG_wACrxAAAvA_oEiUQHEdeFxSMSAE')
        v_circ(call)
    elif call.data == "n":
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAECiRRg4wd7Wn6APMIt-HxT8Z9hDnHG_wACrxAAAvA_oEiUQHEdeFxSMSAE')
        v_n(call)

    elif call.data == "t1":
        bot.send_message(call.message.chat.id, "Введите первую сторону")
        bot.register_next_step_handler(call.message, three_t1_a1)
    elif call.data == "t2":
        bot.send_message(call.message.chat.id, "Введите первую сторону")
        bot.register_next_step_handler(call.message, three_t2_a1)
    elif call.data == "t3":
        bot.send_message(call.message.chat.id, "Введите сторону")
        bot.register_next_step_handler(call.message, three_t3_a1)
    elif call.data == "t4":
        bot.send_message(call.message.chat.id, "Введите сторону")
        bot.register_next_step_handler(call.message, three_t4_a1)
    elif call.data == "t5":
        bot.send_message(call.message.chat.id, "Введите периметр")
        bot.register_next_step_handler(call.message, three_t5_a1)
    elif call.data == "t6":
        bot.send_message(call.message.chat.id, "Введите Радиус описанной окружности")
        bot.register_next_step_handler(call.message, three_t6_a1)
    elif call.data == "r1":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/sqf/sqf3.png')
        v_rect_r1(call)
    elif call.data == "r11":
        bot.send_message(call.message.chat.id, "Введите первую сторону")
        bot.register_next_step_handler(call.message, rect_r11_a1)
    elif call.data == "r21":
        bot.send_message(call.message.chat.id, "Введите диагональ")
        bot.register_next_step_handler(call.message, rect_r21_a1)
    elif call.data == "r31":
        bot.send_message(call.message.chat.id, "Введите радиус описанной окружности")
        bot.register_next_step_handler(call.message, rect_r31_a1)
    elif call.data == "r2":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/sqf/sqf4.png')
        v_rect_r2(call)
    elif call.data == "r12":
        bot.send_message(call.message.chat.id, "Введите сторону")
        bot.register_next_step_handler(call.message, rect_r12_a1)
    elif call.data == "r22":
        bot.send_message(call.message.chat.id, "Введите 1 сторону")
        bot.register_next_step_handler(call.message, rect_r22_a1)
    elif call.data == "r32":
        bot.send_message(call.message.chat.id, "Введите 1 диагональ")
        bot.register_next_step_handler(call.message, rect_r32_a1)
    elif call.data == "r3":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/sqf/sqf10.png')
        v_rect_r3(call)
    elif call.data == "r13":
        bot.send_message(call.message.chat.id, "Введите сторону")
        bot.register_next_step_handler(call.message, rect_r13_a1)
    elif call.data == "r23":
        bot.send_message(call.message.chat.id, "Введите радиус вписанной окружности")
        bot.register_next_step_handler(call.message, rect_r23_a1)
    elif call.data == "r33":
        bot.send_message(call.message.chat.id, "Введите диагональ")
        bot.register_next_step_handler(call.message, rect_r33_a1)
    elif call.data == "r43":
        bot.send_message(call.message.chat.id, "Введите Радиус описанной окружности")
        bot.register_next_step_handler(call.message, rect_r43_a1)
    elif call.data == "r4":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/sqf/sqf11.png')
        v_rect_r4(call)
    elif call.data == "r14":
        bot.send_message(call.message.chat.id, "Введите сторону")
        bot.register_next_step_handler(call.message, rect_r14_a1)
    elif call.data == "r24":
        bot.send_message(call.message.chat.id, "Введите сторону")
        bot.register_next_step_handler(call.message, rect_r24_a1)
    elif call.data == "r34":
        bot.send_message(call.message.chat.id, "Введите первую диагональ")
        bot.register_next_step_handler(call.message, rect_r34_a1)
    elif call.data == "r44":
        bot.send_message(call.message.chat.id, "Введите сторону")
        bot.register_next_step_handler(call.message, rect_r44_a1)
    elif call.data == "r54":
        bot.send_message(call.message.chat.id, "Введите радиус вписанной окружности")
        bot.register_next_step_handler(call.message, rect_r54_a1)
    elif call.data == "r5":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/sqf/sqf17.png')
        v_rect_r5(call)
    elif call.data == "r15":
        bot.send_message(call.message.chat.id, "Введите первое основание")
        bot.register_next_step_handler(call.message, rect_r15_a1)
    elif call.data == "r25":
        bot.send_message(call.message.chat.id, "Введите среднюю линию")
        bot.register_next_step_handler(call.message, rect_r25_a1)
    elif call.data == "r35":
        bot.send_message(call.message.chat.id, "Введите 1 диагональ")
        bot.register_next_step_handler(call.message, rect_r35_a1)
    elif call.data == "r45":
        bot.send_message(call.message.chat.id, "Введите первое основание")
        bot.register_next_step_handler(call.message, rect_r45_a1)
    elif call.data == "r6":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/sqf/sqf21.png')
        v_rect_r6(call)
    elif call.data == "r16":
        bot.send_message(call.message.chat.id, "Введите a")
        bot.register_next_step_handler(call.message, rect_r16_a1)
    elif call.data == "r26":
        bot.send_message(call.message.chat.id, "Введите a")
        bot.register_next_step_handler(call.message, rect_r26_a1)
    elif call.data == "r36":
        bot.send_message(call.message.chat.id, "Введите a")
        bot.register_next_step_handler(call.message, rect_r36_a1)
    elif call.data == "r46":
        bot.send_message(call.message.chat.id, "Введите d1")
        bot.register_next_step_handler(call.message, rect_r46_a1)
    elif call.data == "r7":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/sqf/sqf24.png')
        v_rect_r7(call)
    elif call.data == "r17":
        bot.send_message(call.message.chat.id, "Введите d1")
        bot.register_next_step_handler(call.message, rect_r17_a1)
    elif call.data == "r8":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/sqf/sqf32.png')
        v_rect_r8(call)
    elif call.data == "r18":
        bot.send_message(call.message.chat.id, "Введите a")
        bot.register_next_step_handler(call.message, rect_r18_a1)
    elif call.data == "c1":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/l/l8.png')
        bot.send_message(call.message.chat.id,"R - Радиус описанной окружности \n alpha - Угол")
        bot.send_message(call.message.chat.id, "Введите R")
        bot.register_next_step_handler(call.message, circ_c1_a1)
    elif call.data == "c2":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/l/l9.png')
        bot.send_message(call.message.chat.id, "R - Радиус описанной окружности \n alpha - Угол")
        bot.send_message(call.message.chat.id, "Введите R")
        bot.register_next_step_handler(call.message, circ_c2_a1)
    elif call.data == "c3":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/l/l10.png')
        bot.send_message(call.message.chat.id, "R - Радиус описанной окружности \n alpha - Угол")
        bot.send_message(call.message.chat.id, "Введите R")
        bot.register_next_step_handler(call.message, circ_c3_a1)
    elif call.data == "n1":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/regular/reg2.png')
        bot.send_message(call.message.chat.id, "Введите a")
        bot.register_next_step_handler(call.message, n_1_a1)
    elif call.data == "n2":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/regular/reg3.png')
        bot.send_message(call.message.chat.id, "Введите r")
        bot.register_next_step_handler(call.message, n_2_a1)
    elif call.data == "n3":
        bot.send_photo(call.message.chat.id, 'https://www.resolventa.ru/sprris/planimetry/regular/reg4.png')
        bot.send_message(call.message.chat.id, "Введите R")
        bot.register_next_step_handler(call.message, n_3_a1)


@bot.message_handler(content_types=["text"])

def send_error(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECiPNg4wUn1akZx_F6-NPZGRNMQgUmHgACNA4AAlYkoUhui8XpegABv4QgBA')
    send_help(message)

if __name__ == '__main__':
    bot.polling(none_stop=True)