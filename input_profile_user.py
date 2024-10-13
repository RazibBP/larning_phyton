import qrcode
import image

qr = qrcode.QRCode(
    version=15,
    border=5,
    box_size=7
)
print("QRcode make python code.")
data = input("Enter tour link:")
qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill='black',back_color='white')
img.save("qrcode make.png")