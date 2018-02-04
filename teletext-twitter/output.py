# teletext-twitter - creates pages for vbit2 teletext system
# (c) Mark Pentler 2018 (https://github.com/mpentler)
# see README.md for details on getting it running or run with -h
# output module

import time
import textwrap
import re

# define our control codes here for easy use later
ESCAPE = chr(27)
DOUBLE_HEIGHT = ESCAPE + chr(77)
SET_BACKGROUND = ESCAPE + chr(93)
TWITTER_BIRD = chr(105) + chr(108) + chr(39)
text_colours = {"red" : 65, "green" : 66, "yellow" : 67 , "blue" : 68 , "magenta" : 69, "cyan" : 70, "white" : 71}
mosaic_colours = {"red" : 81, "green" : 82, "yellow" : 83, "blue" : 84, "magenta" : 85, "cyan" : 86, "white" : 87}

# character replacement and stripping function
def clean_line(line):
    emoji_pattern = re.compile("[" # our unicode ranges go here. this will need frequent tweaking
                              u"\U00002300-\U000023FF" # misc technical
                              u"\U000024C2-\U0001F251" # enclosed characters including flags
                              u"\U0001F300-\U0001F5FF" # symbols & pictographs
                              u"\U0001F600-\U0001F67F" # emoticons
                              u"\U0001F680-\U0001F9FF" # transport & map symbols
                               "]+", flags=re.UNICODE)
    line = emoji_pattern.sub(r'', line)

    line = line.replace("’", "'") # replacing some problematic characters here
    line = line.replace("_", "-") # the teletext English character set doesn't
    line = line.replace("#", "_") # support a lot of things!

    return line

def write_tweet_info(file, line_num, username, timestamp, config):
    string = "OL," + str(line_num) + ","
    string += "`" * (35-len(timestamp)-len(username))
    string += ESCAPE + chr(text_colours[config["username_colour"]]) +"@" + username
    string += ESCAPE + chr(text_colours["white"]) + "|"
    string += ESCAPE + chr(text_colours[config["timestamp_colour"]]) + timestamp
    string += "\r\n"
    file.write(string)

def write_tweet_line(file, line_num, line, config):
    string = "OL," + str(line_num) + ","
    string += ESCAPE + chr(text_colours[config["tweet_colour"]]) + line
    string += "\r\n"
    file.write(string)

def write_header(config): # write a header for the page and pop a nice banner at the top
    page_title = config["page_title"]
    logo_spacer = " " * (39 - (4 + len(page_title) + 5))
    with open(config["tti_path"] + "P153.tti", "w+") as file:
        file.write("DE,Autogenerated by Teletext-Twitter\r\n")
        file.write("PN,15300\r\n")
        file.write("SC,0000\r\n")
        file.write("PS,8000\r\n")
        file.write("OL,1," + ESCAPE + chr(text_colours[config["header_colour"]]) + SET_BACKGROUND +
                   DOUBLE_HEIGHT + ESCAPE + chr(text_colours["white"]) +
                   page_title + logo_spacer + ESCAPE + chr(mosaic_colours["cyan"]) + TWITTER_BIRD + "\r\n")
        file.write("OL,3," + ESCAPE + chr(mosaic_colours[config["header_separator"]]) + (chr(35) * 39) + "\r\n")

def write_timeline(twitter_object, config): # grab the latest timeline - only 5 tweets for now
    statuses = twitter_object.GetHomeTimeline(count = 5)
    line_position = 4

    for status in statuses: # iterate through our responses
        tweet_time = time.strptime(status.created_at,"%a %b %d %H:%M:%S +0000 %Y")
        tweet_human_time = time.strftime("%d-%b-%Y %H:%S", tweet_time) # reformat time/date output
        tweet_username = status.user.screen_name
        tweet_text = textwrap.wrap(status.text, 39) # make sure our lines fit on the screen

        if (line_position + len(tweet_text) + 1) > 24: # are we going to fill the page?
            break # yep! dump the last tweet!

        with open(config["tti_path"] + "P153.tti", "a") as file:
            write_tweet_info(file, line_position, tweet_username, tweet_human_time, config)
            line_position += 1
            for line in tweet_text:
                line = clean_line(line)
                write_tweet_line(file, line_position, line, config)
                line_position += 1

def write_search_term(twitter_object, search_term, config): # search recent tweets with a particular search term
    statuses = twitter_object.GetSearch(term=search_term, result_type="recent", count=5)
    line_position = 4

    for status in statuses: # iterate through our responses
        tweet_time = time.strptime(status.created_at,"%a %b %d %H:%M:%S +0000 %Y")
        tweet_human_time = time.strftime("%d-%b-%Y %H:%S", tweet_time) # reformat time/date output
        tweet_username = status.user.screen_name
        tweet_text = textwrap.wrap(status.text, 39) # make sure our lines fit on the screen

        if (line_position + len(tweet_text) + 1) > 24: # are we going to fill the page?
            break # yep! dump the last tweet!

        with open(config["tti_path"] + "P153.tti", "a") as file:
            write_tweet_info(file, line_position, tweet_username, tweet_human_time, config)
            line_position += 1
            for line in tweet_text:
                line = clean_line(line)
                write_tweet_line(file, line_position, line, config)
                line_position += 1
