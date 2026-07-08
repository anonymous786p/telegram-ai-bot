import cv2


def read_qr(image_path):

    image = cv2.imread(image_path)

    detector = cv2.QRCodeDetector()

    data, bbox, _ = detector.detectAndDecode(image)

    if bbox is None:
        return None

    if data == "":
        return None

    return data.strip()