import telebot

bot = telebot.TeleBot('5919819560:AAGBhtbTMi9RFHuODnTbZVgaGngK0gMVsWM')

value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton('%', callback_data='/100'),
                telebot.types.InlineKeyboardButton('MV', callback_data='Васькин Error'),
                telebot.types.InlineKeyboardButton('C', callback_data='C'),
                telebot.types.InlineKeyboardButton('⌫', callback_data='<='))
keyboard.row(   telebot.types.InlineKeyboardButton('xⁿ', callback_data='**'),
                telebot.types.InlineKeyboardButton('x²', callback_data='**2'),
                telebot.types.InlineKeyboardButton('√x', callback_data='**0.5'),
                telebot.types.InlineKeyboardButton('÷', callback_data='/'))
keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('×', callback_data='*'))
keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'))
keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'))
keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data='.'),
                telebot.types.InlineKeyboardButton('=', callback_data='='))   

@bot.message_handler(commands=['start', 'calculate'])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old
    data = query.data
    old = data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1] 
    elif data == '=':
        try:
            value = str(eval(value))
        except: 
            value = 'Ошибка!'
    else:
        value += data
    
    if (value != old and value != '') or (value != old and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old = '0'
        elif value == 'Васькин Error**2':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Жееееееесть', reply_markup=keyboard)
            old = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
            old = value
    
    if value == 'Ошибка!': value = '' 
    if value == 'Жееееееесть': value = ''
bot.polling(none_stop=False, interval = 0) # Запуск бота