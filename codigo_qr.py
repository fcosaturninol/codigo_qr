# Importamos la libreria qrcode que nos permite
# relizar nuestros QR.
import qrcode

# A donde apuntara al escanear el codio QR
website = "https://duendetech.blogspot.com/"

# Configuramos el tamaño y grosor del QR
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website)
qr.make()

# Establece el color de linea en color negro y color de fondo en color blanco
img = qr.make_image(fill_color='black', back_color='white')

# Guardamos el QR en una imagen .png
img.save('codigo_qr.png')
