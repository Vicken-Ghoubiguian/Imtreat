import imtreat

img = imtreat.imageManagerClass.openImageFunction("../images/lena.png", 1)

img = imtreat.bodyPartsDetectionClass.smileDetectionFunction(img)

imtreat.imageManagerClass.saveImageFunction("/Téléchargements/", "image_1", ".png", img)

