import qrcode as qr
img= qr.make("https://www.linkedin.com/in/rohit-sahu-7142742a7?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
img.save("qrcode.png")

