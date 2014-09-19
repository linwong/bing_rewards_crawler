#!/usr/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import getopt
import os
import random
import time

# Default profile location
profile_location = '~/bing_firefox'

try:
  options, args = getopt.getopt(sys.argv[1:], "p:h", ["profile=", "help"])
except getopt.GetoptError:
  print 'Usage: bing_rewards_crawler.py [-p path_to_profile]'
  exit(2)

for opt, arg in options:
  if opt in ('-p', '--profile'):
    profile_location = arg
  if opt in ('-h', '--help'):
    print 'Usage: bing_rewards_crawler.py [-p path_to_profile]'
    exit()

# Stores the Firefox profile.  Change if you want to use different directory
profile_directory = os.path.expanduser(profile_location)
num_of_searches = 35
num_of_mobile_searches = 25

url = 'http://bing.com'
ffprofile = webdriver.FirefoxProfile(profile_directory)
driver    = webdriver.Firefox(ffprofile)
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
  'ryan tannehill',
  'michael redd',
  'sidney moncrief',
  'google chrome',
  'firefox',
  'world cup',
  'youtube',
  'yahoo',
  'flickr',
  'delicious',
  'feedly',
  'ars technica',
  'cnn',
  'engadget',
  'hacker news',
  'woot',
  'android',
  'lifehacker',
  'iphone',
  'apple',
  'nexus 9',
  'king of tokyo',
  'king of new york',
  'robinson crusoe',
  'the sum of all fears',
  'tom clancy',
  'clear and present danger',
  'halo 5',
  'borderlands',
  'ufc',
  'josh gordon',
  'mom',
  'mccain',
  'ebola',
  'heartstone',
  'monaco',
  'max payne',
  'hammerfight',
  'skyrim',
  'the elder scrolls',
  'ftl',
  'wasteland',
  'fallout',
  'castle crashers',
  'nikola tesla',
  'star wars',
  'star trek',
  'han solo',
  'luke skywalker',
  'boba fett',
  'jabba the hutt',
  'princess leia',
  'amidala',
  'lando',
  'captain kirk',
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
  if i > num_of_searches:
    break
driver.quit()


# Mobile Search
ffprofile = webdriver.FirefoxProfile(profile_directory)
ffprofile.set_preference('general.useragent.override', 'Mozilla/5.0 (Linux; Android 4.4.4; A0001 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile Safari/537.36')
driver    = webdriver.Firefox(ffprofile)
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
  if i > num_of_mobile_searches:
    break
driver.quit()
