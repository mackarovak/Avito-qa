from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

# Initialize the driver
driver = webdriver.Chrome()
url = "https://www.avito.ru/favorites"
def test_favorites_page_title():
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.title_is("Объявления | Избранное | Авито")
    )
    title = driver.title
    expected_title = "Объявления | Избранное | Авито"
    try:
        assert title == expected_title
    except AssertionError:
        print("Заголовок страницы не совпадает с ожидаемым значением")

def test_add_item_to_favorites(item_url):
    driver.get(item_url)

    # Find the "Add to favorites" button and click it
    add_to_favorites_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span'))
    )
    add_to_favorites_button.click()

    # Go to the favorites page
    driver.get(url)

    # Check if the item is added to the favorites list
    favorites_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a/img'))
    )

    try:
        assert favorites_list.is_displayed()
    except AssertionError:
        print("Товар не добавлен в избранное")

def test_remove_item(url, xpath):
    driver.get(url)
    item_to_remove = driver.find_element(By.XPATH, xpath)
    remove_button = item_to_remove.find_element(By.XPATH, './div[1]/div')
    remove_button.click()
    try:
        driver.find_element(By.XPATH, xpath)
        assert True
    except NoSuchElementException:
        assert False, "Товар не удален из избранного"


def test_sorting():
    driver.get(url)
    price_checkbox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[1]/div/div/div[2]/div[1]')
    price_checkbox.click()
    print("Товары из избанного отсортированы по давности добавления")

# Add item to favorites
def test_add_to_favorites(item_url, xpath):
    driver.get(item_url)

    add_to_favorites_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    add_to_favorites_button.click()

    driver.get(url)

    favorites_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a/img'))
    )

    try:
        assert favorites_list.is_displayed()
    except AssertionError:
        print("Товар не добавлен в избранное")

try:
    test_favorites_page_title()
    xpath = '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div/div/div/div[2]'
# Run first test
    url1 = "https://www.avito.ru/kaliningrad/kollektsionirovanie/moneta_50let_3363777565"
    test_add_item_to_favorites(url1)

# Run second test
    url2 = "https://www.avito.ru/krasnodar/odezhda_obuv_aksessuary/krossovki_dolcegabbana_zhenskie_3209566854"
    test_add_item_to_favorites(url2)

# Run third test
    url3 = "https://www.avito.ru/norilsk/remont_i_stroitelstvo/linoleum_novyy_3251589313"
    test_add_item_to_favorites(url3)

    test_sorting()

# Remove items from favorites
    test_remove_item(url, xpath)
    test_remove_item(url, xpath)
    test_remove_item(url, xpath)

# Add new items to favorites
    poisk_url = "https://www.avito.ru/all/kollektsionirovanie?q=%D0%9C%D0%BE%D0%BD%D0%B5%D1%82%D0%B0+50%D0%BB%D0%B5%D1%82"
    test_add_to_favorites(poisk_url, '//*[@id="i3363777565"]/div/div/div[2]/div[1]/div')
    test_add_to_favorites('https://www.avito.ru/all/odezhda_obuv_aksessuary?q=%D0%9A%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8+Dolce%26Gabbana+%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B5', '//*[@id="i3182581196"]/div/div/div[2]/div[1]/div')
    time.sleep(10)
finally:
    driver.quit()