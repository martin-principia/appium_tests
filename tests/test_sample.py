from pages.main_page import MainPage


def test_open_notifications(driver):
    driver.execute_script("mobile: activateApp", {
        "appId": "cz.monetplus.proidm.cpost.dev"
    })

    # Main Page
    page = MainPage(driver)
    page.verify_page_loaded().click_qrScener().verify_page_loaded()

    driver.save_screenshot("screen.png")
    assert driver.session_id is not None
