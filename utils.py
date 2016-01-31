from constants import *
import mimetypes

def yes_no_prompt(prompt):
    return input(prompt + ' [y/N] ') in ['y', 'Y']

def color_string(message, message_type):
    # http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    SUCCESS_TERM_COLOR = '\033[92m'
    ERROR_TERM_COLOR = '\033[91m'
    NORMAL_TERM_COLOR = '\033[0m'
    if message_type is 'error':
        return ERROR_TERM_COLOR + message + NORMAL_TERM_COLOR
    elif message_type is 'success':
        return SUCCESS_TERM_COLOR + message + NORMAL_TERM_COLOR
    elif message_type is 'normal':
        return NORMAL_TERM_COLOR + message

def sigint_handler(signal, frame):
    # restore terminal colors, just in case
    print(utils.color_string('', 'normal'))
    exit(130)

# see if a response from last.fm has any errors, and if yes, return them
def check_response_error(parsed_response):
    error_xml_tag = parsed_response.lfm.error
    return error_xml_tag.text.strip() if error_xml_tag else None

def is_audio_file(filename):
    mime_type = mimetypes.guess_type(filename)[0]
    return mime_type in SUPPORTED_MIME_TYPES