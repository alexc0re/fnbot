import re


def alpha_space_filter(message):
    return bool(re.match('^[a-zA-Z\s]*$', message.text))