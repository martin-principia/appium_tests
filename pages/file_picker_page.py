from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FilePickerPage(BasePage):

    # IMAGE_ITEM = (By.XPATH, '//android.widget.TextView[@text="qrcode.png"]')
    IMAGE_ITEM = (By.XPATH, '//android.view.View[contains(@content-desc, "Fotka")]')

    def select_qr_image(self):
        self.click(self.IMAGE_ITEM)
        return self
