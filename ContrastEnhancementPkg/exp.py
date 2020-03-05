import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
from os.path import basename

def exp(img1,type,ran,g):
    imgwoext=os.path.splitext(os.path.basename(img1))[0]
    imgbgr = cv2.imread(img1, type)
    out = np.zeros_like(imgbgr)
    image = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB) #check this function
    blue,green,red=image[:,:,0],image[:,:,1],image[:,:,2] #manipulate this line
    gamma=float(g)
    rednew = np.zeros_like(red)
    red = red.astype(float)

    greennew = np.zeros_like(green)
    green = green.astype(float)

    bluenew = np.zeros_like(blue)
    blue = blue.astype(float)

    # Red Band
    redheight=red.shape[0]
    redwidth=red.shape[1]

    for i in np.arange(redheight):
        for j in np.arange(redwidth):
            rednew[i][j] = 255*((red.item(i,j)/255.0)**gamma);

    rednew = rednew.astype(np.uint8)

    # Green Band
    greenheight=green.shape[0]
    greenwidth=green.shape[1]

    for i in np.arange(greenheight):
        for j in np.arange(greenwidth):
            greennew[i][j] = 255*((green.item(i,j)/255.0)**gamma);

    greennew = greennew.astype(np.uint8)

    # Blue Band
    blueheight=blue.shape[0]
    bluewidth=blue.shape[1]

    for i in np.arange(blueheight):
        for j in np.arange(bluewidth):
            bluenew[i][j] = 255*((blue.item(i,j)/255.0)**gamma);

    bluenew = bluenew.astype(np.uint8)

    out[:,:,0]=rednew
    out[:,:,1]=greennew
    out[:,:,2]=bluenew

    cv2.imwrite('static/output/'+imgwoext+str(ran)+'_exp_out_img.jpg', out)

    plt.clf()
    plt.hist(red.flatten(),256,[0,256], color = 'r')
    plt.hist(green.flatten(),256,[0,256], color = 'g')
    plt.hist(blue.flatten(),256,[0,256], color = 'b')
    plt.savefig('static/output/'+imgwoext+str(ran)+'_exp_inp_hist.jpg')

    plt.clf()
    plt.hist(rednew.flatten(),256,[0,256], color = 'r')
    plt.hist(greennew.flatten(),256,[0,256], color = 'g')
    plt.hist(bluenew.flatten(),256,[0,256], color = 'b')
    plt.savefig('static/output/'+imgwoext+str(ran)+'_exp_out_hist.jpg')
    plt.clf()
