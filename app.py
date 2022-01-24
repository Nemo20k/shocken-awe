from flask import Flask, render_template
from crawler import take_html
import sys
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/url/<url>')
def get_url(url: str):
    path = take_html(url='https://www.haaretz.co.il/opinions/.premium-1.10558984', user_agent=r'msnbot/1.0 (+http://search.msn.com/msnbot.htm)', save_path='templates/page.html')
    return render_template('page.html')