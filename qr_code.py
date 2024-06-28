import qrcode as qr
from PIL import Image

qrr=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=4)

qrr.add_data("Hey Good Morning !!, You Can Do it Okay...")
qrr.make(fit=True)

img=qrr.make_image(fill_color="green",back_color="yellow")

img.save("Quote.png")




