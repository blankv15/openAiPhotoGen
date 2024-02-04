
import requests
import os
import shutil
from ImageGen import Image
import urllib.request

def createImage(imageDesc, imageTitle):
    imagePrompt = imageDesc

    newImage = Image(imagePrompt)
    imgURL = newImage.createImage()
    # newImage.getImageUrl()

    urllib.request.urlretrieve(imgURL, imageTitle.replace(" ", "") + ".jpg")
    shutil.move(imageTitle.replace(" ", "") + ".jpg", 'C:/Users/Hamish Chhagan/Desktop/openAiPhotoGen/photos')

    return imgURL


