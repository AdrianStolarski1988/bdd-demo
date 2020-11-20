from Functions.Base import Base


task_2 = "//*[contains(@href,'/task_2')]"
task_nb = "//a[contains(@href,'/task_*')]"



class Main(Base):

    def choose_task_nb(self, nb):
        task = task_nb.replace("*", str(nb))
        self.driver.find_element_by_xpath(task).click()

    def get_current_url(self):
        return self.driver.current_url


    def back(self):
        self.driver.back()


    def get_text_from_element(self, element):
        return self.driver.find_element_by_xpath(element).text