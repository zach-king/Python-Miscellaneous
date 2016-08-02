from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

driver = webdriver.Firefox()
driver.get('http://www.python.org')
assert 'Python' in driver.title
elem = driver.find_element_by_name('q')
elem.clear()

query = ''

if len(sys.argv) != 1:
    query = sys.argv[1]
else:
    query = input('Search: ')

elem.send_keys(query)
elem.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
driver.close()