from flask import request
import requests


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
