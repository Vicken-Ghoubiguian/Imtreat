import imtreat

img = imtreat.openImageFunction("images/soleil.png", 0)

img = imtreat.edgeDetectionModeFunction(img)

imtreat.saveImageFunction("/Téléchargements/", "image_1", ".png", img)
