# coding=utf-8
from __future__ import print_function

import json

from flask import request, abort

import tinder_api
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

            late_time = wasLate(user_id, request.json['payload']['body']['time'])

            if late_time < 0:
                send_messages(user, 0 - late_time)
        else:
            return json.dumps({'response': 'Unknown user'})

        return json.dumps({'response': 'success'})


def photo(req):
    # Do nothing at all
    return "photo"


def send_messages(fb_user_data, late_time):
    tinder_api.authverif(fb_user_data['fb_access'], fb_user_data['fb_user'])
    matches = tinder_api.get_updates()['matches']
    for match in matches:
        tinder_api.send_msg(match, """Hey babe, just letting you know I’m the
        kind of person who turns up to things {}
        minutes late. Hope you’re okay with that 😉""".format(late_time / 60))


def wasLate(userid, clockTime):
    today = date.today().isoformat()
    headers = {"Authorization": "bearer " + TANDA_KEY}
    params = {"user_ids": userid, "from": today, "to": today}
    r = requests.get("https://my.tanda.co/api/v2/schedules/",
                     params=params, headers=headers)
    if r.text != "[]":
        return r.json()[0]['start'] - clockTime
    else:
        return 0
