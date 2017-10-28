from flask import request
from datetime import date
import requests

config = {
    "auth_code": "bearer 64bcdf0cb293f0808835e2fae294409435b6521585a8bb874d3bf5fffb3fe1fe",
}


def hook():
    if request.json['payload']['topic'] == 'clockin.updated':
        return clockin(request.json)
    elif request.json['payload']['topic'] == 'clockin.photo':
        return photo(request.json)


def clockin(req):
    # Use the tinder api to find the person's song and
    # post a request to Byron's server with the name of the song
    # requests.post('http://localhost:12345', data = {'song':'value'})
    return "clockin"


def photo(req):
    # Do nothing at all
    return "photo"


def wasLate(userid, clockTime):
    print("GOING!")
    today = date.today().isoformat()
    headers = {"Authorization": config['auth_code']}
    params = {"user_ids": userid, "from": today, "to": today}
    r = requests.get("https://my.tanda.co/api/v2/schedules/",
                     params=params, headers=headers)
    if r.text != "[]":
        return r.json()[0]['start'] < clockTime
    else:
        return False
