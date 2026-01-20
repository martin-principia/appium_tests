from pages.main_page import MainPage
from pages.qrScaner_page import QrScanerPage
from pages.file_picker_page import FilePickerPage
from utils.files import push_qr_image


def test_open_notifications(driver):
    # Push QR image to device
    push_qr_image(driver)
    import time
    time.sleep(2)
    
    # driver.execute_script("mobile: terminateApp", {
    #     "appId": "cz.monetplus.proidm.cpost.dev"
    # })

    driver.execute_script("mobile: activateApp", {
        "appId": "cz.monetplus.proidm.cpost.dev"
    })

    # Open app
    page = MainPage(driver)
    page.verify_page_loaded()
    page.click_qrScener().verify_page_loaded()

    # Select QR Scanner
    qr = QrScanerPage(driver)
    # Select Load Image
    qr.click_load_image()

    picker = FilePickerPage(driver)
    picker.select_qr_image()
    
    # TODO: dodelat zisk a kontrolu result
    result = qr.get_result_text()
    print("Result:", result)
    assert result == "expected-value"

    driver.save_screenshot("screen.png")
    assert driver.session_id is not None
