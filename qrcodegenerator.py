import qrcode
from PIL import Image

# Function to generate QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=15,
        box_size=6,
        border=6
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

# User input for data and filename
data = input("Enter the data to be encoded in the QR code: ")
filename = input("Enter the filename for the QR code (with .png extension): ")

# Generate QR code
generate_qr_code(data, filename)
