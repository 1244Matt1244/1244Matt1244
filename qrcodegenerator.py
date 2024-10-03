import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if data == "":
        messagebox.showwarning("Input Error", "Please enter data to generate QR Code.")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{file_name.get()}.png")
    
    messagebox.showinfo("Success", f"QR Code saved as {file_name.get()}.png")

# Set up GUI
root = Tk()
root.title("QR Code Generator")

Label(root, text="Enter Data for QR Code:").pack(pady=10)
entry = Entry(root, width=40)
entry.pack(pady=5)

Label(root, text="Enter File Name:").pack(pady=10)
file_name = Entry(root, width=40)
file_name.pack(pady=5)

Button(root, text="Generate QR Code", command=generate_qr).pack(pady=20)

root.mainloop()
