import json

'''
{[
  id (from Tanda ID): {
    fb_access: Facebook Access Token,
    fb_user: Facebook User ID
  }
]}
'''
store = dict()  # This is basically MongoDB, right?


def load():
    with open('user_storage.dat', 'w+') as f:
        data = f.read()
        global store  # I always feel so dirty when I do this
        try:
            store = json.loads(data)
        except ValueError:
            store = dict()


def save():
    data = json.dumps(store)
    with open('user_storage.dat', 'w+') as f:
        f.write(data)


def get_id(id):
    return store[id]
