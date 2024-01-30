from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        
    searchBox = (By.ID, "twotabsearchtextbox") 
    btnSearch = (By.ID, "nav-search-submit-button")  
    
    
    def searchBoxMethod(self):
        return self.driver.find_element(*HomePage.searchBox)
    
    def btnSearchMethod(self):
        return self.driver.find_element(*HomePage.btnSearch)
    
