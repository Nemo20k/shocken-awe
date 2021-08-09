# shocken-awe

Scanner for Haaretz paywall. generate full-page screenshot for given url


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

python3 main.py -url SOME-HAARETZ-URL.COM -s SAVE-PATH
```
it may take a minute for the selenium driver to work
