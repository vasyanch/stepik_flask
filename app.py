from flask import Flask, render_template

from data import tours, departures


app = Flask(__name__)


@app.route('/')
def render_index():
    sorted_tours = sort_by_price(tours)
    return render_template('index.html', tours=sorted_tours[:6], departures=departures)


@app.route('/departure/<departure>/')
def render_departure(departure):
    departure_tours = sort_by_price(
        {tour_id: value for tour_id, value in tours.items() if value['departure'] == departure}
    )
    prices = [tour[1]['price'] for tour in departure_tours]
    nights = [tour[1]['nights'] for tour in departure_tours]
    return render_template(
        'departure.html', tours=departure_tours, departures=departures, departure=departure,
        prices=prices, nights=nights
    )


@app.route('/tour/<int:tour_id>/')
def render_tour(tour_id):
    return render_template('tour.html', tour=tours.get(tour_id), departures=departures)


def sort_by_price(any_tours: dict) -> list:
    return sorted(any_tours.items(), key=lambda x: x[1]['price'])


if __name__ == '__main__':
    app.run()
