#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Echelon Ignite 2013 Thailand
# http://e27.co/ignite/
#
# Service Configuration Management for Rapid Growth Workshop Demo
#
__author__ = 'Takashi Someda <someda@nulab-inc.com>'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

import pytest

#browser = webdriver.Firefox() # Get local session of firefox
#browser.get("http://www.yahoo.com") # Load page
#assert "Yahoo!" in browser.title
#elem = browser.find_element_by_name("p") # Find the query box
#elem.send_keys("seleniumhq" + Keys.RETURN)
#time.sleep(0.2) # Let the page load, will be added to the API
#try:
#    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
#except NoSuchElementException:
#    assert 0, "can't find seleniumhq"
#browser.close()


@pytest.fixture(scope='module')
def driver(request):
    ret = webdriver.Firefox()

    def fin():
        ret.close()
    request.addfinalizer(fin)
    return ret


def test_todo1(driver):

    driver.get('http://localhost:5000/todo')

    assert 'Todo' in driver.title

    add_button = driver.find_element_by_xpath("//input[@value='add']")
    assert add_button is not None

    send_data = 'run integration test'

    todo_summary = driver.find_element_by_xpath("//input[@type='text' and @placeholder='todo']")
    todo_summary.send_keys(send_data)
    add_button.click()

    time.sleep(.5)
    assert todo_summary.text == ''

    added_summary = driver.find_element_by_xpath("//span[text()='%s']" % send_data)
    assert added_summary is not None
