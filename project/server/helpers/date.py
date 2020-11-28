import calendar

from datetime import datetime


def __get_iso8601_format():
    return '%Y-%m-%dT%H:%M:%SZ'


def from_iso8601(date):
    return datetime.strptime(date, __get_iso8601_format())


def is_last_day_of_month(date):
    return calendar.monthrange(date.year, date.month)[1] <= date.day


def to_iso8601(date):
    return date.strftime(__get_iso8601_format())
