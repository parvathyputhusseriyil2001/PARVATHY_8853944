# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Navigating to the W3Schools.com homepage
driver.get("https://www.w3schools.com/")
time.sleep(3)
#
# # Finding the search bar and enter the text HTML
search_bar = driver.find_element("id","search2")
search_bar.send_keys("HTML")
time.sleep(3)
#
# # Submitting the search query
search_bar.send_keys(Keys.RETURN)
#
# Waiting for the search results page to load
time.sleep(3)
#
# Verifying that the search results page has loaded
assert "HTML Tutorial" in driver.title
print("HTML tutorial page is displayed")

# Selecting the HTML Tutorial  from the search results
Strt_butn = driver.find_element("xpath","//a[.='Study our free HTML Tutorial »']")
Strt_butn.is_displayed()
print("Study our free HTML tutorial button is displayed")

#click and verify Study our free HTML tutorial button
Strt_butn.click()
time.sleep(3)
assert "Introduction to HTML" in driver.title
print("Introduction to HTML page is loaded")



# verify next button is displayed
Next_button = driver.find_element("xpath","//div[@class='w3-clear nextprev']/a[.='Next ❯']")
Next_button.is_displayed()
print("Next button is displayed")
#
# # Waiting for the page to open
time.sleep(5)
#
# Verify  Try it Yourself button is displayed
Tryit_button=driver.find_element("xpath","//a[.='Try it Yourself »']")
Tryit_button.is_displayed()
print("Try it yourself button is displayed")


#Java option is displayed
java_option= driver.find_element("xpath","//a[@title='Java Tutorial']")
java_option.is_displayed()
print("Java option is displayed in the navigation bar")

#click on java option and verify the page loaded
java_option.click()
time.sleep(3)
assert "Java Tutorial"in driver.title
print("Java Tutorial page is loaded")

#verify login option
login_btn= driver.find_element("xpath","//a[.='Log in']")
login_btn.is_displayed()
print("Login option is displyed")

#click and verify the login button
login_btn.click()
time.sleep(3)
assert "Log in - W3Schools" in driver.title
print("Login page is displayed")
driver.back()

#verify Sign Up option
SignUp_btn= driver.find_element("id","signupbtn_topnav")
SignUp_btn.is_displayed()
print("Sign Up option is displyed")

#click and verify the Signup button
SignUp_btn.click()
time.sleep(3)
assert "W3Schools - Sign Up To Improve Your Learning Experience" in driver.title
print("Sign Up To Improve Your Learning Experience is displayed")

#click signup for free
signup_free= driver.find_element("xpath","//a[.='Sign Up For Free']")
signup_free.click()
time.sleep(3)
assert "Sign up - W3Schools" in driver.title
print("Sign up page is displayed")
driver.back()
driver.back()

time.sleep(4)
#close the webdriver
driver.close()
