from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def promotion_image():
    return f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" 
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <figure>
                        <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
                        <figcaption>Вот она какая, красная планета.</figcaption>
                    </figure>
                    <div class="alert alert-dark" role="alert">
                        Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                        И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                        Присоединяйся!
                    </div>
                </body>
                </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    return f"""<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="text" class="form-control" id="lastname" placeholder="Введите фамилию" name="lastname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    </br>
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        </br>
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <div class="form-group form-check">
                                        </br>
                                        <label for="job">Какие у Вас есть профессии?</label>
                                        <div class="job">
                                            <input type="checkbox" class="form-check-input" id="job-engineer" name="accept-engineer">
                                            <label class="form-check-label" for="form-check-input">Инженер-исследователь</label>
                                            </br>
                                            <input type="checkbox" class="form-check-input" id="job-engineer2" name="accept-engineer2">
                                            <label class="form-check-label" for="form-check-input">Инженер-строитель</label>
                                            </br>
                                            <input type="checkbox" class="form-check-input" id="job-pilot" name="accept-pilot">
                                            <label class="form-check-label" for="form-check-input">Пилот</label>
                                            </br>
                                            <input type="checkbox" class="form-check-input" id="job-meteo" name="accept-meteo">
                                            <label class="form-check-label" for="form-check-input">Метеоролог</label>
                                            </br>
                                            <input type="checkbox" class="form-check-input" id="job-engineer3" name="accept-engineer3">
                                            <label class="form-check-label" for="form-check-input">Инженер по жизнеобеспечению</label>
                                            </br>
                                            <input type="checkbox" class="form-check-input" id="job-engineer4" name="accept-engineer4">
                                            <label class="form-check-label" for="form-check-input">Инженер по радиационной защите</label>
                                            </br>
                                            <input type="checkbox" class="form-check-input" id="job-doctor" name="accept-doctor">
                                            <label class="form-check-label" for="form-check-input">Врач</label>
                                            </br>
                                            <input type="checkbox" class="form-check-input" id="job-eczobio" name="accept-eczobio">
                                            <label class="form-check-label" for="form-check-input">Экзобиолог</label>
                                        </div>
                                    </div>
                                     <div class="form-group">
                                     </br>
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        </br>
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>

                                    <div class="form-group">
                                        </br>
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    </br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)