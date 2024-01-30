import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def selectByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 600)")

    def scroll1000(self):
        self.driver.execute_script("window.scrollBy(0, 1400)")
        
    def implicitly_wait(self, timeout):
        return self.driver.implicitly_wait(timeout)    

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def verifyElementPresence(self, element, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((element, text)))
