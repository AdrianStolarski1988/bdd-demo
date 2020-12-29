import time

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from Pages import Main, Search, Category

scenarios('../features/filtering_products.feature')


@pytest.fixture(scope='function')
def context():
    return {}

@pytest.fixture(scope='function')
def driver(selenium_driver):
    browser = Main.MainSite(selenium_driver)
    return browser


@given('the user go to main site')
def the_user_go_to_main_site(driver):
    # driver = Main.MainSite(selenium_driver)
    driver.go_to(driver.BASE_URL)


@when(parsers.parse('the user overrun one of the main category'))
def the_user_choose_category(driver):
    # driver = Main.MainSite(selenium_driver)
    driver.hover_on_one_of_the_main_menu()
    driver.hint_is_displayed()

@when(parsers.parse('the user choose one of subcategories "{category_name}" and click on them'))
def click_on_subcategories(driver, category_name):
    # driver = Main.MainSite(selenium_driver)
    # driver.chose_subcategory(category_name)
    driver.find_element(By.XPATH, Main.menu_subcategory.replace("category", category_name)).click()


@then(parsers.parse('the user choose price filter "{filter}"'))
def set_filter(context, selenium_driver, filter):
    category_site = Category.CategoryPage(selenium_driver)
    category_site.click_on_filter_element(filter)

    lowest_price = category_site.check_element_is_visible(By.XPATH, Category.price_from)
    highest_price = category_site.check_element_is_visible(By.XPATH, Category.price_to)

    set_price_od = category_site.drag_and_drop_element(lowest_price, 40, 0)
    set_price_do = category_site.drag_and_drop_element(highest_price, -100, 0)

    ceny = category_site.prices_from_filter()
    context["cena_od"] = ceny[0]
    context["cena_do"] = ceny[1]



# @then(parsers.parse('the text in header of search is "{word}"'))
# def check_word(selenium_driver, word):
#     driver = Search.SearchPage(selenium_driver)
#     assert word in driver.search_word_is_displayed_in_search_header()
#
#
# @then('the user see list of products after click on search button')
# def check_display_list_of_products(selenium_driver, context):
#     driver = Search.SearchPage(selenium_driver)
#     amount2 = driver.list_of_products()
#     context['amount_from_list'] = str(amount2)
#     assert amount2 > 0
#
#
# @then('amount displayed product is equal with amount in hint')
# def compare_amount_of_products(context):
#     assert context['amount_from_hint'] == context['amount_from_list']
