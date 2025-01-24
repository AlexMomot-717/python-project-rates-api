#!/usr/bin/env python3
from typing import Any

from flask import Flask, Response, abort, jsonify, make_response, request
from rates_api.utils.dates_handlers import dates_validator
from rates_api.utils.db import get_daily_rates

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.json.sort_keys = False  # type: ignore[attr-defined]


@app.route("/rates")
def get_rates() -> Response:
    """
    Function extracts arguments from the query parameters, checks them,
    requests data from database and forms json object
    :param date_from: first date of the requested period
    :param date_to: last date of the requested period
    :param org: origin port code
    :param dst: destination port code
    :return: Json object included days and average prices or error info
    """
    date_from = request.args.get("date_from", "", type=str)
    date_to = request.args.get("date_to", "", type=str)
    orig = request.args.get("origin", "", type=str)
    dest = request.args.get("destination", "", type=str)

    date_validation_result = dates_validator(date_from, date_to)

    # If at least one of dates is incorrect or date from > date_to:
    if not date_validation_result:
        abort(422)

    # Valid dates converted into date format:
    date_from_f, date_to_f = date_validation_result

    # List of dicts included days and average prices from database:
    daily_rates = get_daily_rates(date_from_f, date_to_f, orig, dest)

    rates = [
        {"day": str(rate["day"]), "average_price": rate["avg_price"]}
        for rate in daily_rates
    ]

    return jsonify(rates)


@app.errorhandler(422)
def not_found(error: Exception) -> Any:
    error_info = {"error": "Incorrect date or sequence of dates"}
    return make_response(jsonify(error_info), 422)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
