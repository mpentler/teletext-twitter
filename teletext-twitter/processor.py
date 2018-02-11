# teletext-twitter - creates pages for vbit2 teletext system
# (c) Mark Pentler 2018 (https://github.com/mpentler)
# see README.md for details on getting it running or run with -h
# text processor module

import textwrap
import re

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

def charsub(text):
    # do any substitutitons that will change the length of the text
    text = text.replace("…", "...")
    
    # these could be enhanced but this will save packets
    text = text.replace("’", "'")
    text = text.replace("‘", "'")
    text = text.replace("“", "\"")
    text = text.replace("”", "\"")
    return text

enhancementmapping = {
    # map to L1 replacement, enhancement mode, enhancement data
    "#":[0x5F,0,0],
    "_":[0x2D,0x10,0x5F]
    #todo: lots more mappings!
}

def charenhance(text,offset):
    newtext = ""
    enhancements = []
    for index, char in enumerate(text):
        newchar = enhancementmapping.get(char, [ord(char),0,0])
        if newchar[0] > 127:
            newchar = [0x7F,0,0] # blank unknown unicode characters
        newtext += chr(newchar[0])
        if (newchar[1]):
            enhancements.append([index+offset,newchar[1],newchar[2]])
    return newtext,enhancements