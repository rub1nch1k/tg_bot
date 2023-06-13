def main():
    from core import bot

    TOKEN = '5943109353:AAHKGUHf_x75IE-cpy2c20_ORPD5vkmRTCY'
    bot = bot.Bot(TOKEN)
    bot.infinity_polling()


if __name__ == '__main__':
    main()