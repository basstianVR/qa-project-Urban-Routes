from selenium.webdriver.common.by import By

SELECTORS = {
    "from_field": (By.ID, 'from'),
    "to_field": (By.ID, 'to'),
    "btn_taxi": (By.XPATH, "//button[normalize-space()='Pedir un taxi']"),
    "comfort_tariff": (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]"),
    "btn_phone_number": (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[1]/div"),
    "field_phone_number": (By.ID, 'phone'),
    "btn_next_phone_number": (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[1]/form/div[2]/button"),
    "field_confirmation_code": (By.ID, 'code'),
    "btn_confirmation_code": (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/form/div[2]/button[1]"),
    "btn_method_pay": (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[2]"),
    "btn_add_card": (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]"),
    "field_input_card_number": (By.ID, 'number'),
    "field_input_card_code": (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input"),
    "btn_add_the_card": (By.XPATH, '//button[text()="Agregar"]'),
    "btn_close_method_pay_window": (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button"),
    "method_pay_setted": (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]"),
    "field_input_comment": (By.ID, 'comment'),
    "btn_blanket_and_scarves_switch": (By.XPATH, "//div[@class='workflow']//div[1]//div[1]//div[2]//div[1]//span[1]"),
    "btn_add_ice_cream": (By.XPATH, "//div[@class='r-group']//div[1]//div[1]//div[2]//div[1]//div[3]"),
    "amount_of_ice_cream": (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]"),
    "btn_request_taxi": (By.XPATH, "//*[@id='root']/div/div[3]/div[4]/button"),
    "window_order": (By.XPATH, "//*[@id='root']/div/div[5]/div[2]")
}