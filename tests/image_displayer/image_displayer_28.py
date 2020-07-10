import imtreat

img = imtreat.imageManagerClass.openImageFunction("../images/lena.png", 1)

img = imtreat.bodyPartsDetectionClass.noseDetectionFunction(img)

imtreat.imageManagerClass.displayImageFunction("experience de MMMMMOOOOIIIIIIIIIIIII", img)

imtreat.imageManagerClass.finishItFunction()
