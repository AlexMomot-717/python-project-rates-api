from datetime import date, datetime, timedelta


def dates_validator(date_from: str, date_to: str) -> bool:
    if not check_date_format(date_from) or not check_date_format(date_to):
        return False
    date_from_formatted = convert_date_type(date_from)
    date_to_formatted = convert_date_type(date_to)
    if date_to_formatted < date_from_formatted:
        return False
    return True


def check_date_format(date_param: str) -> bool:
    try:
        datetime.fromisoformat(date_param)
        return True
    except ValueError:
        return False


def convert_date_type(date_param: str) -> date:
    date_els: list[int] = list(int(i) for i in date_param.split("-"))
    dt_date = datetime(date_els[0], date_els[1], date_els[2]).date()
    return dt_date


def get_dates(date_from: str, date_to: str) -> list[str]:
    start_day = extract_data(date_from)
    end_day = extract_data(date_to)
    delta = timedelta(days=1)
    dates = []
    while start_day <= end_day:
        dates.append(str(start_day.date()))
        start_day += delta
    return dates


def extract_data(date_param: str) -> datetime:
    return datetime.strptime(date_param, "%Y-%m-%d")
