from redis import StrictRedis

from flask import Flask, abort, jsonify, request
app = Flask(__name__)

redis = StrictRedis()


@app.route('/')
def currency_list():
    """List currencies which have any exchange rates"""
    currencies = redis.keys()
    return jsonify(currencies=currencies)


@app.route('/<code>/')
def date_list(code):
    """Get a list of dates that have exchange rates for a currency"""
    dates = redis.hkeys(code)
    if len(dates) == 0:
        abort(404)
    return jsonify(currency=code, dates=dates)


@app.route('/<code>/<date>/', methods=['GET', 'PUT'])
def exchange_on_date(code, date):
    if request.method == 'PUT':
        set_rate(code, date, request.form['rate'])
    return get_rate(code, date)


def get_rate(code, date):
    """Return the exchange rate for a currency on a specific date"""
    rate = redis.hget(code, date)
    if not rate:
        abort(404)
    return jsonify(currency=code, base_currency='usd', date=date, rate=rate)


def set_rate(code, date, rate):
    """Set the exchange rate for a currency on a specific date"""
    return redis.hset(code, date, rate)

if __name__ == '__main__':
    app.run(debug=True)
