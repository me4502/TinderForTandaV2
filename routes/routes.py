from flask import request, abort
from storage import save, get_id
from datetime import date
from sqs import sqs_queue
import requests

import os
from dotenv import load_dotenv, find_dotenv

TANDA_KEY = os.environ.get("TANDA_KEY")


def hook():
    # This is a ClockIn
    if request.json['payload']['topic'] == 'clockin.updated':
        try:
            # Check if the user was late with: 
            # (bool) wasLate(request.json['payload']['body']['user_id'], request.json['payload']['body']['time']))

            user = get_id(request.json['payload']['body']['user_id'])

            sqs_queue.send_message(MessageBody='Hello World')
        except:
            abort(401)

        return request.json


def photo(req):
    # Do nothing at all
    return "photo"


def wasLate(userid, clockTime):
    today = date.today().isoformat()
    headers = {"Authorization": "bearer " + TANDA_KEY}
    params = {"user_ids": userid, "from": today, "to": today}
    r = requests.get("https://my.tanda.co/api/v2/schedules/",
                     params=params, headers=headers)
    if r.text != "[]":
        return r.json()[0]['start'] < clockTime
    else:
        return False
