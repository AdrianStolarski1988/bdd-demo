from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support import expected_conditions as ec

from Pages import Main, Search

scenarios('../features/searching_products.feature')


@given('the user go to main site')
def the_user_go_to_main_site(selenium_driver):
    site = Main.MainSite(selenium_driver)
    site.go_to(site.BASE_URL)


@when(parsers.parse('the user enter to search bar words "{product}" and see hint'))
def the_user_find_product(selenium_driver, product):
    driver = Main.MainSite(selenium_driver)
    driver.search_product_by_name(product)
    assert not driver.hint_is_displayed()


@when('the user click on search button')
def click_on_button(selenium_driver):
    driver = Main.MainSite(selenium_driver)
    driver.click_on_search_button()


@then(parsers.parse('the user is on search site with url "{url}"'))
def check_confirm_url(url):
    assert ec.url_contains(url)


@then(parsers.parse('the text in header of search is "{word}"'))
def check_word(selenium_driver, word):
    driver = Search.SearchPage(selenium_driver)
    assert word in driver.search_word_is_displayed_in_search_header()


@then('the user see list of products after click on search button')
def check_display_list_of_products(selenium_driver):
    driver = Search.SearchPage(selenium_driver)
    assert driver.list_of_products() > 0
