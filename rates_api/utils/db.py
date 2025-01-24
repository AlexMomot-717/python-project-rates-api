import os
from datetime import date
from typing import Any, Dict, List

import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()


def connect_db() -> Any:
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn


def get_daily_rates(
    date_from: date, date_to: date, org: str, dst: str
) -> List[Dict[str, Any]]:
    """
    Function selects data from database and calculates average prices
    :param date_from:
    :param date_to:
    :param org:
    :param dst:
    :return: list of RealDicts included day and
             average price (None if the conditions are not met)
    """
    conn = connect_db()
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cr:
        dict_cr.execute(
            """
            WITH days AS (
                SELECT generate_series(
                    %(date_from)s::date,
                    %(date_to)s::date,
                    '1 day'::interval
                 )::date AS day
            )
            SELECT
                 days.day,
                 CASE
                     WHEN COUNT(prices.price) >= 3
                     THEN AVG(prices.price)::INTEGER
                 END AS avg_price
            FROM days
            LEFT JOIN prices ON
                days.day = prices.day
                AND prices.orig_code = %(org)s
                AND prices.dest_code = %(dst)s
            GROUP BY days.day
            ORDER BY days.day;
            """,
            {
                "date_from": date_from,
                "date_to": date_to,
                "org": org.upper(),
                "dst": dst.upper(),
            },
        )
        target_daily_rates = dict_cr.fetchall()
        conn.close()
    daily_rates = []
    for daily_rate in target_daily_rates:
        daily_rates.append(daily_rate)
    return daily_rates
