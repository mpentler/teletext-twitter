# teletext-twitter
Reads your Twitter timeline and turns it into teletext pages for your Raspberry Pi

![Screenshot](https://i.imgur.com/xwnfUw3.jpg "Screenshot of output")

## Installation
Right now this readme file makes the assumption that if you're interested in this, then:

1) You've already got your Raspberry Pi connected to a TV over composite using a cable with the correct pin-out. I bought mine from The Pi Hut: https://thepihut.com/products/adafruit-a-v-and-rca-composite-video-audio-cable-for-raspberry-pi
2) You've already got VBIT2 and Raspi-Teletext running and outputting teletext data to your TV

You can find both of the required projects at these links:
raspi-teletext: https://github.com/ali1234/raspi-teletext - Only PAL is supported by raspi-teletext
VBIT2: https://github.com/peterkvt80/vbit2

After getting these up and running the last thing to do is to rename config.py-default to config.py and get your Twitter access tokens to store in the file. You can find a good guide for doing this here: https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/

You will need to pick a unique name for the app. Which is annoying. Pick anything you want that isn't taken. Maybe add your name at the end.

When you've setup your config.py you can change to the teletext-twitter directory and run the script with:

`python3 teletext-twitter.py` (add -h to show options)

It will constantly update a spare page (153 - chosen because it used to be used for this purpose on Teefax in the past) in the main teletext folder (which defaults in VBIT2 to /home/pi/teletext/).

All of the files in that folder are sent across to the TV every so often, therefore the script constantly overwrites it with new tweets (up to 5 - space permitting!) so that it will update on your screen.

## Notes
* At this moment in time the script reads 5 tweets. Further versions will improve on this by writing multiple tweets, possibly in subpages :-O
* New tweets are grabbed every 60 seconds by default. This is configurable with the -d option, but you do have be aware of the Twitter API limits.
* Right now this script doesn't do much to strip or replace characters that the teletext specification doesn't support. Emojis in particular may destroy the layout. I'll work on it...
* Character substitutions that *are* handled are things like replacing underscores with hyphens and also making sure # works correctly. You also have to replace curly apostrophes with straight ones, as that's all the specification allows

Apart from those notes, things should work ok. Have fun, turn back the clock, and if you genuinely use this for anything please let me know (also you're mental/cool).
