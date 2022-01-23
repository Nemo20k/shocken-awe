import argparse
import time
from crawler import take_screenshot, take_html


USER_AGENT = r'msnbot/1.0 (+http://search.msn.com/msnbot.htm)'

parser = argparse.ArgumentParser('shocken-awe')
parser.add_argument('-url', type=str, dest='url', help="the url address of the page")
parser.add_argument('-s', type=str, dest='save_path', default='output')
parser.add_argument('-img', action='store_true', dest='screenshot', help='take full page screenshot')

parser.add_argument('-html', action='store_true', dest='html', help='save html version local')

if __name__ == '__main__':
    try:
        args: argparse.Namespace = parser.parse_args()
    
        saving_function = take_screenshot if args.screenshot else take_html
        save_path = saving_function(user_agent=USER_AGENT, **vars(args))
        print(f'page {args.url} saved succefuly at {save_path}')
    except Exception as e:
        print(f'failed to save page {args.url} with exception:\n{e}')


