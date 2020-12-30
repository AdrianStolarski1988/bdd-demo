from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

price_filter = "//p[contains(text(),'Filter')]"
price_from = "//p[contains(text(),'Cena')]/../..//li//a[1]"
price_to = "//p[contains(text(),'Cena')]/../..//li//a[2]"
element_to_get_id_category = "//p[contains(text(),'Cena')]/../following-sibling::ul"
price_from_label = "//*[@id='facet_label_number']"
price_to_label = "//*[@id='facet_label_number']/span[2]"
save_btn = "//ul[@id='facet_number']/li/div[2]/button"
founded_products_label = '.products-selection__number'
product_box = "//div[@class='card card-product']"
next_site_arrow = "//*[@class='icon icon--arrow-right']"
price = "//span[@class='price' or @class='price price--with-discount']"

# //span[contains(@class, 'price') and not[@contains(@class,'regular-price')]
from Functions.Base import Base

class CategoryPage(Base):

    def drag_and_drop_element(self, element, x_offset, y_offset):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_offset, y_offset)
        action.perform()

    def get_id_filter_category(self):
        id_filter = self.driver.find_element(By.XPATH, element_to_get_id_category).get_attribute("id")
        return id_filter.split("_")[1]

    def click_on_filter_element(self, filter):
        price = self.driver.find_element(By.XPATH, price_filter.replace("Filter", filter))
        price.click()

    def prices_from_filter(self):
        price = self.driver.find_element(By.XPATH,
                                            price_from_label.replace("number", f'{self.get_id_filter_category()}')).text
        cena_od = price.split("\n")[0][:-2]
        cena_do = price.split("\n")[1][:-2]

        return cena_od, cena_do

    def click_on_save_button(self):
        btn = self.driver.find_element(By.XPATH, save_btn.replace("number", f'{self.get_id_filter_category()}'))
        btn.click()

    def read_count_filtered_products(self):
        count_text = self.driver.find_element(By.CSS_SELECTOR, founded_products_label).text
        print(count_text.split(" ")[0])
        return count_text.split(" ")[0]

    def count_products_on_site(self):
        amount_elements = len(self.driver.find_elements(By.XPATH, product_box))
        return amount_elements

    def next_site_exist(self):
        return self.if_element_exist(By.XPATH, next_site_arrow)

    def click_next_site_arrow(self):
        self.driver.find_element(By.XPATH, next_site_arrow).click()

    def product_price(self):
        cena = self.driver.find_element(By.XPATH, price).text
        cena = cena.split(" ")[0]
        cena = cena.replace(",", ".")
        return cena

    def all_prices_from_site(self):
        prices = self.driver.find_elements(By.XPATH, price)
        all_prices = []
        for ithem in enumerate(prices):
            cena = ithem[1].text
            now = cena.replace(",", ".").split(" ")[0]
            all_prices.append(now)
        return all_prices

    def prices_are_in_scope(self, min, max, data):
        errors = 0
        for item in data:
            if not float(min) <= float(item) <= float(max):
                print(item)
                errors += 1
        return True if errors == 0 else False
