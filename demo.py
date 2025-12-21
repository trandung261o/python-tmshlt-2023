import tmsangdev
import qrcode


result = tmsangdev.roll_dice(6)
print(result)

image = qrcode.make("https://youtube.com/@tmsangdev")

image.save("qrcode.png", "PNG")
