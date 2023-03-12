from flask import Flask, url_for

app = Flask(__name__)


@app.route('/carousel')
def sample_file_upload():
    urls = []
    for i in range(5):
        urls.append(url_for('static', filename=f'img/mars{i}.png'))
    return f"""<!DOCTYPE html>
                    <html lang="ru">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>

                        <title>Пейзажи Марса</title>
                    </head>
                    <body>
                        <h1 style="text-align: center;">Пейзажи Марса</h1>
                
                        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                    <ol class="carousel-indicators">
                        <li data-slide-to="0" class="active"></li>
                        <li data-slide-to="1"></li>
                        <li data-slide-to="2"></li>
                        <li data-slide-to="3"></li>
                        <li data-slide-to="4"></li>
                    </ol>
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img class="d-block w-100" src="{urls[0]}" alt="First slide">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{urls[1]}" alt="Second slide">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{urls[2]}" alt="Third slide">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{urls[3]}" alt="Fourth slide">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{urls[4]}" alt="Fifth slide">
                        </div>
                    </div>
                    </body>
                    </html>"""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)