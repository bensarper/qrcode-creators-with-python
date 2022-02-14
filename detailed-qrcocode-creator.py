
import qrcode 

qr = qrcode.QRCode(
    version=1 , 
    error_correction=qrcode.constants.ERROR_CORRECT_L , 
    box_size=30 , 
    border=1 

)

qr.add_data("https://github.com/bensarper")
qr.make(fit=True)

image = qr.make_image(fill_color="white",back_color="black")
image.save("abc2.png")