# teletext-twitter - creates pages for vbit2 teletext system
# (c) Mark Pentler 2018 (https://github.com/mpentler)
# see README.md for details on getting it running or run with -h
# text processor module

import textwrap
import re

ESCAPE = chr(27)
text_colours = {"red" : 65, "green" : 66, "yellow" : 67 , "blue" : 68, "magenta" : 69, "cyan" : 70, "white" : 71}

def tweet_remove_emojis(tweet):
    # remove pesky emoji characters
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
    # all tweets are https t.co links, so this is all we need
    url_pattern = re.compile("https://\S+")
    tweet = url_pattern.sub('[LINK]', tweet)
    return tweet

def tweet_highlight_query(tweet, query, config):
    tweet = tweet.replace((" " + query + " "),
                          (ESCAPE + chr(text_colours[config["search_highlight"]]) + query + ESCAPE + chr(text_colours[config["tweet_colour"]])))
    return tweet

def charsub(text):
    # Now our character substitutions. The teletext English character set doesn't support a lot of characters!
    text = text.replace("’", "'")
    text = text.replace("_", "-")
    text = text.replace("#", "_")
    text = text.replace("“", "\"")
    text = text.replace("…", "...")
    return text
