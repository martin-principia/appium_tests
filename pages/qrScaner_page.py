from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QrScanerPage(BasePage):

    TITLE = (By.XPATH, '//android.widget.TextView[@text="QR skener"]')
    # SCAN_WINDOW = (By.XPATH, '//android.widget.FrameLayout[@content-desc="QR skener"]')

    def verify_page_loaded(self):
        # čeká, až se nadpis objeví
        self.find(self.TITLE)
        return self
    
    def click_load_image(self):
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="Vybrat obrázek"]').click()
        return self