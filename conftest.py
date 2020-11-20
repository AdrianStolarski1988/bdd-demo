import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



browser = None


def browser_config(browser_options):
    browser_options.add_argument('--headless')
    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('--disable-dev-shm-usage')
    return browser_options


@pytest.fixture(autouse=True, scope="session")
def selenium_driver(request):
    global browser

    # if request.param == "chrome":
    browser_options = ChromeOptions()
    browser_config(browser_options)
    browser = webdriver.Chrome(options=browser_options)

# if request.param == "firefox":
#     browser_options = FirefoxOptions()
#     browser_config(browser_options)
#     browser = webdriver.Firefox(options=browser_options)



    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    browser.implicitly_wait(10)

    yield browser
    browser.quit()
    # return browser


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    timestamp = str(int(time.time()))

    if report.when == 'call' and report.failed:

    # # TODO do zrobienia dodawanie screenow do raportow

        #dodawanie url do raportow - lista screenow?
        # extra.append(pytest_html.extras.url('http://www.example.com/')
        screenshot_name = "screenshots/"+timestamp + ".png" #tests/screenshots/"
        print(screenshot_name)
        browser.save_screenshot(screenshot_name)
        print("OK")
        extra.append(pytest_html.extras.image(screenshot_name))
    report.extra = extra
