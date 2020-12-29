from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

price_filter = "//p[contains(text(),'Filter')]"
price_from = "//p[contains(text(),'Cena')]/../..//li//a[1]"
price_to = "//p[contains(text(),'Cena')]/../..//li//a[2]"
element_to_get_id_category = "//p[contains(text(),'Cena')]/../following-sibling::ul"
price_from_label = "//*[@id='facet_label_number']"
price_to_label = "//*[@id='facet_label_number']/span[2]"

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
