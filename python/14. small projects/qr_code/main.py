import qrcode

# Get the URL from the user
url = input("Enter the URL: ").strip()
file_path = "qrcode.png"

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create the image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save(file_path)

print("QR code generated and saved as", file_path)