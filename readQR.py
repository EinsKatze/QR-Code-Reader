from requests import get
from pyscreenshot import grab
from pyzbar.pyzbar import decode
from os import system 
import tempfile

im = grab()

for qrcode in decode(im):
    qr_str = str(qrcode.data)
    qr_str = qr_str[2:][:-1]
    print(qr_str)
    try:
        response = get(qr_str)
        print("URL is valid and exists on the internet")
        system("start \"\" " + qr_str)

    except Exception as exception:
        print("URL does not exist on Internet")
        path = tempfile.gettempdir() + "\site.html"
        f = open(path, 'w')
        f.write(f"""<!DOCTYPE html>
<html style="background-color:#2a2a2a;" lang="en">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css">
    <body style="color:white; text-align:center;">
        <h1 style="font-family:Segoe UI;">Text of your QR-Code: <br></h1>
        <button onclick="location.href='https://github.com/EinsKatze/QR-Code-Reader'" style="background-color: transparent; width: 50px; height: 50px; border: none; cursor: pointer; position: absolute; left: 1%; top: 1%;"><i style="font-size: 44px; position: absolute; left: 1%; top: 1%;" class="fab fa-github"></i></button>
        <br>
        <code style="font-size:200%;">{qr_str}</code>
    </body>
</html>

        """)
        f.close()
        system("start " + path)

