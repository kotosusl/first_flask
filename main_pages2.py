from flask import Flask, url_for, request
import os

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        if os.path.isfile('static/img/avatar.png'):
            image = f'''<img src="{url_for('static', filename='img/avatar.png')}">'''
        else:
            image = ''
        return f'''<!doctype html>
                        <html lang="en">
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
                            <h1>Загрузка фотографии</h1>
                            <h3 style="text-align: center;">для участия в миссии</h3>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <br><br>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <br>
                                <div>
                                {image}
                                </div>
                                <br>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file'].read()
        image = open('static/img/avatar.png', 'wb')
        image.write(f)
        image.close()
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)