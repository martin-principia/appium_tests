def test_open_notifications(driver):
    driver.execute_script("mobile: activateApp", {
        "appId": "cz.seznam.mapy"
    })

    driver.save_screenshot("screen.png")
    assert driver.session_id is not None
