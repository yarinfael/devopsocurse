# ﻿from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# 1A
# driver = webdriver.Chrome(executable_path='C:\\tools\\chromedriver.exe')
# driver.get("http://www.walla.co.il")
# 1B
# driver = webdriver.Chrome(executable_path='C:\\tools\\geckodriver.exe')
# driver.get("http://www.ynet.co.il")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2A
# website_title = driver.title
# 2B
# driver.refresh()
# 2C
# if website_title==driver.title:
#   print('same titles')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 3
# yes
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 4
# driver.get('https://translate.google.com')
# driver.maximize_window()
# source = driver.find_element_by_id('source')
# source.click()
# source.send_keys('משהו בעברית')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 5
# driver.get("https://www.youtube.com/")
# driver.find_element_by_id("search").send_keys("help!")
# driver.find_element_by_id("search-icon-legacy").click()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 6
# there is no translate button
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 7
# driver.get("https://www.facebook.com/")
# driver.implicitly_wait(10)
# driver.find_element_by_id("email").send_keys("<Email>")
# driver.find_element_by_id("pass").send_keys("<Pass>")