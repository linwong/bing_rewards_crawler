#!/usr/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import getopt
import os
import random
import time
import re

# Defaults
profile_location = '~/bing_firefox'
search_terms = 'search_terms.txt'
login_list = 'logins.txt'
num_of_searches = 65
num_of_mobile_searches = 25

# Get options
#  -p --profile - use profile location
#  -b - only opens browser, no searches (useful for opening specific profile)
#  -l --logins - use logins in logins.txt file
#  -h --help  
try:
  options, args = getopt.getopt(sys.argv[1:], "p:hbl", ["profile=", "help", "browser", "logins"])
except getopt.GetoptError:
  print 'Usage: bing_rewards_crawler.py [-p path_to_profile] [-b] [-l]'
  exit(2)

open_browser = False
use_login_file = False
for opt, arg in options:
  if opt in ('-p', '--profile'):
    profile_location = arg
  if opt in ('-b', '--browser'):
    open_browser = True
  if opt in ('-l', '--logins'):
    use_login_file = True
  if opt in ('-h', '--help'):
    print 'Usage: bing_rewards_crawler.py [-p path_to_profile] [-b] [-l]'
    exit()

script_directory  = os.path.abspath(os.path.dirname(__file__))
profile_directory = os.path.expanduser(profile_location)

# open logins file and insert them into a list
logins = []
if use_login_file:
  with open(script_directory + '/' + login_list) as f:
    while 1:
      line = f.readline()
      if not line:
        break
      line = line.strip("\n")
      if re.match('^#', line) is not None:
        continue
      logins.append(line)
  f.close();

# open search file and insert them into a list
with open(script_directory + '/' + search_terms) as f:
  searches = [x.strip("\n") for x in f.readlines()]
f.close()
random.shuffle(searches)


# Desktop search
url = 'http://bing.com'
ffprofile = webdriver.FirefoxProfile(profile_directory)
driver    = webdriver.Firefox(ffprofile)
driver.get(url)

# this only opens the browser and does no searches
if open_browser:
  exit()

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
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME,'q')))
  finally:
    time.sleep(2)
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
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME,'q')))
  finally:
    time.sleep(2)
    i += 1
    print 'mobile search ' + `i` + ' ' + search
  if i > num_of_mobile_searches:
    break
driver.quit()
