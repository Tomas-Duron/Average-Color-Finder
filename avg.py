import cv2
import numpy as np
from tkinter import filedialog
from tkinter import *


reqimg = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files", "*.png"),("all files","*.*")))
if( reqimg != "" ):
    img = cv2.imread(reqimg)

    height = img.shape[0]
    width = img.shape[1]
    redList = []
    greenList = []
    blueList = []

    for h in range(height):
        for w in range(width):
            r,g,b = (img[h,w])
            redList.append(r)
            greenList.append(g)
            blueList.append(b)

    def listAvg(lst):
        return sum(lst)/len(lst)

    avgColor = np.zeros((height,width,3), np.uint8)
    avgColor[:] = (round(listAvg(redList)),round(listAvg(greenList)),round(listAvg(blueList)))
    print(r,g,b)

    cv2.imshow("image", avgColor)
    cv2.imshow("prevImg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print( "User canceled" )