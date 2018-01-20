# teletext-twitter
Reads your Twitter timeline and turns it into teletext pages for your Raspberry Pi

## Installation
Right now this readme file makes the assumption that if you're interested in this, then:

1) You've already got your Raspberry Pi connected to a TV over composite
2) You've already got VBIT2 and Raspi-Teletext running and outputting teletext data to your TV

Assuming both of these things are true, then the last thing to do is to rename config.py-default to config.py and get your Twitter access tokens to store in the file. You can find a good guide for doing this here: https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/

When you've setup your config.py you can change to the teletext-twitter directory and run the script with:

`python3 teletext-twitter`

It will constantly update a spare page (153 - chosen because it used to be used for this purpose on Teefax in the past) in the main teletext folder (which defaults in VBIT2 to /home/pi/teletext/).

All of the files in that folder are sent across to the TV every so often, therefore the script constantly overwrites it with a new tweet (only one tweet right now! See the notes section below) so that it will update on your screen*

## Notes
* At this moment in time the script reads a single tweet. Further versions will improve on this by writing multiple tweets to the screen. Maybe even subpages :-O
* A tweet is grabbed every 30 seconds right now. I may make this user-configurable in the future, but you do have be aware of the Twitter API limits.
