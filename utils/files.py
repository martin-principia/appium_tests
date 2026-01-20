import base64


def push_qr_image(driver, path="tests/data/qrcode.png"):
    with open(path, "rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode("utf-8")

    driver.push_file("/sdcard/Download/qrcode.png", encoded)
