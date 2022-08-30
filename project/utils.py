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

games_id = {
    'Just Chatting' : '509658',
    'League of Legends' : '21779',
    'Grand Theft Auto V' : '32982',
    'Minecraft' : '27471',
    'Counter-Strike: Global Offensive' : '32399',
    'VALORANT' : '516575',
    'Tom Clancy\'s Rainbow Six Siege' : '460630',
    'Apex Legends' : '511224',
    'Fortnite' : '33214',
    'Path of Exile' : '29307',
    'PUBG: BATTLEGROUNDS' : '493057',
    'Dead by Daylight' : '491487',
    'Teamfight Tactics' : '513143',
    'Dota 2' : '29595',
    'World of Warcraft' : '18122',
    'Call of Duty: Warzone' : '512710',
    'Hearthstone' : '138585'
}