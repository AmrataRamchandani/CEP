import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from os.path import basename

def  linear(img,type,ran):
    imgwoext=os.path.splitext(os.path.basename(img))[0]
    imgbgr=cv2.imread(img,type)
    img = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB)
    out = np.zeros_like(img)
    blue,green,red=img[:,:,0],img[:,:,1],img[:,:,2]

    # Red Band

    rmin = red.flatten().min()      #find the min. value of pixel in the image
    rmax = red.flatten().max()    #find the max. value of pixel in the image
    rslope = 255/(rmax - rmin); #find the slope of line joining point (0,255) to (rmin,rmax)
    redimg=rslope*(red-rmin)

    # Green Band

    gmin = green.flatten().min()      #find the min. value of pixel in the image
    gmax = green.flatten().max()    #find the max. value of pixel in the image
    gslope = 255/(gmax - gmin); #find the slope of line joining point (0,255) to (rmin,rmax)
    greenimg=gslope*(green-gmin)

    # Blue Band

    bmin = blue.flatten().min()      #find the min. value of pixel in the image
    bmax = blue.flatten().max()    #find the max. value of pixel in the image
    bslope = 255/(bmax - bmin); #find the slope of line joining point (0,255) to (rmin,rmax)
    blueimg=bslope*(blue-bmin)

    out[:,:,0]=redimg
    out[:,:,1]=greenimg
    out[:,:,2]=blueimg

    cv2.imwrite('static/output/'+imgwoext+str(ran)+'_linear_out_img.jpg', out)

    plt.clf()
    plt.hist(red.flatten(),256,[0,256])
    plt.hist(green.flatten(),256,[0,256])
    plt.hist(blue.flatten(),256,[0,256])
    plt.savefig('static/output/'+imgwoext+str(ran)+'_linear_inp_hist.jpg')

    plt.clf()
    plt.hist(redimg.flatten(),256,[0,256])
    plt.hist(greenimg.flatten(),256,[0,256])
    plt.hist(blueimg.flatten(),256,[0,256])
    plt.savefig('static/output/'+imgwoext+str(ran)+'_linear_out_hist.jpg')
    plt.clf()
