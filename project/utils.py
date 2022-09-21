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

def parsetime(datetime_object):
    return dt.datetime.strftime(datetime_object, '%Y-%m-%dT%H:%M:%SZ')

prev_week_saturday = parsetime(get_previous_saturday())
prev_week_sunday = parsetime((get_previous_saturday() - dt.timedelta(6)).replace(hour = 0, minute = 0, second= 0))