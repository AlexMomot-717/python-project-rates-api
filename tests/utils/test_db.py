from rates_api.utils.db import get_available_dates, get_daily_rates


def test_get_available_dates(test_database: None) -> None:
    # given
    date_from = "2016-01-01"
    date_to = "2016-01-10"
    org = "CNSGH"
    dst = "NLRTM"

    # when
    date_from_avail, date_to_avail = get_available_dates(date_from, date_to, org, dst)

    # then
    assert str(date_from_avail) == date_from
    assert str(date_to_avail) == date_to


def test_get_available_dates_partly_available(test_database: None) -> None:
    # given
    date_from = "2015-01-01"
    date_to = "2017-01-10"
    org = "CNSGH"
    dst = "NLRTM"

    # when
    date_from_avail, date_to_avail = get_available_dates(date_from, date_to, org, dst)

    # then
    expected_date_from_available = "2016-01-01"
    expected_date_to_available = "2016-01-31"
    assert str(date_from_avail) == expected_date_from_available
    assert str(date_to_avail) == expected_date_to_available


def test_get_available_dates_are_the_same(test_database: None) -> None:
    # given
    date_from = "2016-01-01"
    date_to = "2016-01-01"
    org = "CNSGH"
    dst = "NLRTM"

    # when
    date_from_avail, date_to_avail = get_available_dates(date_from, date_to, org, dst)

    # then
    expected_date_from_available = "2016-01-01"
    expected_date_to_available = "2016-01-01"
    assert str(date_from_avail) == expected_date_from_available
    assert str(date_to_avail) == expected_date_to_available


def test_get_available_dates_are_earlier(test_database: None) -> None:
    # given
    date_from = "2015-01-01"
    date_to = "2015-03-10"
    org = "CNSGH"
    dst = "NLRTM"

    # when
    result = get_available_dates(date_from, date_to, org, dst)

    # then
    assert result is None


def test_get_available_dates_are_later(test_database: None) -> None:
    # given
    date_from = "2016-03-01"
    date_to = "2016-04-01"
    org = "CNSGH"
    dst = "NLRTM"

    # when
    result = get_available_dates(date_from, date_to, org, dst)

    # then
    assert result is None


def test_get_daily_rates(test_database: None) -> None:
    # given
    org = "CNSGH"
    dst = "RULED"

    # when
    daily_rates = get_daily_rates(org, dst)

    # then
    expected_rate_data = {"day": "2016-01-01", "average_price": 2009}
    rate_selection = {
        "day": str(daily_rates[0]["day"]),
        "average_price": int(daily_rates[0]["rate"]),
    }
    assert rate_selection == expected_rate_data


def test_get_daily_rates_non_existent_port_codet(test_database: None) -> None:
    # given
    org = "CNSGH"
    dst = "YYYY"

    # when
    daily_rates = get_daily_rates(org, dst)

    # then
    assert daily_rates is None
