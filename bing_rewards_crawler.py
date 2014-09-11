#!/usr/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import random
import time

url = 'http://bing.com'
chromedriver = '/home/clw/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
chrome_options = Options()
chrome_options.add_argument("user-data-dir=/home/clw/bing_chrome/")
chrome_options.add_argument("enable-extensions")
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
driver.get(url)

searches = [
  'federer',
  'michael jordan',
  'nadal',
  'miami dolphins',
  'battlestar galactica',
  'destiny',
  'coca-cola',
  'felicia day',
  'mkbhd',
  'instagram',
  'facebook',
  'ferguson',
  'google',
  'the verge',
  'matthew berry',
  'espn',
  'milwaukee bucks',
  'wil wheaton',
  'xbox one',
  'surface pro',
  'nexus 5',
  'oneplus one',
  'selenium python',
  'humble bundle',
  'pinterest',
  'stack overflow',
  'sports illustrated',
  'emacs',
  'python',
  'bearded dragon',
  'rss reader',
  'gmail',
  'bill gates',
  'netflix',
  'reed hastings',
  'amazon',
  'the apprentice',
  'the resistance',
  'survivor',
  'the amazing race',
  'caris wong',
  'greenman gaming',
  'steam',
  'world of warcraft',
  'civilization beyond earth',
  'papers please',
  'prison architect',
  'steamworld dig',
  'theme hospital',
  'gog',
  'the fugitive',
  'cylon leader',
  'miami heat',
  'lebron james',
  'cinema sins',
  'free xbox gold live',
  'starbuck',
  'laura roslin',
  'president obama',
  'tom zarek',
  'lee apollo',
  'adama',
  'xbox one madden',
  'moto x',
  'tom brady',
  'peyton manning',
  'ryan tannehill'
]

random.shuffle(searches)

# Desktop search
i = 0
for search in searches:
  while True:
    try:
      input = driver.find_element_by_name('q')
      break
    except:
      print "couldn't find element"
      time.sleep(1)
  input.clear()
  input.send_keys(search)
  input.submit()
  try:
    WebDriverWait(driver, 10).until(EC.title_contains(search))
  finally:
    i += 1
    print 'search ' + `i` + ' ' + search
  if i > 30:
    break
driver.quit()


# Mobile Search
chrome_options = Options()
chrome_options.add_argument("user-data-dir=/home/clw/bing_chrome/")
chrome_options.add_argument("enable-extensions")
chrome_options.add_argument("use-mobile-user-agent")
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 4.4.4; A0001 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile Safari/537.36')
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
driver.get(url)

random.shuffle(searches)

i = 0
for search in searches:
  while True:
    try:
      input = driver.find_element_by_name('q')
      break
    except:
      print "couldn't find element"
      time.sleep(1)
  input.clear()
  input.send_keys(search)
  input.submit()
  try:
    WebDriverWait(driver, 10).until(EC.title_contains(search))
  finally:
    i += 1
    print 'mobile search ' + `i` + ' ' + search
  if i > 20:
    break
driver.quit()
