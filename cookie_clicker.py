from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
upgrades = driver.find_elements_by_css_selector("#store div")
upgrade_ids = [upgrade.get_attribute("id") for upgrade in upgrades]



timeout = time.time() + 5
minute = time.time() + 60

while True:
    cookie.click()
    if time.time() > timeout:
        prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []
        for price in prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        upgrade_dict = {}
        for n in range(len(item_prices)):
            upgrade_dict[item_prices[n]] = upgrade_ids[n]

        money = driver.find_element_by_xpath('//*[@id="money"]').text
        possible_upgrades = {}
        for cost, id in upgrade_dict.items():
            if int(money) > cost:
                possible_upgrades[cost] = id

        best_upgrade = max(possible_upgrades)

        driver.find_element_by_id(possible_upgrades[best_upgrade]).click()
        timeout = time.time() + 5
    
    if time.time() > minute:
        cps = driver.find_element_by_xpath('//*[@id="cps"]').text
        print(cps)
        break

driver.quit()