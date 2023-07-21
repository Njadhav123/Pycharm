from selenium import webdriver
driver = webdriver.Chrome("../Drivers/chromedriver.exe")
driver.get("https://google.com")
driver.quit()
print("neha")