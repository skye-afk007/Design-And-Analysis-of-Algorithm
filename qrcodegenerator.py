# First, install the library by running: pip install qrcode[pil]

import qrcode

# Prompt the user to enter the text they want to encode
data = input("Enter the text or URL to generate a QR code: ")

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code, use 1 for a small code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Border size (minimum is 4)
)

# Add the user-defined data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill="black", back_color="white")
img.save("user_defined_qrcode.png")

print("QR code generated and saved as 'user_defined_qrcode.png'.")
