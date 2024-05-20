import datetime

def is_date_object(input):
    return isinstance(input, datetime.date) and not isinstance(input, datetime.datetime)
