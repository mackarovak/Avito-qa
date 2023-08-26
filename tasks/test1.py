from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

def test_avito_favorites_page_title():

    # Открытие страницы
    driver.get("https://www.avito.ru/favorites")

    # Ожидание загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.title_is("Объявления | Избранное | Авито")
    )

    # Получение заголовка страницы
    title = driver.title

    # Сравнение заголовка с ожидаемым значением
    expected_title = "Объявления | Избранное | Авито"
    if title == expected_title:
        print("Заголовок страницы совпадает с ожидаемым значением")
    else:
        print("Заголовок страницы не совпадает с ожидаемым значением")


def test_add_item_to_favorites():

    # Открытие страницы с монетой
    driver.get("https://www.avito.ru/kaliningrad/kollektsionirovanie/moneta_50let_3363777565")

    # Нахождение кнопки "Добавить в избранное" и клик
    add_to_favorites_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span'))
    )
    add_to_favorites_button.click()

    # Переход на страницу избранного
    driver.get("https://www.avito.ru/favorites")

    # Проверка наличия добавленного элемента в списке избранного
    favorites_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a/img'))
    )

    # Завершение работы драйвера

def test_add_another_item_to_favorites():

    # Открытие страницы с телефоном
    driver.get("https://www.avito.ru/slavyansk-na-kubani/telefony/telefon_samsung_s21fe5g_3254210395")

    # Нахождение кнопки "Добавить в избранное" и клик
    add_to_favorites_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span'))
    )
    add_to_favorites_button.click()

    # Переход на страницу избранного
    driver.get("https://www.avito.ru/favorites")

    # Проверка наличия добавленного элемента в списке избранного
    favorites_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div/favorite-items-list/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a/img'))
    )



# Запуск теста
test_avito_favorites_page_title()
# Запуск первого теста
test_add_item_to_favorites()
# Запуск второго теста
test_add_another_item_to_favorites()
# Завершение работы драйвера
driver.quit()