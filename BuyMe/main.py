import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:\\tools\\chromedriver.exe')
driver.get("https://buyme.co.il")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_partial_link_text('הרשמה').click()
driver.implicitly_wait(10)

# registration
# driver.find_element_by_xpath("//span[@class='text-btn']").click()
# driver.find_element_by_id('ember1019').send_keys('yarin')
# driver.find_element_by_id('ember1021').send_keys('ac@ac.ac')
# driver.find_element_by_id('valPass').send_keys('Password1')
# driver.find_element_by_id('ember1025').send_keys('Password1')
# driver.find_element_by_xpath("//input[@id='ember1026-id']").click()
# driver.find_element_by_xpath("//button[@class='ui-btn orange large']").click()

# direct login
driver.find_element_by_id('ember1005').send_keys('ac@ac.ac')
driver.find_element_by_id('ember1007').send_keys('Password1')
driver.find_element_by_xpath("//button[@class='ui-btn orange large']").click()

# choose price point
time.sleep(1)
driver.find_elements_by_class_name('chosen-single')[0].click()
time.sleep(1)
driver.find_elements_by_class_name("active-result")[2].click()

# choose region
time.sleep(1)
driver.find_elements_by_class_name('chosen-single')[1].click()
time.sleep(1)
driver.find_elements_by_class_name("active-result")[5].click()

# choose category
time.sleep(1)
driver.find_elements_by_class_name('chosen-single')[2].click()
time.sleep(1)
driver.find_elements_by_class_name("active-result")[7].click()

# search
driver.find_element_by_id('ember723').click()
time.sleep(1)

# choose gift card
driver.find_elements_by_class_name('card-item')[2].click()
driver.find_elements_by_class_name('step-1-item')[1].click()
time.sleep(1)

# tried to enter amount, however without success. this is the code.
# amount = driver.find_element_by_class_name('money')
# amount.sleep(0.5)
# amount.click()
# time.sleep(0.5)
# amount.send_keys("666")

# sender and receiver info
source = driver.find_elements_by_class_name('ui-input')[0]
source.send_keys('אשתי היקרה')
source = driver.find_elements_by_class_name('ui-input')[1]
source.send_keys('Dez')
source = driver.find_element_by_tag_name('textarea')
source.send_keys('ברכה גנרית')

# upload pic
pic = driver.find_element_by_id('ember1364')
pic.send_keys('C:\8.jpg')

# pick email
chooseemail = driver.find_element_by_class_name('icon-envelope')
chooseemail.click()
# enter email
entermail = driver.find_element_by_id('ember1797')
entermail.send_keys('aladdin@disney.com')
entermail.send_keys(Keys.ENTER)

# pick mobile
choosemob = driver.find_element_by_class_name('mobile-send-method')
choosemob.click()
# enter mobile
entermob = driver.find_element_by_id('ember1805')
entermob.send_keys('0522600199')
time.sleep(0.5)
entermob = driver.find_element_by_id('resendReciver')
entermob.send_keys('0522600199')
entermob.send_keys(Keys.ENTER)

driver.find_element_by_xpath("//div[@class='submit-wrapper']/button[@class='btn btn-theme']").click()
# asljlkjsadl