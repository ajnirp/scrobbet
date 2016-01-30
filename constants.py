import os

WEBAPP = 'http://scrobbetserv.herokuapp.com/'
API_KEY = 'b27b214ef5f1aa035e30721a133e2ec3'
ATTRIBUTE_LIST = ['artist', 'title', 'album', 'tracknumber']
HOME_DIR = os.path.expanduser("~")
CONFIG_DIR = HOME_DIR + '/.config/'
SK_LOCAL_STORE = CONFIG_DIR + '.scrobbetsession'
SUPPORTED_MIME_TYPES = set([
    'audio/mpeg',
    'audio/mp4',
    'audio/m4a',
    'audio/ogg',
    'audio/flac',
    'audio/wav',
    'audio/aiff'
])