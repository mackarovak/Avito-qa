from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.get("https://www.avito.ru/favorites")

title = driver.title

expected_title = "Объявления | Избранное | Авито"
if title == expected_title:
    print("Заголовок страницы совпадает с ожидаемым значением")
else:
    print("Заголовок страницы не совпадает с ожидаемым значением")

driver.get("https://www.avito.ru/kaliningrad/kollektsionirovanie/moneta_50let_3363777565")
add_to_favorites_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span'))
)

add_to_favorites_button.click()
driver.get("https://www.avito.ru/favorites")
favorites_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a/img'))
)

driver.get("https://www.avito.ru/krasnodar/odezhda_obuv_aksessuary/krossovki_dolcegabbana_zhenskie_3209566854")
add_to_favorites_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span'))
)

add_to_favorites_button.click()
driver.get("https://www.avito.ru/favorites")
favorites_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a/img'))
)

# driver.get("https://www.avito.ru/all/kollektsionirovanie?q=%D0%9C%D0%BE%D0%BD%D0%B5%D1%82%D0%B0+50%D0%BB%D0%B5%D1%82")
# add_to_favorites_button = WebDriverWait(driver, 10).until(
  #  EC.presence_of_element_located((By.XPATH, '//*[@id="i3363777565"]/div/div/div[2]/div[1]/div'))
# )
# add_to_favorites_button.click()


driver.get("https://www.avito.ru/favorites")
item_to_remove = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div/div/div/div[2]')
remove_button = item_to_remove.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div')
remove_button.click()

driver.get("https://www.avito.ru/kaliningrad/kollektsionirovanie/moneta_50let_3363777565")

driver.get("https://www.avito.ru/favorites")
time.sleep(2)
driver.quit()
