# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

tensor_site = 'https://tensor.ru/'
tensor_title = 'Тензор — IT-компания'

try:
    driver.get(sbis_site)
    time.sleep(1)
    print('Проверить адрес сайта и заголовок страницы (sbis.ru)')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Проверить наличие видимость кнопки Контакты')
    button_txt = 'Контакты'
    start_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item > a[href="/contacts"]')
    assert start_btn.text == button_txt

    print('Кликнуть на кнопку "Контакты"')
    assert start_btn.is_displayed(), 'Элемент не отображается'
    start_btn.click()
    time.sleep(3)

    print('Найти баннер "Тензор"')
    tensor_banner_title = 'tensor.ru'
    tensor_banner = driver.find_element(By.XPATH, '//div[@id="contacts_clients"]//a[@href="https://tensor.ru/"]')
    assert tensor_banner_title == tensor_banner.get_attribute('title')

    print('Кликнуть на баннер "Тензор"')
    assert tensor_banner.is_displayed(), 'Элемент не отображается'
    tensor_banner.click()
    time.sleep(2)

    print('Проверить адрес сайта и заголовок страницы (tensor.ru)')
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_site, 'Неверный адрес сайта'
    assert driver.title == tensor_title, 'Неверный заголовок сайта'

    print('Найти блок с новостью "Сила в людях" и линк')
    # Тут возможно перемудрил, но посчитал что нужно проверить именно что существует блок выше (Общий <div>)
    # А не просто существует дочерний <p> "Сила в людях"
    strength_block = driver.find_element(By.XPATH, '//p[. = "Сила в людях"]/parent::div')

    print('Найти линк "Подробнее" и кликнуть')
    about_link = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text > a[href="/about"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", about_link)  # Доскроллить до элемента
    about_link.click()
    time.sleep(2)

    print('Проверить адрес сайта и заголовок страницы (https://tensor.ru/about)')
    about_site = 'https://tensor.ru/about'
    about_title = 'О компании | Тензор — IT-компания'
    assert driver.current_url == about_site, 'Неверный адрес сайта'
    assert driver.title == about_title, 'Неверный заголовок сайта'

finally:
    driver.quit()
