from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return "Missiya"


@app.route('/index')
def index():
    return 'I na Marse'


@app.route('/promotion')
def promotion():
    return """<p style="font-size: 40px;
                        color: red;
                        box-shadow: 0 0 100px 50px red;">Человечество вырастает из детства.
            <br>
            Человечеству мала одна планета.
            <br>
            Мы сделаем обитаемыми безжизненные пока планеты.
            <br>
            И начнем с Марса!
            <br>
            Присоединяйся!<p>"""


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
