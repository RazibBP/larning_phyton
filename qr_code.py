import qrcode
import image

qr = qrcode.QRCode(
    version = 15,
    box_size = 6,
    border = 5
)
data = "https://www.facebook.com/mdrajib.bp/?viewas=100000686899395"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='balck',back_color='white')
img.save('text.png')