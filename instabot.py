from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

# Username and password of your instagram account:
my_username = 'insert username here'
my_password = 'insert password here'

# Instagram username list for DM:
usernames = [''] # read from an excel file could be nice

# Messages:
messages = ['Hello, this is a test! If you got this message, the code is fking working >:D']

# Delay time between messages in sec:
between_messages = 5

browser = webdriver.Chrome('chromedriver') #web brower scraper

# Authorization:
def auth(username, password):
	try:
		browser.get('https://instagram.com')
		time.sleep(random.randrange(2,4))

		input_username = browser.find_element_by_name('username')
		input_password = browser.find_element_by_name('password')

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)

# Sending messages:
def send_message(users, messages):
	try:
		browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click() # save login info button
		time.sleep(random.randrange(4,5))
		browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click() # notifications button
		time.sleep(random.randrange(4,5))
		browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click() # messenger button
		time.sleep(random.randrange(4,5))
		browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div').click() # send messages button
		for user in users:
			time.sleep(random.randrange(4,5))
			browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user) # username fillout space 
			time.sleep(random.randrange(2,3))
			browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]').click() # user button
			time.sleep(random.randrange(2,3))
			browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click() # next button
			time.sleep(random.randrange(3,4))
			text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
			text_area.send_keys(random.choice(messages))
			time.sleep(random.randrange(2,4))
			text_area.send_keys(Keys.ENTER)
			print(f'Message successfully sent to {user}')
			time.sleep(between_messages)
			browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

	except Exception as err:
		print(err)


auth(my_username, my_password)
time.sleep(random.randrange(2,4))
send_message(usernames, messages)
