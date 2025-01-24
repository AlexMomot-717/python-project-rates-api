from datetime import date

from rates_api.utils.dates_handlers import (
    check_date_format,
    convert_date_type,
    dates_validator,
    parse_date,
)


def test_dates_validator() -> None:
    # given
    date_from = "2016-01-01"
    date_to = "2016-01-10"

    # when
    result = dates_validator(date_from=date_from, date_to=date_to)

    # then
    expected_result = (date(2016, 1, 1), date(2016, 1, 10))
    assert result == expected_result


def test_dates_validator_incorrect_format() -> None:
    # given
    date_from = "01/01/2016"
    date_to = "2016-01-10"

    # when
    result = dates_validator(date_from=date_from, date_to=date_to)

    # then
    assert result is None


def test_dates_validator_date_to_is_less_than_date_from() -> None:
    # given
    date_from = "2016-01-10"
    date_to = "2016-01-01"

    # when
    result = dates_validator(date_from=date_from, date_to=date_to)

    # then
    assert result is None


def test_check_date_format() -> None:
    # given
    date_param = "2016-01-10"

    # when
    result = check_date_format(date_param)

    # then
    assert result is True


def test_check_date_format_incorrect_pattern() -> None:
    # given
    date_param = "01-01-2016"

    # when
    result = check_date_format(date_param)

    # then
    assert result is False


def test_check_date_format_not_iso_format() -> None:
    # given
    date_param = "2016-16-99"

    # when
    result = check_date_format(date_param)

    # then
    assert result is False


def test_convert_date_type():
    # given
    date_param = "2016-01-10"

    # when
    result = convert_date_type(date_param)

    # then
    result_type = type(result)
    expected_type = "<class 'datetime.date'>"
    assert str(result_type) == expected_type


def test_date_parse_date():
    # given
    date_param = "2016-01-10"

    # when
    result = parse_date(date_param)

    # then
    result_type = type(result)
    expected_type = "<class 'datetime.datetime'>"
    assert str(result_type) == expected_type
