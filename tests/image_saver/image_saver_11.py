import imtreat

img = imtreat.imageManagerClass.openImageFunction("../images/soleil.png", 1)

img = imtreat.definedModesClass.oceanModeFunction(img)

imtreat.imageManagerClass.saveImageFunction("/Téléchargements/", "image_1", ".png", img)
