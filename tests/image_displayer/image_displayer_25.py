import imtreat

img = imtreat.imageManagerClass.openImageFunction("../images/lena.png", 1)

img = imtreat.bodyPartsDetectionClass.faceDetectionFunction(img)

imtreat.imageManagerClass.displayImageFunction("experience de MMMMMOOOOIIIIIIIIIII", img)

imtreat.imageManagerClass.finishItFunction()
