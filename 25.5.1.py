from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.ChromiumEdge('./msedgedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


# 1. проверяем все ли питомцы отобразились в списке
def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('anna@pych.ru')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('violin3144')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # явное ожидание
    pytest.driver.get("https://petfriends.skillfactory.ru/all_pets")
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="navbar-toggler-icon"]')))

    pytest.driver.find_element(By.CSS_SELECTOR, 'span[class="navbar-toggler-icon"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

    # неявное ожидание
    pytest.driver.implicitly_wait(10)
    pytest.driver.get("https://petfriends.skillfactory.ru/my_pets")
    pytest.driver.find_element(By.XPATH, '//tr/td[1]')

    images = [i for i in pytest.driver.find_elements(By.XPATH, '//img[@style="max-width: 100px; max-height: '
                                                               '100px;"]')]
    names = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[1]')]
    types = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[2]')]
    ages = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[3]')]

    for i in range(len(names)):
        assert images[i] != ''
        assert names[i] != ''
        assert types[i] != ''
        assert ages[i] != ''


# 1. проверяем все ли питомцы отобразились в списке
def test_quantity_of_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('anna@pych.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('violin3144')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    pytest.driver.find_element(By.CSS_SELECTOR, 'span[class="navbar-toggler-icon"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

    names = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[1]')]
    stat = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')

    assert int(stat.text.split('\n')[1].split(' ')[-1]) == len(names)


# 2. хотя бы у половины питомцев есть фото
def test_images_of_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('anna@pych.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('violin3144')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    pytest.driver.find_element(By.CSS_SELECTOR, 'span[class="navbar-toggler-icon"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

    images = [i for i in pytest.driver.find_elements(By.XPATH, '//img[@style="max-width: 100px; max-height: 100px;"]')]
    names = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[1]')]
    types = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[2]')]
    ages = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[3]')]

    stat = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')
    mid = stat.text.split('\n')
    assert int(mid[1].split(' ')[-1]) / 2 < len(images)


# 3. у всех питомцев есть имя, возраст и порода
def test_all_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('anna@pych.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('violin3144')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    pytest.driver.find_element(By.CSS_SELECTOR, 'span[class="navbar-toggler-icon"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

    names = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[1]')]
    types = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[2]')]
    ages = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[3]')]
    stat = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')
    mid = stat.text.split('\n')

    assert len(names) == int(mid[1].split(' ')[-1])
    assert len(types) == len(names)
    assert len(ages) == len(types)


# 4. у всех питомцев разные имена
def test_various_names():
    pytest.driver.find_element(By.ID, 'email').send_keys('anna@pych.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('violin3144')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    pytest.driver.find_element(By.CSS_SELECTOR, 'span[class="navbar-toggler-icon"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

    names = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[1]')]
    assert len(set(names)) == len(names)


# 5. в списке нет повторяющихся питомцев
def test_various_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('anna@pych.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('violin3144')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    pytest.driver.find_element(By.CSS_SELECTOR, 'span[class="navbar-toggler-icon"]').click()
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

    names = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[1]')]
    types = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[2]')]
    ages = [i.text for i in pytest.driver.find_elements(By.XPATH, '//tr/td[3]')]

    l = []
    for i in range(len(names)):
        l.append("".join(names[i]) + "".join(types[i]) + "".join(ages[i]))

    assert len(l) == len(set(l))