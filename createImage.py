import requests

from ImageGen import Image
import urllib.request


def createImage(imageDesc, imageTitle):
    imagePrompt = imageDesc

    newImage = Image(imagePrompt)
    imgURL = newImage.createImage()
    # newImage.getImageUrl()

    urllib.request.urlretrieve(imgURL, imageTitle.replace(" ", "") + ".jpg")
    return imgURL
