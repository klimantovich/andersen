import telebot
import re
from github import Github

TELEGRAM_TOKEN = '5520420147:AAGp7rxLkhhCApNlUZVJ1ADko13OyjkHPPg'
GITHUB_TOKEN = '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'

repository_address = 'https://github.com/klimantovich/andersen.git'
master_branch_address = 'https://github.com/klimantovich/andersen/tree/master/'
repository_name = 'klimantovich/andersen'

bot = telebot.TeleBot(TELEGRAM_TOKEN)   
repo = Github(GITHUB_TOKEN).get_repo(repository_name)

# return list of completed tasks   
def get_tasks_list():
    contents = repo.get_contents("")
    counter = 1
    tasks = ''
    for content_file in contents:
        if re.match(r'^Exercise', content_file.path) is not None:
            tasks += str(counter) + ".\t" + content_file.path + "\n"
            counter += 1
    return tasks

def generate_task_link(exercise_number):
    return master_branch_address + "Exercise" + str(exercise_number[0])

'''
USER MESSAGES HANDLERS
'''
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "/git - вернуть адрес репозитория,\n/tasks - получить нумерованный список выполненных заданий,\n/task # - ссылка на папку свыполненной задачей номер #")

@bot.message_handler(regexp=r'^/task ([1-9]{1}|1[0-4]{1})$')
def handle_task_number(message):
    exercise_number = re.findall(r'([1-9]{1}|1[0-4]{1})$', message.text)
    bot.send_message(message.chat.id, generate_task_link(exercise_number))

@bot.message_handler(commands=['git', 'tasks'])
def hundle_main_commands(message):
    if message.text == "/git":
        bot.send_message(message.chat.id, "https://github.com/klimantovich/andersen.git")
    elif message.text == "/tasks":
        bot.send_message(message.chat.id, get_tasks_list())

@bot.message_handler(content_types=['text'])
def handle_other_input(message):
	bot.send_message(message.from_user.id, "Неизвестная команда. Справка: /help.")

bot.polling(none_stop=True, interval=0)