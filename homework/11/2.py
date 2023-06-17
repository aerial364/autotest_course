# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
auth_link = 'https://fix-online.sbis.ru/auth/'
contacts_link = 'https://fix-online.sbis.ru/page/dialogs'
login = 'YOUR_LOGIN_HERE'
password = 'YOUR_PASSWORD_HERE'
action = ActionChains(driver)

try:
    # Логинимся
    driver.get(auth_link)
    time.sleep(1)
    login_input = driver.find_element(By.CSS_SELECTOR, '[name = "Login"]')
    login_input.send_keys(login)
    next_btn = driver.find_element(By.XPATH, '//span[@tabindex="2"]')
    next_btn.click()
    password_input = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password_input.send_keys(password)
    finish_btn = driver.find_element(By.XPATH, '//span[@tabindex="4"]')
    finish_btn.click()
    time.sleep(2)
    # Переходим в Контакты
    driver.get(contacts_link)
    time.sleep(2)
    # Открываем селектор по кнопке "+"
    plus_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    plus_btn.click()
    time.sleep(2)
    # Выбираем себя в селекторе
    search_input = driver.find_element(By.XPATH, '//*[@id="popup"]//input')
    search_input.click()
    search_input.send_keys('Афанасьев Никита Алексеевич')
    assert search_input.get_attribute('value') == 'Афанасьев Никита Алексеевич'
    time.sleep(2)
    person_card = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    assert person_card.get_attribute('title') == 'Афанасьев Никита'
    person_card.click()
    time.sleep(2)
    # Пишем сообщение
    text_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    text_field.send_keys('Привет, это автотест!')
    # Отправляем сообщение
    send_btn = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    send_btn.click()
    time.sleep(2)
    # Проверяем наличие уведомления в реестре
    message = driver.find_element(By.XPATH, '//div[@data-qa="item"]//p[. = "Привет, это автотест!"]')
    # Удаляем сообщение
    action.context_click(message).perform()  # right click
    time.sleep(2)
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
    delete_btn.click()
    time.sleep(5)
    # Проверяем удаление сообщение из реестра
    try:
        message_after_delete = driver.find_element(By.XPATH, '//div[@data-qa="item"]//p[. = "Привет, это автотест!"]')
    except selenium.common.exceptions.NoSuchElementException:
        print("Сообщение успешно удалено")
    else:
        raise Exception('Сообщение не было удалено!')


finally:
    driver.quit()
