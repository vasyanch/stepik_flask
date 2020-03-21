from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/departure/<departure>')
def render_departure(departure):
    return render_template('departure.html', departure=departure)


@app.route('/tour/<id>/')
def render_tour(id):
    return render_template('tour.html', id=id)


@app.errorhandler(404)
def render_not_found(error):
    return f"page not found", 404


@app.errorhandler(500)
def render_server_error(error):
    return f"server is broken {error.original_exception}", 500


if __name__ == '__main__':
    app.run()
