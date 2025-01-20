import datetime
import os
from typing import Any, Dict, List, Tuple

import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from rates_api.utils.dates_handlers import convert_date_type

load_dotenv()


def connect_db() -> Any:
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn


def get_available_dates(
    date_from: str, date_to: str, orig: str, dest: str
) -> Tuple[datetime.date, datetime.date] | None:
    date_from_f = convert_date_type(date_from)
    date_to_f = convert_date_type(date_to)
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute(
            "SELECT DISTINCT day "
            "FROM prices "
            "WHERE orig_code=%(org)s AND dest_code=%(dst)s "
            "ORDER BY day;",
            {
                "org": orig.upper(),
                "dst": dest.upper(),
            },
        )
        unique_dates = cur.fetchall()
        conn.close()
        if not unique_dates:
            return None
    actual_dates = []
    for date in unique_dates:
        actual_dates.append(date)
    start = actual_dates[0][0]
    end = actual_dates[-1][0]
    if (date_from_f < start) and (date_to_f > end):
        return start, end
    elif date_from_f < start < date_to_f <= end:
        return start, date_to_f
    elif (start <= date_from_f <= end) and (date_to_f > end):
        return date_from_f, end
    elif (date_from_f >= start) and (date_to_f <= end):
        return date_from_f, date_to_f
    return None


def get_daily_rates(org: str, dst: str) -> List[Dict[str, Any]] | None:
    conn = connect_db()
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cr:
        dict_cr.execute(
            "SELECT day, AVG(price) AS rate "
            "FROM prices "
            "WHERE orig_code=%(org)s AND dest_code=%(dst)s "
            "GROUP BY day "
            "HAVING COUNT(price) >= 3 "
            "ORDER BY day;",
            {
                "org": org.upper(),
                "dst": dst.upper(),
            },
        )
        target_daily_rates = dict_cr.fetchall()
        conn.close()
        if not target_daily_rates:
            return None
    daily_rates = []
    for daily_rate in target_daily_rates:
        daily_rates.append(daily_rate)
    return daily_rates
