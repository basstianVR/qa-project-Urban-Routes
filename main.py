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
from retrieve_phone_code import retrieve_phone_code
from urban_routes_page import UrbanRoutesPage


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
