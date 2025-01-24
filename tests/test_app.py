from flask.testing import FlaskClient
from tests.fixtures.expected_jsons import EXPECTED_JSON


def test_get_rates(client: FlaskClient, test_database: None) -> None:
    # given
    date_from = "2015-12-30"
    date_to = "2016-02-02"
    org = "CNSGH"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = EXPECTED_JSON
    assert response.status_code == 200
    assert response.get_json() == expected_json


def test_get_rates_from_and_to_dates_are_the_same(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2016-01-03"
    date_to = "2016-01-03"
    org = "CNSGH"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = [{"day": "2016-01-03", "average_price": None}]
    assert response.status_code == 200
    assert response.get_json() == expected_json


def test_get_rates_lowercase_port_code(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2015-12-30"
    date_to = "2016-02-02"
    org = "cnsgh"
    dst = "nlrtm"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = EXPECTED_JSON
    assert response.status_code == 200
    assert response.get_json() == expected_json


def test_get_rates_non_existent_origin(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2016-01-01"
    date_to = "2016-01-02"
    org = "RULED"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = [
        {"day": "2016-01-01", "average_price": None},
        {"day": "2016-01-02", "average_price": None},
    ]
    assert response.status_code == 200
    assert response.get_json() == expected_json


def test_get_rates_non_existent_destination(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2016-01-03"
    date_to = "2016-01-05"
    org = "CNSGH"
    dst = "HTOVN"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = [
        {"day": "2016-01-03", "average_price": None},
        {"day": "2016-01-04", "average_price": None},
        {"day": "2016-01-05", "average_price": None},
    ]
    assert response.status_code == 200
    assert response.get_json() == expected_json


def test_get_rates_incorrect_date_format(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "01.01.2016"
    date_to = "10.01.2016"
    org = "CNSGH"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = {"error": "Incorrect date or sequence of dates"}
    assert response.status_code == 422
    assert response.get_json() == expected_json


def test_get_rates_dates_are_incorrect(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2016-02-20"
    date_to = "2016-01-10"
    org = "CNSGH"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = {"error": "Incorrect date or sequence of dates"}
    assert response.status_code == 422
    assert response.get_json() == expected_json


def test_get_rates_earlier_than_available_date_range(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2014-10-08"
    date_to = "2014-10-10"
    org = "CNSGH"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = [
        {"day": "2014-10-08", "average_price": None},
        {"day": "2014-10-09", "average_price": None},
        {"day": "2014-10-10", "average_price": None},
    ]
    assert response.status_code == 200
    assert response.get_json() == expected_json


def test_get_rates_not_available_date_range_ports(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2024-11-25"
    date_to = "2024-11-26"
    org = "SSSSS"
    dst = "ttg"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = [
        {"day": "2024-11-25", "average_price": None},
        {"day": "2024-11-26", "average_price": None},
    ]
    assert response.status_code == 200
    assert response.get_json() == expected_json
