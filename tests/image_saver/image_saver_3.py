import imtreat

img = imtreat.imageManagerClass.openImageFunction("../images/soleil.png", 0)

img = imtreat.definedModesClass.hueSaturationLightnessModeFunction(img)

imtreat.imageManagerClass.saveImageFunction("/Téléchargements/", "image_1", ".png", img)
