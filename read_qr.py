import cv2

d = cv2.QRCodeDetector()

val, points, qrcode = d.detectAndDecode(cv2.imread("img/qr_details.png"))

print(val)