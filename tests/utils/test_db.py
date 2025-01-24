from datetime import date

from psycopg2.extras import RealDictRow
from rates_api.utils.db import get_daily_rates


def test_get_daily_rates(test_database: None) -> None:
    # given
    date_from = date(2015, 12, 30)
    date_to = date(2016, 1, 4)
    org = "CNSGH"
    dst = "RULED"

    # when
    daily_rates = get_daily_rates(date_from, date_to, org, dst)

    # then
    expected_rate_piece = {"day": "2016-01-01", "average_price": 2009}
    rate_selection = {
        "day": str(daily_rates[2]["day"]),
        "average_price": daily_rates[2]["avg_price"],
    }
    assert rate_selection == expected_rate_piece


def test_get_daily_rates_data_are_not_found(test_database: None) -> None:
    # given
    date_from = date(2015, 12, 31)
    date_to = date(2016, 1, 1)
    org = "CNSGH"
    dst = "YYYYY"

    # when
    daily_rates = get_daily_rates(date_from, date_to, org, dst)
    print(daily_rates)

    # then
    expected_daily_rates = [
        RealDictRow([("day", date(2015, 12, 31)), ("avg_price", None)]),
        RealDictRow([("day", date(2016, 1, 1)), ("avg_price", None)]),
    ]
    assert daily_rates == expected_daily_rates
