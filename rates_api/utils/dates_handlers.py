from datetime import date, datetime


def dates_validator(date_from: str, date_to: str) -> tuple[date, date] | None:
    """
    Function checks dates values, format and sequence
    :rtype: object
    :param date_from: the first date of the requested period
    :param date_to: the last date of the requested period
    :return: Tuple of two date objects if both dates are valid otherwise None
    """
    if not check_date_format(date_from) or not check_date_format(date_to):
        return None
    # Convert dates  into datetime.date objects for later comparison:
    date_from_formatted = convert_date_type(date_from)
    date_to_formatted = convert_date_type(date_to)
    if date_to_formatted < date_from_formatted:
        return None
    else:
        return date_from_formatted, date_to_formatted


def check_date_format(date_param: str) -> bool:
    """
    Function checks date value and format
    :param date: string
    :return: True if date are valid otherwise False
    """
    try:
        datetime.fromisoformat(date_param)
        return True
    except ValueError:
        return False


def convert_date_type(date_param: str) -> date:
    """
    Function converts date into datetime.date object
    :param date: string
    :return: Datetime.date object
    """
    date_els: list[int] = list(int(i) for i in date_param.split("-"))
    dt_date = datetime(date_els[0], date_els[1], date_els[2]).date()
    return dt_date


def parse_date(date_param: str) -> datetime:
    """
    Function converts date string into datetime object
    :param date: string
    :return: Datetime object
    """
    return datetime.strptime(date_param, "%Y-%m-%d")
