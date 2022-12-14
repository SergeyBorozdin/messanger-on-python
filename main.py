from flask import Flask, render_template, request
from datetime import datetime
import json  # импорт библиотеки для работы с json

app = Flask(__name__)  # создали сервер
all_messages = []  # переменная где храниться вся история чата
DB_FILE = 'db.json'


def load_messages():  # функция для загрузки сообщений из файла db.json
    with open(DB_FILE, 'r') as json_file:
        data = json.load(json_file)
    return data['messages']


all_messages = load_messages()  # загрузили сообщения


def save_messages():  # функ сохраняет историю в json файл
    data = {'messages': all_messages}
    with open(DB_FILE, 'w') as json_file:
        json.dump(data, json_file)


@app.route('/')  # @ аннотация указывает на какую страницу должна вести ссылка
def index_page():
    return 'Hello word!'


@app.route('/chat')  # ссылка на дисплей чата
def dispay_chart():  # отобразить наш чат по шаблону из  templates/form.htm
    return render_template('form.html')


# функция для добавления сообщения в список сообщений
def add_message(sender, text):
    new_message = {
        'sender': sender,
        'text': text,
        'time': datetime.now().strftime('%H:%M')
    }
    all_messages.append(new_message)  # append - добавлет сообщение в список all_messages
    save_messages()


@app.route('/send_message')  # http://127.0.0.1:5000/send_message?name=Vlad&text=Hello
def send_message():  # функ которая отправляет сообщение
    sender = request.args['name']
    text = request.args['text']
    add_message(sender, text)
    save_messages()
    return "OK"


# функция печати сообщения
def print_message(message):
    # message - это словарь, в котором есть ключи sender, text, time
    print('[', message['sender'], ']', message['text'], '| Время:', message['time'])


# функция для печати всех сообщений
def print_all_message(message_list):
    for msg in message_list:  # запускаем цикл по каждому значению в списке message_list
        print_message(msg)


# add_message('Влад', 'Привет как дела?')
# add_message('Петр', 'Привет Влад, я отлично')


@app.route('/get_messages')  # указываем ссылку по которой получаем все сообщения
def get_messages():  # получаем списком все сообщения
    return {'messages': all_messages}


app.run()  # запустили сервер
# https://live.skillbox.ru/webinars/code/pishem-interfeis-messendzhera-na-python011022/?utm_source=expertsender&utm_medium=email&utm_campaign=all_all_expertsender_email_invite1_intensive-564-2022-09_all_code_skillbox&utm_content=2022-10-01&utm_term=intensive_posting_old