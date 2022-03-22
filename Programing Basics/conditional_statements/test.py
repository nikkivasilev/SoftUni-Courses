import pyqrcode
import png
from pyqrcode import QRCode
link =
url = pyqrcode.create(link)
url.png("qr.png", scale=8)