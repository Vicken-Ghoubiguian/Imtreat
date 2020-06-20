import imtreat

img = imtreat.openImageFunction("images/soleil.png", 1)

img = imtreat.definedModesClass.sketchModeFunction(img, False)

imtreat.saveImageFunction("/Téléchargements/", "image_1", ".png", img)
