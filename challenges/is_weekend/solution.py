import datetime

def is_weekend(date):
    if not isinstance(date, datetime.date):
        raise TypeError("Input is not a Date object")
    return date.weekday() in [5, 6]
