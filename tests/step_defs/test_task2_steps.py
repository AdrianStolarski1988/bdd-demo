from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support import expected_conditions as ec

from Pages import Main, Task2

scenarios('../features/StronaGlowna.feature')



@given('the user go to main site')
def the_user_go_to_main_site(selenium_driver):
    site = Task2.Task2Page(selenium_driver)
    site.go_to("https://testingcup.pgs-soft.com/")


@when(parsers.parse('the user click on task number "{task}"'))
def the_user_click_on_task2(selenium_driver, task):
    driver = Main.Main(selenium_driver)
    driver.choose_task_nb(task)

@then('url is correct')
def correct_url():
    assert ec.url_contains('task_2')



@given('check if products are displayed')
def check_displayed_products(selenium_driver):
    driver = Task2.Task2Page(selenium_driver)
    amount = driver.count_amount_of_products()
    assert amount > 0, "any product isn't visible"


@when(parsers.parse('I choose category "{category}"'))
def choose_category(selenium_driver, category):
    driver = Task2.Task2Page(selenium_driver)
    driver.go_to(driver.BASE_URL + "task_2")
    driver.click_on_select_bar()
    driver.enter_category_to_search_bar(category)
    driver.press_enter_button()



@then(parsers.parse('I expect products in category in amount "{item}"'))
def display_category(selenium_driver, item):
    driver = Task2.Task2Page(selenium_driver)
    amount_visible_products= driver.count_amount_of_products()
    assert amount_visible_products is int(item), "error - not equal expected products with displayed"




