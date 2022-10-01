from flask import Flask

app = Flask(__name__)  # создали сервер
all_messages = [] # переменная где храниться вся история чата



@app.route('/')  # @ аннотация указывает на какую страницу должна вести ссылка
def index_page():
    return 'Hello word!'

#функция для добавления сообщения в список сообщений
def add_message(sender, text, current_time):
  new_message = {
      'sender': sender,
      'text': text,
      'time': current_time
  }
  all_messages.append(new_message) #append - добавлет сообщение в список all_messages


#функция печати сообщения
def print_message(message):
  #message - это словарь, в котором есть ключи sender, text, time
  print('[', message['sender'], ']', message['text'], '| Время:', message['time'])

#функция для печати всех сообщений
def print_all_message(message_list):
  for msg in message_list: #запускаем цикл по каждому значению в списке message_list
    print_message(msg)

add_message("Влад", "Привет как дела?", "21:55")
add_message("Петр", "Привет Влад, я отлично", "21:58")

def get_all_messages(): #получаем списком все сообщения
    return {"messages" : all_messages}

app.run()  # запустили сервер
