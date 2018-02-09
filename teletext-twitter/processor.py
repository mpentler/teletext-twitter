# teletext-twitter - creates pages for vbit2 teletext system
# (c) Mark Pentler 2018 (https://github.com/mpentler)
# see README.md for details on getting it running or run with -h
# tweet processor module

import textwrap
import re

def tweet_remove_emojis(tweet): # character replacement and stripping function
    # first, get rid of as many emojis as possible
    emoji_pattern = re.compile("[" # our unicode ranges go here. this will need frequent tweaking
                              u"\U00002300-\U000023FF" # misc technical
                              u"\U000024C2-\U0001F251" # enclosed characters including flags
                              u"\U0001F300-\U0001F5FF" # symbols & pictographs
                              u"\U0001F600-\U0001F67F" # emoticons
                              u"\U0001F680-\U0001F9FF" # transport & map symbols
                               "]+", flags=re.UNICODE)
    tweet = emoji_pattern.sub(r'', tweet)
    return tweet

def tweet_remove_urls(tweet):
    url_pattern = re.compile("https://\S+")
    tweet = url_pattern.sub('[LINK]', tweet)
    return tweet

def charsub(text):
    # Now our character substitutions. The teletext English character set doesn't support a lot of characters!
    text = text.replace("’", "'")
    text = text.replace("_", "-")
    text = text.replace("#", "_")
    text = text.replace('“', '"')

    return text
