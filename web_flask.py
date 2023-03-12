from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/answer', methods=['POST', 'GET'])
def answer():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        global dct
        professions = []
        if request.form.get('accept-engineer', ''):
            professions.append('Инженер-исследователь')
        if request.form.get('accept-engineer2', ''):
            professions.append('Инженер-строитель')
        if request.form.get('accept-pilot', ''):
            professions.append('Пилот')
        if request.form.get('accept-meteo', ''):
            professions.append('Метеоролог')
        if request.form.get('accept-engineer3', ''):
            professions.append('Инженер по жизнеобеспечению')
        if request.form.get('accept-engineer4', ''):
            professions.append('Инженер по радиационной защите')
        if request.form.get('accept-doctor', ''):
            professions.append('Врач')
        if request.form.get('accept-eczobio', ''):
            professions.append('Экзобиолог')
        ready = 'True' if request.form.get('accept', '') else 'False'
        dct = {
            "surname": request.form.get('lastname', ''),
            "name": request.form.get('name', ''),
            "education": request.form.get('class', ''),
            "profession": ', '.join(professions),
            "sex": request.form.get('sex', ''),
            "motivation": request.form.get('about', ''),
            "ready": ready
        }
        return redirect('/auto_answer')


@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', title="Анкета", dct=dct)


dct = {}
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)