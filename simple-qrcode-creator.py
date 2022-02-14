
import qrcode

image = qrcode.make("https://github.com/bensarper")
image.save("abc.png")

