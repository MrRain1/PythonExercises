from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://automatetheboringstuff.com")

# by argument expects: `css selector`, `link text`, `partial link text`, `tag name`, `xpath`
elem = driver.find_element(by= "css selector", value= ".main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(2) > a:nth-child(1)")
elem.click()

driver.get("https://www.amazon.it/")
search_bar = driver.find_element(by="css selector", value="#twotabsearchtextbox")
search_bar.send_keys("automate the boring stuff with python")
search_bar.submit()

driver.back()
driver.forward()
driver.refresh()

#driver.quit()