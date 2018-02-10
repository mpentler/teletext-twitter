## Changelog

### v0.9
- tweet usernames now go through character substition like tweets do
- useless hypertext links are now filtered and replaced with a placeholder
- blank lines now written to fill page, no more fasttext links inserted by TVs on line 24 by default if you don't specify any

### v0.8
- major feature addition: subpage support to handle a larger number of tweets
- added cycle_time parameter to config, this is cycle time between subpages
- added count argument to specify number of tweets to download
- a few more bug fixes: line 24 now writable and no more dropped tweets (they go to subpages instead)
- moved a few bits of code around for logic and readability

### v0.7
- compressed three different tweet output functions into one!
- fixed still display bug in write_home_timeline function

### v0.6
- New mode added: show latest tweets from a certain user
- cmd line switches changed to accommodate user mode
- logo looks less like a dog
- bug fix: tweet cleaning now works in search mode
- bug fix: added curly quote->normal quote replacement
- default config file wasn't formatted right

### v0.5.3
- Page number now user-customisable

### v0.5.2
- Fixed stupid bug where I'd used %S instead of %M for the time display. now they're correct

### v0.5.1
- more restructuring
- you can now customise the page title text

### v0.5
- extensive code restructuring, including splitting things out into modules
- code made a lot more "functional" resulting in saving some lines (it's a start anyway)

### v0.4
- emoji stripping added!
- implemented theme support: pick your own colour scheme!
- changed config file layout to help future improvements
- changing the folder structure to aid a more modular design
- added tti_path variable to config.py

### v0.3
- search mode added!
- all terminal output now sent correctly to stdout and stderr
- checking cmd line args for errors such as missing arguments or incompatible switched
- added some files to improve github community score

### v0.2
- improved error handling
- script now exits on twitter authentication error
- documentation much improved due to increaed public interest
- added argparse code with some options including quiet mode
- error checking added

### v0.1
- added some control code constants for readability and some more code comments
- graphical banner added, lots of colour, and more than one tweet on a screen
- writes a single tweet to a .TTI file now for output
