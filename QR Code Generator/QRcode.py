import qrcode

# Example data (you can replace this with your own content)
data = "Hello, World"

# Output file name
filename = "my_qr_code.png"

# Generate the QR code
img = qrcode.make(data)

# Save the image to a file
img.save(filename)
