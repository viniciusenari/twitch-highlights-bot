import os
from dotenv import load_dotenv
import datetime as dt
load_dotenv()

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

def get_previous_saturday():
    today_weekday = dt.datetime.today().weekday()
    if today_weekday == 6:
        return (dt.datetime.now() - dt.timedelta(1)).replace(hour = 11, minute = 59, second= 59)
    return (dt.datetime.now() - dt.timedelta(today_weekday + 2)).replace(hour = 11, minute = 59, second= 59)

def parsetime_rfc(datetime_object):
    return dt.datetime.strftime(datetime_object, '%Y-%m-%dT%H:%M:%SZ')

def parsetime_dBY(datetime_object):
    return dt.datetime.strftime(datetime_object, '%d %B, %Y')

prev_week_saturday_rfc = parsetime_rfc(get_previous_saturday())
prev_week_sunday_rfc = parsetime_rfc((get_previous_saturday() - dt.timedelta(6)).replace(hour = 0, minute = 0, second= 0))

prev_week_saturday_dBY = parsetime_dBY(get_previous_saturday())
prev_week_sunday_dBY = parsetime_dBY((get_previous_saturday() - dt.timedelta(6)).replace(hour = 0, minute = 0, second= 0))