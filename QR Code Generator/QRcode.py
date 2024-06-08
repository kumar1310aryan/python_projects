import qrcode

data = "Hello, World"

# Output file
filename = "my_qr_code.png"

img = qrcode.make(data)

img.save(filename)
