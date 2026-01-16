from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.qrScaner_page import QrScanerPage


class MainPage(BasePage):

    TITLE = (By.XPATH, "//android.widget.TextView[@text='Certifikát online']")
    BUTTON_QR = (By.XPATH, "//android.view.View[@content-desc='Načíst QR kód']")

    def verify_page_loaded(self):
        # čeká, až se nadpis objeví
        self.find(self.TITLE)
        return self

    def click_qrScener(self):
        self.click(self.BUTTON_QR)
        return QrScanerPage(self.driver)