import telebot
from telebot import types
from random import*


bot = telebot.TeleBot('ваш токен')
@bot.message_handler(commands=['start']) #стартовый текст
def hello(message):
    hello = 'Приветствую вас, вы зашли на мой бот. Перед вами есть кнопки для взаимодействия с ботом. Если их нет, введите команду "/кнопки"'
    bot.send_message(message.chat.id, hello)


@bot.message_handler(commands= ['монетка']) #подброс монетки
def monetka(message):
    monetka = randint(1, 2)
    if monetka == 1:
        bot.send_message(message.chat.id, '<b>Орёл</b>', parse_mode='html')
    elif monetka == 2:
        bot.send_message(message.chat.id, '<b>Решка</b>', parse_mode='html')

@bot.message_handler(commands=['канал автора']) #walking on the streets channel ютуб
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('крутой канал' , url ='https://www.youtube.com/channel/UCn5PVfRHRC3L6yd87IEa2Dg'))
    bot.send_message(message.chat.id, 'Крутой канал:', reply_markup=markup)


@bot.message_handler(commands=['кнопки']) #бот показывает кнопки
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)

    website = types.KeyboardButton('Канал автора на ютуб')

    монетка = types.KeyboardButton('монетка')

    mem = types.KeyboardButton('мем')

    локация = types.KeyboardButton('локация')

    ID = types.KeyboardButton('Мой ID в телеграм')

    sticker = types.KeyboardButton('стикер')


    markup.add(website, монетка, mem,локация,  sticker, ID)
    bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup=markup)

@bot.message_handler()
def user_text(message):
    bot.send_message(message.chat.id, '<b>ВНИМАНИЕ! Для этого бота больше нет идей, поэтому бот будет заброшен. Если у вас есть какие-либо предложения, то вы можете найти кнопку "Предложить идею" и следовать инструкциям "</b>', parse_mode='html')

    if message.text == 'Привет':
        bot.send_message(message.chat.id,'И тебе привет', parse_mode='html')

    elif message.text == 'Предложить идею':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Напишите мне сообщение', url='https://t.me/Platonloveyko'))
        bot.send_message(message.chat.id, 'Автор', reply_markup=markup)




    elif message.text == 'Канал автора на ютуб':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('крутой канал', url='https://www.youtube.com/channel/UCn5PVfRHRC3L6yd87IEa2Dg'))
        bot.send_message(message.chat.id, 'Крутой канал:', reply_markup=markup)

    # elif message.text == 'Получить скриншот':  Функция в разработке...
        # bot.send_message(message.chat.id, '<b>Данная функция находится в разработке</b>' , parse_mode='html')
        # screen = screenshot('s.jpg')
        # # sc = open(screen, 'rb')
        # bot.send_document(message.chat.id, 's.jpg', 'rb')

    elif message.text == 'монетка':
        monetka = randint(1, 2)
        if monetka == 1:
            bot.send_message(message.chat.id, '<b>Орёл</b>', parse_mode='html')
        elif monetka == 2:
            bot.send_message(message.chat.id, '<b>Решка</b>', parse_mode='html')

    elif message.text == 'мем':
        mem1 = open('meme1.PNG','rb')
        mem2 = open('meme2.PNG', 'rb')
        mem3 = open('meme3.PNG', 'rb')
        mem4 = open('meme4.PNG', 'rb')
        rand = randint(1,4)
        if rand == 1:
            bot.send_photo(message.chat.id, mem1)
        elif rand == 2:
            bot.send_photo(message.chat.id, mem2)
        elif rand == 3:
            bot.send_photo(message.chat.id, mem3)
        elif rand == 4:
            bot.send_photo(message.chat.id, mem4)

    elif message.text == 'Мой ID в телеграм':
        bot.send_message(message.chat.id, f'Ваш айди: {message.from_user.id}', parse_mode='html')

    elif message.text == 'Я бот?':
        bot.send_message(message.chat.id, f'Результат: {message.from_user.is_bot}', parse_mode='html')



    elif message.text == 'локация':
        bot.send_location(message.chat.id, 45.46701619311258, 133.39271910650052)

    elif message.text == 'стикер':
        sticker = open('понасенко8.webp', 'rb')
        bot.send_sticker(message.chat.id, sticker)

    else:
        bot.send_message(message.chat.id, 'Моя твоя не понимать')

bot.polling(none_stop=True)