# teletext-twitter
Reads your Twitter timeline and turns it into teletext pages for your Raspberry Pi

Right now this readme file makes the assumption that if you're interested in this, then:

1) You've already got your Raspberry Pi connected to a TV over composite
2) You've already got VBIT2 and Raspi-Teletext running and outputting teletext data to your TV

Assuming both of these things are true, then running this Python3 script should work. It will constantly update a spare page (153) in the main teletext folder (which defaults in VBIT2 to /home/pi/teletext/).

All of the files in that folder are sent across to the TV every so often, therefore the script constantly overwrites it with a new tweet (only one tweet right now!) so that it will update on your screen*

*maybe
