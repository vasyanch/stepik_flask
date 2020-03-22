from flask import Flask, render_template

from data import tours, departures


app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html', tours=tours, departures=departures)


@app.route('/departure/<departure>/')
def render_departure(departure):
    return render_template('departure.html', tours=tours, departures=departures, departure=departure)


@app.route('/tour/<int:id>/')
def render_tour(id):
    return render_template('tour.html', tour=tours.get(id), departures=departures)


@app.errorhandler(404)
def render_not_found(error):
    return f"page not found", 404


@app.errorhandler(500)
def render_server_error(error):
    return f"server is broken {error.original_exception}", 500


if __name__ == '__main__':
    app.run(debug=True)
