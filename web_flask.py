import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/list_prof/<list>')
def training(list):
    with open('templates/list_prof.json', "rt", encoding="utf8") as f:
        new_list = json.loads(f.read())
    return render_template('base.html', list=list, list_prof=new_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)