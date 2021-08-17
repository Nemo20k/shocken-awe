# shocken-awe

Scanner for Haaretz paywall. generate html file or full-page screenshot for given url

## DISCLAIMER
This code was created and published for educational and academic use only. The full rights of any website content belongs to the website owners. anyone who use this program is self-responsible for it use.


##  Clone

```
git clone https://github.com/Nemo20k/shocken-awe.git
```


## Dependencies

```
pip3 install selenium
```

chromedriver for mac is included. currently, for other platform you can download fitting driver
from the [chromedriver download page](https://chromedriver.chromium.org/downloads)

## useage 
```
cd ./shocken-awe

# take screenshot
python3 main.py -img -url SOME-HAARETZ-URL.COM -s SAVE-PATH

# save html file (recomended)
python3 main.py -html -url SOME-HAARETZ-URL.COM -s SAVE-PATH
```

* html is the faster and lighter option, but may not save pictures.
