import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    btn_taxi = (By.XPATH, "//button[normalize-space()='Pedir un taxi']")
    comfort_tariff = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]")
    btn_phone_number = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[1]/div")
    field_phone_number = (By.ID, 'phone')
    btn_next_phone_number = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[1]/form/div[2]/button")
    field_confirmation_code = (By.ID, 'code')
    btn_confirmation_code = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/form/div[2]/button[1]")
    btn_method_pay = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[2]")
    btn_add_card = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]")
    field_input_card_number = (By.ID, 'number')
    field_input_card_code = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input")
    btn_add_the_card = (By.XPATH, '//button[text()="Agregar"]')
    btn_close_method_pay_window = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    method_pay_setted = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]")
    field_input_comment = (By.ID, 'comment')
    btn_blanket_and_scarves_switch = (By.XPATH, "//div[@class='workflow']//div[1]//div[1]//div[2]//div[1]//span[1]")
    btn_add_ice_cream = (By.XPATH, "//div[@class='r-group']//div[1]//div[1]//div[2]//div[1]//div[3]")
    amount_of_ice_cream = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]")
    btn_request_taxi = (By.XPATH, "//*[@id='root']/div/div[3]/div[4]/button")
    window_order = (By.XPATH, "//*[@id='root']/div/div[5]/div[2]")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_btn_taxi(self):
        self.driver.find_element(*self.btn_taxi).click()

    def click_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    def click_phone_number(self):
        self.driver.find_element(*self.btn_phone_number).click()

    def fill_field_phone_number(self):
        self.driver.find_element(*self.field_phone_number).send_keys(data.phone_number)

    def click_btn_next_phone_number(self):
        self.driver.find_element(*self.btn_next_phone_number).click()

    def fill_field_confirmation_code(self, code):
        self.driver.find_element(*self.field_confirmation_code).send_keys(code)

    def click_btn_confirmation_code(self):
        self.driver.find_element(*self.btn_confirmation_code).click()

    def click_method_pay(self):
        self.driver.find_element(*self.btn_method_pay).click()

    def click_btn_add_card(self):
        self.driver.find_element(*self.btn_add_card).click()

    def fill_field_input_card_number(self, card_number):
        self.driver.find_element(*self.field_input_card_number).send_keys(card_number)

    def fill_field_input_card_code(self, card_code):
        self.driver.find_element(*self.field_input_card_code).send_keys(card_code)

    def press_tab(self):
        self.driver.find_element(*self.field_input_card_code).send_keys(Keys.TAB)

    def click_btn_add_the_card(self):
        self.driver.find_element(*self.btn_add_the_card).click()

    def click_btn_close_method_pay_window(self):
        self.driver.find_element(*self.btn_close_method_pay_window).click()

    def fill_field_input_comment(self, comment):
        self.driver.find_element(*self.field_input_comment).send_keys(comment)

    def click_blanket_and_scarves_switch(self):
        self.driver.find_element(*self.btn_blanket_and_scarves_switch).click()

    def click_btn_add_ice_cream(self):
        self.driver.find_element(*self.btn_add_ice_cream).click()

    def click_btn_request_taxi(self):
        self.driver.find_element(*self.btn_request_taxi).click()


class TestUrbanRoutes:

    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        #Espera de 2 segundos para asegurar la carga de los componentes antes de que se ejecuten las pruebas
        cls.driver.implicitly_wait(2)
        # Inicializar la instancia de UrbanRoutesPage una vez para todas las pruebas
        cls.routes_page = UrbanRoutesPage(cls.driver)
        cls.driver.maximize_window()


    # 1. Configurar la dirección
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to


    # 2. Seleccionar la tarifa Comfort
    def test_set_tcard(self):
        self.routes_page.click_btn_taxi()
        self.routes_page.click_comfort_tariff()
        comfort_tariff = self.driver.find_element(*self.routes_page.comfort_tariff)
        assert "active" in comfort_tariff.get_attribute(
            "class"), "La tarifa 'Comfort' no fue seleccionada correctamente"

    # 3. Rellenar el numero de telefono
    def test_set_phone_number(self):
        self.routes_page.click_phone_number()
        self.routes_page.fill_field_phone_number()
        self.routes_page.click_btn_next_phone_number()

        code = retrieve_phone_code(self.driver)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.routes_page.field_confirmation_code)
        )
        self.routes_page.fill_field_confirmation_code(code)
        self.routes_page.click_btn_confirmation_code()

        number_validation = self.driver.find_element(*self.routes_page.field_phone_number).get_attribute("value")
        assert number_validation == data.phone_number

    # 4. Agregar una tarjeta de crédito
    def test_set_method_pay(self):
        self.routes_page.click_method_pay()
        self.routes_page.click_btn_add_card()
        self.routes_page.fill_field_input_card_number(data.card_number)
        self.routes_page.fill_field_input_card_code(data.card_code)
        self.routes_page.press_tab()
        self.routes_page.click_btn_add_the_card()
        self.routes_page.click_btn_close_method_pay_window()

        method_pay = self.driver.find_element(*self.routes_page.method_pay_setted).text
        assert "Tarjeta" == method_pay, "La tarjeta no se guardo correctamente"

    # 5. Escribir un mensaje para el controlador
    def test_set_a_comment(self):
        self.routes_page.fill_field_input_comment(data.message_for_driver)
        comment = self.driver.find_element(*self.routes_page.field_input_comment).get_attribute("value")
        assert data.message_for_driver == comment, "El comentario no se guardo correctamente"



    # 6. Pedir una manta y pañuelos
    def test_request_blanket_and_scarves(self):
        self.routes_page.click_blanket_and_scarves_switch()
        blanket_and_scarves_switch = self.driver.find_element(*self.routes_page.btn_blanket_and_scarves_switch)
        assert blanket_and_scarves_switch.is_selected() == False, "El switch no esta activo"

    # 7. Pedir 2 helados
    def test_add_ice_cream(self):
        self.routes_page.click_btn_add_ice_cream()
        self.routes_page.click_btn_add_ice_cream()
        amount_ice_cream = self.driver.find_element(*self.routes_page.amount_of_ice_cream).text
        amount_ice_cream = int(amount_ice_cream)
        assert amount_ice_cream == 2

    # 8. Aparece el modal para buscar un taxi
    def test_request_taxi(self):
        self.routes_page.click_btn_request_taxi()
        assert self.driver.find_element(*self.routes_page.window_order).is_displayed()
        time.sleep(4)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
