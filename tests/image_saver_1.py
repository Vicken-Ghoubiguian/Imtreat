import imtreat

from pathlib import Path

img = imtreat.openImageFunction("images/soleil.png", 0)

imtreat.saveImageFunction(str(Path.home()) + "/Téléchargements/", "image_1", ".png", img)
