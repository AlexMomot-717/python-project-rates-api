from flask.testing import FlaskClient
from tests.fixtures.expected_jsons import (
    EXPECTED_JSON,
    EXPECTED_JSON_DATES_ARE_PARTLY_AVAILABLE,
    EXPECTED_JSON_DATES_ARE_THE_SAME,
)


def test_get_rates(client: FlaskClient, test_database: None) -> None:
    # given
    date_from = "2016-01-01"
    date_to = "2016-01-10"
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


def test_get_rates_dates_are_partly_available(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2015-10-30"
    date_to = "2016-02-28"
    org = "CNSGH"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = EXPECTED_JSON_DATES_ARE_PARTLY_AVAILABLE
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
    expected_json = EXPECTED_JSON_DATES_ARE_THE_SAME
    assert response.status_code == 200
    assert response.get_json() == expected_json


def test_get_rates_lowercase_port_code(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2016-01-01"
    date_to = "2016-01-10"
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
    date_to = "2016-01-10"
    org = "RULED"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = {"error": "Not found"}
    assert response.status_code == 404
    assert response.get_json() == expected_json


def test_get_rates_non_existent_destination(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2016-01-01"
    date_to = "2016-01-10"
    org = "CNSGH"
    dst = "HTOVN"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = {"error": "Not found"}
    assert response.status_code == 404
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
    expected_json = {"error": "Not found"}
    assert response.status_code == 404
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
    expected_json = {"error": "Not found"}
    assert response.status_code == 404
    assert response.get_json() == expected_json


def test_get_rates_earlier_than_available_date_range(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2010-05-07"
    date_to = "2014-10-10"
    org = "CNSGH"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = {"error": "Not found"}
    assert response.status_code == 404
    assert response.get_json() == expected_json


def test_get_rates_later_than_available_date_range(
    client: FlaskClient, test_database: None
) -> None:
    # given
    date_from = "2016-02-01"
    date_to = "2016-03-30"
    org = "CNSGH"
    dst = "NLRTM"

    route = (
        f"/rates?date_from={date_from}&date_to={date_to}&origin={org}&destination={dst}"
    )

    # when
    response = client.get(route)

    # then
    expected_json = {"error": "Not found"}
    assert response.status_code == 404
    assert response.get_json() == expected_json
