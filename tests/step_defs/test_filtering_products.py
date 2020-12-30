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


@when(parsers.parse('the user choose price filter "{filter}"'))
def set_filter(context, selenium_driver, filter):
    category_site = Category.CategoryPage(selenium_driver)
    category_site.click_on_filter_element(filter)

    lowest_price = category_site.check_element_is_visible(By.XPATH, Category.price_from)
    highest_price = category_site.check_element_is_visible(By.XPATH, Category.price_to)

    #set scope of filter price
    set_price_od = category_site.drag_and_drop_element(lowest_price, 40, 0)
    set_price_do = category_site.drag_and_drop_element(highest_price, -100, 0)

    ceny = category_site.prices_from_filter()
    context["cena_od"] = float(ceny[0])
    context["cena_do"] = float(ceny[1])

    category_site.click_on_save_button()



@then('the user see less products when erlier')
def check_products(selenium_driver):
    time.sleep(3)
    prod_cat = Category.CategoryPage(selenium_driver)

    #information about returned products
    filtered_products = prod_cat.read_count_filtered_products()

    #check if next site exist
    arrow_is_displayed = prod_cat.next_site_exist()

    count_products = 0
    count_products += prod_cat.count_products_on_site()
    while arrow_is_displayed:
        #if next site exist user click on them
        prod_cat.click_next_site_arrow()

        count_products += prod_cat.count_products_on_site()

        #check if next site exixt
        arrow_is_displayed = prod_cat.next_site_exist()


    assert int(filtered_products) == count_products



@then('all price are bettwen choosen scope')
def check_display_list_of_products(selenium_driver, context):
    prod_cat = Category.CategoryPage(selenium_driver)
    ceny = prod_cat.all_prices_from_site()

    assert prod_cat.prices_are_in_scope(context["cena_od"], context["cena_do"], ceny), "Not all prices are in set scope"