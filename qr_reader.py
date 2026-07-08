from pyzbar.pyzbar import decode
from PIL import Image


def read_qr(image_path):

    image = Image.open(image_path)

    qr_codes = decode(image)

    if not qr_codes:
        return None

    return qr_codes[0].data.decode("utf-8")