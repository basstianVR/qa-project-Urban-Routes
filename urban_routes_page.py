from selectors_1 import SELECTORS
import data
from selenium.webdriver import Keys

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*SELECTORS["from_field"]).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*SELECTORS["to_field"]).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*SELECTORS["from_field"]).get_property('value')

    def get_to(self):
        return self.driver.find_element(*SELECTORS["to_field"]).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_btn_taxi(self):
        self.driver.find_element(*SELECTORS["btn_taxi"]).click()

    def click_comfort_tariff(self):
        self.driver.find_element(*SELECTORS["comfort_tariff"]).click()

    def click_phone_number(self):
        self.driver.find_element(*SELECTORS["btn_phone_number"]).click()

    def fill_field_phone_number(self):
        self.driver.find_element(*SELECTORS["field_phone_number"]).send_keys(data.phone_number)

    def click_btn_next_phone_number(self):
        self.driver.find_element(*SELECTORS["btn_next_phone_number"]).click()

    def fill_field_confirmation_code(self, code):
        self.driver.find_element(*SELECTORS["field_confirmation_code"]).send_keys(code)

    def click_btn_confirmation_code(self):
        self.driver.find_element(*SELECTORS["btn_confirmation_code"]).click()

    def click_method_pay(self):
        self.driver.find_element(*SELECTORS["btn_method_pay"]).click()

    def click_btn_add_card(self):
        self.driver.find_element(*SELECTORS["btn_add_card"]).click()

    def fill_field_input_card_number(self, card_number):
        self.driver.find_element(*SELECTORS["field_input_card_number"]).send_keys(card_number)

    def fill_field_input_card_code(self, card_code):
        self.driver.find_element(*SELECTORS["field_input_card_code"]).send_keys(card_code)

    def press_tab(self):
        self.driver.find_element(*SELECTORS["field_input_card_code"]).send_keys(Keys.TAB)

    def click_btn_add_the_card(self):
        self.driver.find_element(*SELECTORS["btn_add_the_card"]).click()

    def click_btn_close_method_pay_window(self):
        self.driver.find_element(*SELECTORS["btn_close_method_pay_window"]).click()

    def fill_field_input_comment(self, comment):
        self.driver.find_element(*SELECTORS["field_input_comment"]).send_keys(comment)

    def click_blanket_and_scarves_switch(self):
        self.driver.find_element(*SELECTORS["btn_blanket_and_scarves_switch"]).click()

    def click_btn_add_ice_cream(self):
        self.driver.find_element(*SELECTORS["btn_add_ice_cream"]).click()

    def click_btn_request_taxi(self):
        self.driver.find_element(*SELECTORS["btn_request_taxi"]).click()
