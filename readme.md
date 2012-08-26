Moneychanger
============

Moneychanger is a small service which tracks the exchange rates for currencies
over time.


Requirements
------------

* Redis


Routes
------

### / GET
Returns a list of currencies which are tracked.

```
{
  "currencies": [
    "jpy",
    "cad",
    "aud"
  ]
}
```

### /\<code>/ GET
Returns a list of dates which have exchange rates for the currency code. Returns `404` if not found.

```
{
  "currency": "cad", 
  "dates": [
    "2012-01-01", 
    "2012-01-02"
  ]
}
```

### /\<code>/\<date>/ GET
Returns the exchange rate for a specific currency code and date. Returns `404` if not found.

```
{
  "date": "2012-01-01", 
  "currency": "cad", 
  "base_currency": "usd", 
  "rate": "1.23"
}
```

### /\<code>/\<date>/ PUT
Sets the exchange rate for a specific currency code and date. Returns the rate that was set.

```
>>> url = 'http://127.0.0.1:5000/jpy/2012-01-03/'
>>> r = requests.put(url, data={'rate': 200})
>>> r.text
u'{"date": "2012-01-03", "currency": "jpy", "base_currency": "usd", "rate": "200"}'
```
