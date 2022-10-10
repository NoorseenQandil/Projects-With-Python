import pyqrcode
from pyqrcode import QRCode
x = "https://www.youtube.com"
url = pyqrcode.create(x)
url.svg("youtube.svg", scale = 8) 