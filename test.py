import qrcode
from PIL import Image

def generate_qr_with_logo(data, logo_path, output_file):
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill='black', back_color='white')

    # Open logo and resize it
    logo = Image.open(logo_path)
    logo = logo.resize((60, 60))

    # Position the logo at the center
    img = img.convert("RGB")
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)

    # Save the QR code with the embedded logo
    img.save(output_file)

# Example usage
generate_qr_with_logo("Sample QR Data", "logo.png", "qr_with_logo.png")
