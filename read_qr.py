import cv2

d = cv2.QRCodeDetector()

val, points, qrcode = d.detectAndDecode(cv2.imread("https://github.com/LuNiZz/davet/blob/main/qrcode.png?raw=true"))

print(val)
