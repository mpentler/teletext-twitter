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
    # do any substitutitons that will change the length of the text
    # mapping to different characters and level 1.5 enhancement will take place later
    text = text.replace("…", "...")
    text = text.replace("Ǆ", "DŽ")
    text = text.replace("ǅ", "Dž")
    text = text.replace("ǆ", "dž")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    
    # these could be enhanced but this will save packets
    text = text.replace("’", "'")
    text = text.replace("‘", "'")
    text = text.replace("“", "\"")
    text = text.replace("”", "\"")
    return text

enhancementmapping = {
    # map to L1 replacement character, enhancement mode, enhancement data
    
    "£":[0x23,0,0],
    "–":[0x60,0,0],
    "—":[0x60,0,0],
    "÷":[0x7e,0,0],
    "#":[0x5F,0,0],
    "[":[0x28,0x10,0x5b],
    "\\":[0x2f,0x10,0x5c],
    "]":[0x29,0x10,0x5d],
    "^":[0x5e,0x10,0x5e],
    "_":[0x60,0x10,0x5f],
    "`":[0x27,0x10,0x60],
    "{":[0x28,0x10,0x7b],
    "|":[0x7c,0x10,0x7c],
    "}":[0x29,0x10,0x7d],
    "~":[0x7f,0x10,0x7e],
    
    # grave
    "À":[0x41,0x11,0x41],"à":[0x61,0x11,0x61],"È":[0x45,0x11,0x45],"è":[0x65,0x11,0x65],"Ì":[0x49,0x11,0x49],"ì":[0x69,0x11,0x69],"Ò":[0x4F,0x11,0x4F],"ò":[0x6F,0x11,0x6F],"Ù":[0x55,0x11,0x55],"ù":[0x75,0x11,0x75],"Ǹ":[0x4E,0x11,0x4E],"ǹ":[0x6E,0x11,0x6e],"Ẁ":[0x57,0x11,0x57],"ẁ":[0x77,0x11,0x77],"Ỳ":[0x59,0x11,0x59],"ỳ":[0x79,0x11,0x79],
    
    # acute
    "Á":[0x41,0x12,0x41],"á":[0x61,0x12,0x61],"Ć":[0x43,0x12,0x43],"ć":[0x63,0x12,0x63],"É":[0x45,0x12,0x45],"é":[0x65,0x12,0x65],"Í":[0x49,0x12,0x49],"í":[0x69,0x12,0x69],"Ĺ":[0x4c,0x12,0x4c],"ĺ":[0x6c,0x12,0x6c],"Ń":[0x4e,0x12,0x4e],"ń":[0x6e,0x12,0x6e],"Ó":[0x4f,0x12,0x4f],"ó":[0x6f,0x12,0x6f],"Ŕ":[0x52,0x12,0x52],"ŕ":[0x72,0x12,0x72],"Ś":[0x53,0x12,0x53],"ś":[0x73,0x12,0x73],"Ú":[0x55,0x12,0x55],"ú":[0x75,0x12,0x75],"Ŵ":[0x57,0x12,0x57],"ŵ":[0x77,0x12,0x77],"Ý":[0x59,0x12,0x59],"ý":[0x79,0x12,0x79],"Ź":[0x5a,0x12,0x5a],"ź":[0x7a,0x12,0x7a],
    
    # circumflex
    "Â":[0x41,0x13,0x41],"â":[0x61,0x13,0x61],"Ê":[0x45,0x13,0x45],"ê":[0x65,0x13,0x65],"Î":[0x49,0x13,0x49],"î":[0x69,0x13,0x69],"Ô":[0x4f,0x13,0x4f],"ô":[0x6f,0x13,0x6f],"Û":[0x55,0x13,0x55],"û":[0x75,0x13,0x75],"Ŵ":[0x57,0x13,0x57],"ŵ":[0x77,0x13,0x77],"Ý":[0x59,0x13,0x59],"ý":[0x79,0x13,0x79],
    
    # tilde
    "Ã":[0x41,0x14,0x41],"ã":[0x61,0x14,0x61],"Ñ":[0x4e,0x14,0x4e],"ñ":[0x6e,0x14,0x6e],"Õ":[0x4f,0x14,0x4f],"õ":[0x6f,0x14,0x6f],
    
    # macron
    "Ā":[0x41,0x15,0x41],"ā":[0x61,0x15,0x61],"Ē":[0x45,0x15,0x45],"ē":[0x65,0x15,0x65],"Ī":[0x49,0x15,0x49],"ī":[0x69,0x15,0x69],"Ū":[0x55,0x15,0x55],"ū":[0x75,0x15,0x75],
    
    # breve
    "Ă":[0x41,0x16,0x41],"ă":[0x61,0x16,0x61],"Ĕ":[0x45,0x16,0x45],"ĕ":[0x65,0x16,0x65],"Ĭ":[0x49,0x16,0x49],"ĭ":[0x69,0x16,0x69],"Ŏ":[0x4f,0x16,0x4f],"ŏ":[0x6f,0x16,0x6f],"Ŭ":[0x55,0x16,0x55],"ŭ":[0x75,0x16,0x75],"Ğ":[0x47,0x16,0x47],"ğ":[0x67,0x16,0x67],
    
    # dot
    "Ė":[0x45,0x17,0x45],"ė":[0x65,0x17,0x65],"Ż":[0x5a,0x17,0x5a],"ż":[0x7a,0x17,0x7a],
    
    # diaeresis/umlaut
    "Ä":[0x41,0x18,0x41],"ä":[0x61,0x18,0x61],"Ë":[0x45,0x18,0x45],"ë":[0x65,0x18,0x65],"Ï":[0x49,0x18,0x49],"ï":[0x69,0x18,0x69],"Ö":[0x4f,0x18,0x4f],"ö":[0x6f,0x18,0x6f],"Ü":[0x55,0x18,0x55],"ü":[0x75,0x18,0x75],"Ẅ":[0x57,0x18,0x57],"ẅ":[0x77,0x18,0x77],"Ÿ":[0x59,0x18,0x59],"ÿ":[0x79,0x18,0x79],
    
    # ring
    "Å":[0x41,0x1a,0x41],"Å":[0x41,0x1a,0x41],"å":[0x61,0x1a,0x61],"Ů":[0x55,0x1a,0x55],"ů":[0x75,0x1a,0x75],
    
    # cedilla/comma,hook
    "Ç":[0x43,0x1b,0x43],"ç":[0x63,0x1b,0x63],"Ķ":[0x4b,0x1b,0x4b],"ķ":[0x6b,0x1b,0x6b],"Ļ":[0x4c,0x1b,0x4c],"ļ":[0x6c,0x1b,0x6c],"Ņ":[0x4e,0x1b,0x4e],"ņ":[0x6e,0x1b,0x6e],"Ş":[0x53,0x1b,0x53],"Ș":[0x53,0x1b,0x53],"ş":[0x73,0x1b,0x73],"ș":[0x73,0x1b,0x73],"Ț":[0x54,0x1b,0x54],"ț":[0x74,0x1b,0x74],
    
    # double acute
    "A̋":[0x41,0x1d,0x41],"a̋":[0x61,0x1d,0x61],"Ő":[0x4f,0x1d,0x4f],"ő":[0x6f,0x1d,0x6f],"Ű":[0x55,0x1d,0x55],"ű":[0x75,0x1d,0x75],
    
    # ogonek
    "Ą":[0x41,0x1e,0x41],"ą":[0x61,0x1e,0x61],"Ę":[0x45,0x1e,0x45],"ę":[0x65,0x1e,0x65],"Į":[0x49,0x1e,0x49],"į":[0x69,0x1e,0x69],"Ų":[0x55,0x1e,0x55],"ų":[0x75,0x1e,0x75],
    
    # caron/háček
    "Č":[0x43,0x1f,0x43],"č":[0x63,0x1f,0x63],"Ď":[0x44,0x1f,0x44],"ď":[0x64,0x1f,0x64],"Ě":[0x45,0x1f,0x45],"ě":[0x65,0x1f,0x65],"Ľ":[0x4c,0x1f,0x4c],"ľ":[0x6c,0x1f,0x6c],"Ň":[0x4e,0x1f,0x4e],"ň":[0x6e,0x1f,0x6e],"Ř":[0x52,0x1f,0x52],"ř":[0x72,0x1f,0x72],"Š":[0x53,0x1f,0x53],"š":[0x73,0x1f,0x73],"Ť":[0x54,0x1f,0x54],"ť":[0x74,0x1f,0x74],"Ž":[0x5a,0x1f,0x5a],"ž":[0x7a,0x1f,0x7a],
    
    "¡":[0x21,0x0F,0x21],
    "¢":[0x63,0x0F,0x22],
    "¥":[0x59,0x0F,0x25],
    "§":[0x53,0x0F,0x27],
    "°":[0x7f,0x0F,0x30],
    "±":[0x7f,0x0F,0x31],
    "²":[0x7f,0x0F,0x32],
    "³":[0x7f,0x0F,0x33],
    "×":[0x7f,0x0F,0x34],
    "µ":[0x7f,0x0F,0x35],
    "¶":[0x7f,0x0F,0x36],
    "¿":[0x3F,0x0F,0x3F],
    "®":[0x7f,0x0F,0x52],
    "©":[0x7f,0x0F,0x53],
    "™":[0x7f,0x0F,0x54],
    "♪":[0x7f,0x0F,0x55],
    "€":[0x45,0x0F,0x56],
    "₠":[0x45,0x0F,0x56],
    "‰":[0x7f,0x0F,0x57],
    "Ω":[0x7f,0x0F,0x60],
    "Æ":[0x7f,0x0F,0x61],
    "æ":[0x7f,0x0F,0x71],
    "Đ":[0x44,0x0F,0x62],
    "Ø":[0x4f,0x0F,0x69],
    "ø":[0x6f,0x0F,0x79],
    "Œ":[0x7f,0x0F,0x6a],
    "œ":[0x7f,0x0F,0x7a],
    "ß":[0x73,0x0F,0x7b],
    
    #todo: more mappings
}

def charenhance(text,offset):
    # replace characters in text string for the level 1 page, and return a list of enhancement triplets
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
