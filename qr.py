import qrcode
from qrcode.constants import ERROR_CORRECT_L

# QR Basico
# img = qrcode.make('https://github.com/LuisMorales97')
# img.save('img/qrcode.png')

# QR Detallado
qr = qrcode.QRCode(
    version=3,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5
)

qr.add_data('https://github.com/LuisMorales97')
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="white")
img.save('img/qr_details.png', 'PNG')