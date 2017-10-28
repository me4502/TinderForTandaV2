from __future__ import print_function

import json

from flask import request, abort
from storage import save, get_id, has_id
from datetime import date
from sqs import sqs_queue
import requests

import os
from dotenv import load_dotenv, find_dotenv

TANDA_KEY = os.environ.get("TANDA_KEY")


def hook():
    # This is a ClockIn
    if request.json['payload']['topic'] == 'clockin.updated':
        # Check if the user was late with:
        # (bool) wasLate(request.json['payload']['body']['user_id'], request.json['payload']['body']['time']))

        user_id = request.json['payload']['body']['user_id']

        if has_id(user_id):
            user = get_id(request.json['payload']['body']['user_id'])

            sqs_queue.send_message(MessageBody='Hello World')
        else:
            return json.dumps({'response': 'Unknown user'})

        return json.dumps({'response': 'success'})


def photo(req):
    # Do nothing at all
    return "photo"


def send_messages(fb_user_data, late_time):
    pass


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
