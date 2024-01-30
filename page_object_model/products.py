from selenium.webdriver.common.by import By

class Products:
    def __init__(self, driver):
        self.driver = driver
        
    listProducts = (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")    
    listNamesProducts = (By.CSS_SELECTOR, "div[data-cy='title-recipe']")
    
    def listProductsMethod(self):
        return self.driver.find_elements(*Products.listProducts)   
    
    def listNamesProductsMethod(self, item):
        return self.driver.find_element(*Products.listNamesProducts)    
    
    def productsMethod(self, item):
        return self.driver.find_element(*Products.listProducts)   