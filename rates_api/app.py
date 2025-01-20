#!/usr/bin/env python3
from typing import Any

from flask import Flask, Response, abort, jsonify, make_response, request
from rates_api.utils.dates_handlers import dates_validator, get_dates
from rates_api.utils.db import get_available_dates, get_daily_rates

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.json.sort_keys = False  # type: ignore[attr-defined]


@app.route("/rates")
def get_rates() -> Response:
    date_from = request.args.get("date_from", "", type=str)
    date_to = request.args.get("date_to", "", type=str)
    orig = request.args.get("origin", "", type=str)
    dest = request.args.get("destination", "", type=str)

    if not dates_validator(date_from=date_from, date_to=date_to):
        abort(404)

    available_date_points = get_available_dates(date_from, date_to, orig, dest)
    if not available_date_points:
        abort(404)
    else:
        date_from_f, date_to_f = available_date_points
        daily_rates = get_daily_rates(orig, dest)
        if not daily_rates:
            abort(404)
        dates_range = get_dates(str(date_from_f), str(date_to_f))
        rates = []
        flag = 0
        for day in dates_range:
            for daily_rate in daily_rates:
                if day == str(daily_rate["day"]):
                    rate = {
                        "day": str(daily_rate["day"]),
                        "average_price": int(daily_rate["rate"]),
                    }
                    rates.append(rate)
                    flag = 1
                    break
            if not flag:
                rate = {"day": day, "average_price": None}
                rates.append(rate)
            flag = 0

        return jsonify(rates)


@app.errorhandler(404)
def not_found(error: Exception) -> Any:
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
