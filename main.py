import telebot

token = ""
with open("Token") as file:
    token = file.readline().rstrip()
bot = telebot.TeleBot(token)