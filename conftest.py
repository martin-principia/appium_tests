import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability("appium:deviceName", "Android")
    options.set_capability("appium:udid", "WKXORG4PFIQKRWQK")

    # spustit konkrétní aplikaci
    options.set_capability("appium:appPackage", "cz.seznam.mapy")
    options.set_capability("appium:appActivity", "cz.seznam.mapy.FreemiumActivity")
    options.set_capability("appium:appWaitPackage", "cz.seznam.mapy")
    options.set_capability("appium:appWaitActivity", "*")
    options.set_capability("appium:autoGrantPermissions", True)
    options.set_capability("appium:forceAppLaunch", True)

    options.set_capability("appium:noReset", True)
    options.set_capability("appium:ignoreHiddenApiPolicyError", True)
    # options.set_capability("appium:grantPermissions", False)
    options.set_capability("appium:skipDeviceInitialization", True)
    options.set_capability("appium:skipServerInstallation", False)
    options.set_capability("appium:newCommandTimeout", 300)

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield driver
    driver.quit()
