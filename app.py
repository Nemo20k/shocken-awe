import os
from flask import Flask, render_template, request
from crawler import take_html

UA = r'msnbot/1.0 (+http://search.msn.com/msnbot.htm)'
app = Flask(__name__)

@app.route('/status')
def index():
  return 'server is on'
  
@app.route('/', methods=['GET'])
def get_url():
    try:
        args = request.args
        url = args.get('url')
        if not url:
            return 'no url is given'
        article_name = os.path.split(url)[-1].replace('.html', '')
        full_path = take_html(url, user_agent=UA, save_path=f'templates/article.html')
        template_path = os.path.split(full_path)[-1]
        return render_template(template_path)
    except Exception as e:
        return (f'failed to get {url}, with exception:\n{e}')
    

if __name__ == "__main__":
  app.run()