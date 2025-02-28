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


@app.route('/image_mars')
def bootstrap():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <h1 class="h">Ждт нас марс!</h1>

    <img src="{url_for('static', filename='mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
    
    <p style="font-size: 40px;">
    <p class="p1">Человечество вырастает из детства.</p>
    <p class="p2">Человечеству мала одна планета.</p>
    <p class="p3">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="p4">И начнем с Марса!</p>
    <p class="p5">Присоединяйся!</p><p>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
