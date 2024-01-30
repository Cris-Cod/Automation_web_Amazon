from utilities.BaseClass import BaseClass
from page_object_model.home_page import HomePage
from page_object_model.products import Products
import pytest

class TestCase(BaseClass):

    def test_search_prodcut(self):
        homePage = HomePage(self.driver)
        products = Products(self.driver)
        self.implicitly_wait(10)
        homePage.searchBoxMethod().click()
        homePage.searchBoxMethod().send_keys("Tarjeta grafica")
        homePage.btnSearchMethod().click()
        items = products.listProductsMethod()
        #print("productos--",items)
        
        for item in items:
            if item == items[1]:
                text = products.listNamesProductsMethod(item).text
                if text == 'Radeon RX 580 - Tarjeta gráfica de 8 GB, tarjeta de video AMD 256 bits 2048SP GDDR5 para juegos de PC, salida DP HDMI DVI, PCI Express 3.0 con ventilador dual para oficina y juegos':
                    products.productsMethod(item).click()