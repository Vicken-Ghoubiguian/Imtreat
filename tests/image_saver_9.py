import imtreat

img = imtreat.openImageFunction("images/soleil.png", 1)

img = imtreat.oilPaintingModeFunction(img)

imtreat.saveImageFunction("/Téléchargements/", "image_1", ".png", img)