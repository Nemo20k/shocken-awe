import argparse
import time
from selenium_crawler import take_screenshot, take_pdf

USER_AGENT = r'msnbot/1.0 (+http://search.msn.com/msnbot.htm)'


parser = argparse.ArgumentParser('shocken-awe')
parser.add_argument('-url', type=str, dest='url')
parser.add_argument('-s', type=str, dest='save_path', default='screenshot.png')

if __name__ == '__main__':
    args = parser.parse_args()
    print(take_screenshot(url=args.url, user_agent=USER_AGENT, save_path=args.save_path))
    #take_pdf(url=args.url, user_agent=USER_AGENT, save_path=args.save_path)