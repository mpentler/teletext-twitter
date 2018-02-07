# teletext-twitter - creates pages for vbit2 teletext system
# (c) Mark Pentler 2018 (https://github.com/mpentler)
# see README.md for details on getting it running or run with -h
# tweet processor module

import textwrap
import re

def clean_tweet(tweet): # character replacement and stripping function
    # first, get rid of as many emojis as possible
    emoji_pattern = re.compile("[" # our unicode ranges go here. this will need frequent tweaking
                              u"\U00002300-\U000023FF" # misc technical
                              u"\U000024C2-\U0001F251" # enclosed characters including flags
                              u"\U0001F300-\U0001F5FF" # symbols & pictographs
                              u"\U0001F600-\U0001F67F" # emoticons
                              u"\U0001F680-\U0001F9FF" # transport & map symbols
                               "]+", flags=re.UNICODE)
    tweet = emoji_pattern.sub(r'', tweet)

    # Now our character substitutions. The teletext English character set doesn't support a lot of characters!
    tweet = tweet.replace("’", "'")
    tweet = tweet.replace("_", "-")
    tweet = tweet.replace("#", "_")
    tweet = tweet.replace('“', '"')

    return tweet
