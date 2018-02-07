# teletext-twitter - creates pages for vbit2 teletext system
# (c) Mark Pentler 2018 (https://github.com/mpentler)
# see README.md for details on getting it running or run with -h
# main script

from output import *
import twitter
import time
import sys
import argparse

# Read config.py for our Twitter access keys etc
config = {}
exec(open("config.py").read(), config)
twitter_object = twitter.Api(access_token_key = config["access_key"],
                      access_token_secret = config["access_secret"],
                      consumer_key = config["consumer_key"],
                      consumer_secret = config["consumer_secret"],
                      sleep_on_rate_limit = True) # so we don't hit the rate limit and raise an exception

def parse_args():
    parser = argparse.ArgumentParser(description="Reads your Twitter timeline and turns it into teletext pages for your Raspberry Pi.")

    parser.add_argument("-m", "--mode", type=str, help="choose between different modes - home, user or search")
    parser.add_argument("-q", "--query", type=str, help="a search query, either a search term or a username. hashtags supported if you put quotes around the string")
    parser.add_argument("-d", "--delay", type=int, default=60, help="seconds between timeline scrapes (minimum is 60 seconds - lower values have no effect)")
    parser.add_argument("-v", "--version", action="version", version="0.6")
    parser.add_argument("-Q", "--quiet", action="store_true", default=False, help="suppresses all output to the terminal except warnings and errors")

    args = parser.parse_args()
    args.delay = max(60, args.delay)

    if args.mode == "search" and not args.query:
        print("[!] Search mode selected but no query specfied with -q. Exiting...", file=sys.stderr)
        sys.exit(1)

    if args.mode == "user" and not args.query:
        print("[!] User timeline mode selected but no username specified. Exiting...", file=sys.stderr)
        sys.exit(1)

    return args

def main():
    args = parse_args()

    if not args.quiet:
        print("[*] teletext-twitter - (c) 2018 Mark Pentler (https://github.com/mpentler)", file=sys.stdout)

    while True:
        try:
            write_header(config)
            if args.mode == "home":
                if not args.quiet:
                    print("[*] Beginning home timeline scraping", file=sys.stdout)
                write_home_timeline(twitter_object, config)
            elif args.mode == "search":
                if not args.quiet:
                    print("[*] Getting recent tweets containing: " + args.query, file=sys.stdout)
                write_search_term(twitter_object, args.query, config)
            elif args.mode == "user":
                if not args.quiet:
                    print("[*] Getting all tweets from user: @{}".format(args.query), file=sys.stdout)
                write_user_timeline(twitter_object, args.query, config)
            if not args.quiet:
                print("[*] Page updated. Waiting {} seconds until next scrape".format(args.delay), file=sys.stdout)
        except OSError as e:
            print("[!] Error accessing teletext data file, exiting: {}".format(e.strerror), file=sys.stderr)
            sys.exit(1)
        except twitter.error.TwitterError as e:
            for error in e.message:
                if error['code'] == 32:
                    print("[!] Authentication error accessing Twitter. Check config.py file and make sure your tokens are correct.", file=sys.stderr)
                    print("[!] Exiting...", file=sys.stderr)
                    sys.exit(1)
                print("[!] Error accessing your Twitter timeline: {}".format(error['message']), file=sys.stderr)
                print("[!] Trying again after specified delay", file=sys.stderr)
        time.sleep(args.delay)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("[*] Interrupted by user. Exiting...", file=sys.stdout)
        sys.exit(0)
