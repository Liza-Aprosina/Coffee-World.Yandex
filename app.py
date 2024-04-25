from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def index_menu():
    return render_template('index_menu.html')


@app.route('/try')
def index_try():
    return render_template('index_try.html')


@app.route('/map')
def index_map():
    return render_template('index_map.html')


# index для тортов

@app.route('/cc')
def index_cc():
    return render_template('index_cc.html')


@app.route('/eclair')
def index_eclair():
    return render_template('index_eclair.html')


@app.route('/mr')
def index_mr():
    return render_template('index_mr.html')


@app.route('/pancho')
def index_pancho():
    return render_template('index_pancho.html')


@app.route('/pp')
def index_pp():
    return render_template('index_pp.html')


@app.route('/souffle')
def index_souffle():
    return render_template('index_souffle.html')


if __name__ == '__main__':
    app.run(debug=True)
