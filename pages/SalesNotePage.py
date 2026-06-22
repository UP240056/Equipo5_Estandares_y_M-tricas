import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage

class SalesNotePage(BasePage):

    CUSTOMER_INPUT = (By.ID, "customer_id")
    PRODUCT_DROPDOWN = (By.ID, "product_select")
    QUANTITY_INPUT = (By.ID, "quantity_field")
    ADD_ITEM_BUTTON = (By.ID, "btn_add_item")
    SAVE_NOTE_BUTTON = (By.ID, "btn_save_sales_note")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")
    ERROR_ALERT = (By.CLASS_NAME, "alert-danger")

    def __init__(self, driver):
        super().__init__(driver)
        ruta_html = os.path.abspath(os.path.join(os.getcwd(), "sales_note", "index.html"))
        self.url = "http://localhost:8000/sales_note/"

    def navigate_to_module(self):
        self.driver.get(self.url)

    def fill_sales_note_form(self, customer, product, quantity):
        # 1. Escribe el cliente normal
        self.send_keys_to_element(self.CUSTOMER_INPUT, customer)
        
        # 2. Manejo correcto del dropdown con la clase Select
        dropdown_element = self.find_element(self.PRODUCT_DROPDOWN)
        dropdown = Select(dropdown_element)
        dropdown.select_by_value(product)
        
        # 3. Escribe la cantidad normal y da clic
        self.send_keys_to_element(self.QUANTITY_INPUT, str(quantity))
        self.click_element(self.ADD_ITEM_BUTTON)

    def submit_sales_note(self):
        self.click_element(self.SAVE_NOTE_BUTTON)

    def get_success_message(self):
        return self.find_element(self.SUCCESS_ALERT).text

    def get_error_message(self):
        return self.find_element(self.ERROR_ALERT).text