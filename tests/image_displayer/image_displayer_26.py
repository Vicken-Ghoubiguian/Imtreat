import imtreat

img = imtreat.imageManagerClass.openImageFunction("../images/lena.png", 1)

img = imtreat.bodyPartsDetectionClass.eyesDetectionFunction(img)

imtreat.imageManagerClass.displayImageFunction("experience de MMMMMOOOOIIIIIII", img)

imtreat.imageManagerClass.finishItFunction()
