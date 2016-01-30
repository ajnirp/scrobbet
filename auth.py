from bs4 import BeautifulSoup as bs
import os
import requests
import webbrowser

from constants import *
import utils

# return session key if already stored else make dotfile and return False
def get_local_session_key():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    if not os.path.isfile(SK_LOCAL_STORE):
        delete_local_session_key()
        return False
    with open(SK_LOCAL_STORE, 'r') as f:
        sk = f.read(32)
        return sk if sk else None

# (re-)authorize if needed
def authorize():
    if get_local_session_key():
        if utils.yes_no_prompt('You already have a session key. Would you like to discard it and get another?'):
            delete_local_session_key()
            authorize()
            exit(0)
    else:
        print('Getting authentication token')
        auth_token, error = get_new_auth_token()
        if error: print(utils.color_string(error, 'error'))
        print("Hit Enter when you're done authorizing")
        request_authorization(auth_token)
        input()
        print('Getting session key')
        session_key, error = get_new_session_key(auth_token)
        if error: print(utils.color_string(error, 'error'))
        store_local_session_key(session_key)

def delete_local_session_key():
    print('Deleting current session key from', SK_LOCAL_STORE)
    open(SK_LOCAL_STORE, 'w').close()

# get authentication token in order to get user authorization
def get_new_auth_token():
    token_response = requests.post(WEBAPP + 'gettoken')
    parsed_response = bs(token_response.text)
    return parsed_response.token.string, utils.check_response_error(parsed_response)

# request session key from last.fm
def get_new_session_key(token):
    session_response = requests.post(WEBAPP + 'getsession', {'token': token})
    parsed_response = bs(session_response.text)
    return parsed_response.key.string, utils.check_response_error(parsed_response)

# get authorization from user to scrobble to their account
def request_authorization(token):
    url = 'http://www.last.fm/api/auth/?api_key=' + API_KEY + '&token=' + token
    webbrowser.open_new(url)

# store session key in the local config file
def store_local_session_key(session_key):
    print('Saving session key to', SK_LOCAL_STORE)
    with open(SK_LOCAL_STORE, 'w') as f:
        f.write(session_key)