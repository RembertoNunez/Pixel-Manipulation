#Pillow, Statistics, and Numpy libraries
from PIL import Image
import numpy
import statistics

#create a list for the images
imgList = []
#for loop to get the pictures from 1 to 9
for i in range(1,10):
    imgList.append(Image.open(str(i)+".png"))
#getting the width and the hight from the images  
picW, picH = imgList[0].size
#creating a new color image using the width and hight grabed from the previews images 
newImg = Image.new("RGB", (picW, picH), "white")
#creating a list to store each color pixels
redPixelList = []
greenPixelList = []
bluePixelList = []
#nested for loop to access the images
for y in range (picH):
    for x in range (picW):
        for myImage in imgList:
            #getting the pixels from the images and storing in the eache pixel lists
            myRed, myGreen, myBlue = myImage.getpixel((x,y))
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
        #sorting the pixels in each list
        redPixelList = sorted(redPixelList)
        greenPixelList = sorted(greenPixelList)
        bluePixelList = sorted(bluePixelList)
        #getting the median from each list using the statiscs and numpy libraries 
        medianRed = statistics.median(redPixelList)
        medianGreen = statistics.median(greenPixelList)
        medianBlue = statistics.median(bluePixelList)
        #putting the corrected pixels back to the new image
        newImg.putpixel((x,y),(medianRed, medianGreen, medianBlue))
        #setting the list of the pixels back nothing
        redPixelList[:] = []
        greenPixelList[:] = []
        bluePixelList[:] = []
#setting the name from the new image created   
newImg.save("newImage.png")