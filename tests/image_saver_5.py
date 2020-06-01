import imtreat

img = imtreat.openImageFunction("images/soleil.png", 1)

img = imtreat.sketchModeFunction(img, True)

imtreat.saveImageFunction("/Téléchargements/", "image_1", ".png", img)
