import imtreat

img = imtreat.imageManagerClass.openImageFunction("../images/soleil.png", 0)

imtreat.imageManagerClass.saveImageFunction("/Téléchargements/", "image_1", ".png", img)
