import json

from flask import request
import tinder_api
from storage import store, save


def hecking_facebook_auth():
    data = request.json
    if data is None:
        data = json.loads(request.data)
    if 'username' not in data \
            or 'password' not in data \
            or 'tanda_id' not in data:
        return {'response': 'Error! Malformed data'}
    username = data['username']
    password = data['password']
    tanda_id = data['tanda_id']

    fb_access = tinder_api.get_fb_access_token(username, password)
    if 'error' in fb_access:
        return {'response': 'Failed to login. Incorrect email/password '
                            'combination?'}
    fb_user = tinder_api.get_fb_id(fb_access)

    store[tanda_id] = {'fb_access': fb_access, 'fb_user': fb_user}
    save()

    return {'response': 'success'}
