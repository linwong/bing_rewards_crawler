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

# Defaults
profile_location = '~/bing_firefox'
search_terms = 'search_terms.txt'

# Get options
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

script_directory  = os.path.abspath(os.path.dirname(__file__))
profile_directory = os.path.expanduser(profile_location)
num_of_searches = 35
num_of_mobile_searches = 25

with open(script_directory + '/' + search_terms) as f:
  searches = [x.strip("\n") for x in f.readlines()]
f.close()
print searches
random.shuffle(searches)

# Desktop search
url = 'http://bing.com'
ffprofile = webdriver.FirefoxProfile(profile_directory)
driver    = webdriver.Firefox(ffprofile)
driver.get(url)

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
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,'q')))
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
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,'q')))
  finally:
    i += 1
    print 'mobile search ' + `i` + ' ' + search
  if i > num_of_mobile_searches:
    break
driver.quit()
