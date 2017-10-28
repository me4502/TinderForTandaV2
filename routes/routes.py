from flask import request, abort
from storage import save, get_id
from sqs import sqs_queue

def hook():
    if request.json['payload']['topic'] == 'clockin.updated':
        try:
            user = get_id(request.json['payload']['body']['user_id'])
            sqs_queue.send_message(MessageBody='Hello World')
        except:
            abort(401)

        return clockin(request.json)

def clockin(req):
    # Use the tinder api to find the person's song and
    # post a request to Byron's server with the name of the song
    # requests.post('http://localhost:12345', data = {'song':'value'})
    return "clockin"


def photo(req):
    # Do nothing at all
    return "photo"
