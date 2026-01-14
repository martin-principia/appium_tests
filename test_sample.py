import time


def test_open_notifications(driver):
    driver.execute_script("mobile: activateApp", {
        "appId": "cz.monetplus.proidm.cpost.dev"
    })

    time.sleep(0.5)

    driver.find_element("xpath", '//android.view.View[@content-desc="Načíst QR kód"]').click()

    driver.save_screenshot("screen.png")
    assert driver.session_id is not None
