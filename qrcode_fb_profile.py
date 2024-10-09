import qrcode
import image

qr = qrcode.QRCode(

    version = 15,
    box_size = 7,
    border = 3
)
data = "https://www.facebook.com/tahsonhossain"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill = 'black',back_color='white')
img.save('FB Profile QRscan.png')