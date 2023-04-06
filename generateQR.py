import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=4,
    border=1,
    image_factory=qrcode.image.svg.SvgPathImage,
)

var = input('What Data should your QR-Code contain?\n> ')

qr.add_data(var)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.svg")