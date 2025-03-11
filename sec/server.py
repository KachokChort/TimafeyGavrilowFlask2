from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<word>')
@app.route('/index/<word>')
def index(word):
    return render_template('base.html', title=word)

@app.route('/training/<prog>')
def training(prog):
    return render_template('training.html', prog=prog)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')