## Changelog

### v0.7
- compressed three different tweet output functions into one! i guess this is slower to run but i like smaller, cleaner files...
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
