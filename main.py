# https://colab.research.google.com/drive/1vELbQ26inppMxV2wQwTaM-aw5tc_WNzs#scrollTo=3f9UQfRfpXde
from flask import Flask

app = Flask(__name__)  # создали сервер


@app.route('/')  # @ аннотация указывает на какую страницу должна вести ссылка
def index_page():
    return 'Hello word!'


app.run()  # запустили сервер
