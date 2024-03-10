
import os
import sys
import time
os.popen("docker run -it -p 9090:9090 opensecurity/nodejsscan:latest")
link = sys.argv[1]
pathSave = "Page.html" if not sys.argv[2] else sys.argv[2]
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
op = webdriver.FirefoxOptions() #Для Google Chrome прописывать webdriver.Chrome()
op.add_argument('--headless')
browser = webdriver.Firefox(options=op) #Для Google Chrome прописывать webdriver.Chrome()
url = "http://127.0.0.1:9090"
time.sleep(2)
browser.get(url)
button = browser.find_element(By.CLASS_NAME,"clone")
element = browser.find_element(By.CLASS_NAME,"repourl")
element.send_keys(link + Keys.RETURN)
button.click()
time.sleep(2)
while True:
    if browser.current_url != url:
        break
with open(pathSave, 'w',encoding="utf-8") as f:
    f.write(browser.page_source)
browser.quit()
