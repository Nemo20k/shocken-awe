import argparse
import time
from selenium_crawler import take_screenshot, take_pdf
from requests_crawler import take_html

USER_AGENT = r'msnbot/1.0 (+http://search.msn.com/msnbot.htm)'

parser = argparse.ArgumentParser('shocken-awe')
parser.add_argument('-url', type=str, dest='url')
parser.add_argument('-s', type=str, dest='save_path', default='screenshot.png')
parser.add_argument('-img', action='store_true', dest='screenshot', help='take full page screenshot')
parser.add_argument('-html', action='store_true', dest='html', help='save html version local')

if __name__ == '__main__':
    args = parser.parse_args()
    if args.screenshot and not args.html:
        take_screenshot(url=args.url, user_agent=USER_AGENT, save_path=args.save_path)
    elif args.html:
        take_html(url=args.url, user_agent=USER_AGENT, save_path=args.save_path)
    else:
        print(args.help)