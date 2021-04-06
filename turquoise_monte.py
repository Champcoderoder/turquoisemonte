# Program na tym etapie działa
# Zmienia rozmiar obrazu i dodaje ramkę
import easygui
from PIL import Image
from PIL import ImageOps

imgname = easygui.enterbox("Nazwa obrazu: ")

# Wartość basewidth i hsize ustawiona na sztywno na 444
# Zostawiam poniższą linię kodu gdybym kiedyś chciał przebudować projekt
# basewidth = int(easygui.enterbox("Szerokość obrazu: "))

basewidth = 444
img = Image.open(imgname)
wpercent = (basewidth / float(img.size[0]))
# hsize = int((float(img.size[1]) * float(wpercent)))
hsize = 444
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save(imgname)

# Wartość border ustawiona na sztywno na 10
# Zostawiam poniższą linię kodu gdybym kiedyś chciał przebudować projekt
# border = int(easygui.enterbox("Rozmiar ramki: "))

img = Image.open(imgname)
img_with_border = ImageOps.expand(img, border=10, fill="turquoise")
img_with_border.save(imgname)
