import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 6, # size of the box where qr code will be displayed
    border = 6  # it is the whit part of image -- border in all 4 sides with white color  
)

data = "https://www.youtube.com/watch?v=vrfJF5QYLfQ"


qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_color = "white")
img.save("test.png")