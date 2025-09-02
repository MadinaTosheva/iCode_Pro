import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

from HW_5.conftest import browser


def test_standard_user_login(browser):

    username = browser.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = browser.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    time.sleep(1)

    login_btn = browser.find_element(By.ID, "login-button").click()

    assert 'inventory' in browser.current_url


def test_locked_out_user_login(browser):

    username = browser.find_element(By.ID, "user-name")
    username.send_keys("locked_out_user")

    password = browser.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    time.sleep(1)

    login_btn = browser.find_element(By.ID, "login-button").click()

    time.sleep(1)

    error_message = browser.find_element(By.XPATH, "//div/h3").text
    assert error_message == 'Epic sadface: Sorry, this user has been locked out.'


def test_problem_user_login(browser):

    username = browser.find_element(By.ID, "user-name")
    username.send_keys("problem_user")

    password = browser.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    time.sleep(1)

    login_btn = browser.find_element(By.ID, "login-button").click()

    image_in_main_page = browser.find_element(By.XPATH, "//img[@src='/static/media/sl-404.168b1cce.jpg']")

    first_element = browser.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Backpack')]")
    first_element.click()
    image_in_first_element_page = browser.find_element(By.XPATH, "//img[@src ='/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg']")

    assert image_in_main_page != image_in_first_element_page   # сравниваю изображения первого элемента в главном экране,и после перехода на него


def test_wrong_credentials_login(browser):

    username = browser.find_element(By.ID, "user-name")
    username.send_keys("Madina")

    password = browser.find_element(By.ID, "password")
    password.send_keys("1234")

    time.sleep(1)

    login_btn = browser.find_element(By.ID, "login-button").click()

    time.sleep(1)


    error_message = browser.find_element(By.XPATH, "//div/h3").text
    assert error_message == 'Epic sadface: Username and password do not match any user in this service'


pytest.mark.slow()
def test_add_item_to_cart(browser):     # функционал добавления элемента на карзину
    test_standard_user_login(browser)   # вызвала готовую функцию логина

    add_to_card_btn = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_card_btn.click()

    time.sleep(3)

    shipping_cart_count = browser.find_element(By.CLASS_NAME, "shopping_cart_link").text

    assert shipping_cart_count == "1"



def test_validate_number_of_items_in_the_page(browser):  #валидируем количество вещей на странице
    test_standard_user_login(browser)


    all_items = browser.find_elements(By.CLASS_NAME, "inventory_item")

    number_of_items = 0

    for item in all_items:
      if item.is_displayed():
          number_of_items += 1

    assert number_of_items == 6


pytest.mark.slow()
def test_validate_each_item_has_img_price_button(browser):  #валидируем, что каждый айтем имеет картинку, цену и кнопку добавления
    test_standard_user_login(browser)


    all_items = browser.find_elements(By.CLASS_NAME, "inventory_item")

    img = browser.find_element(By.XPATH, "//div/a/img")
    price = browser.find_element(By.XPATH, "//div[@class = 'inventory_item_price']")
    add_button = browser.find_element(By.XPATH, "//button[contains(text(),'Add to cart' )]")

    time.sleep(3)

    for item in all_items:
      if item.is_displayed():

          assert img.is_displayed()
          assert price.is_displayed()
          assert add_button.is_displayed()









