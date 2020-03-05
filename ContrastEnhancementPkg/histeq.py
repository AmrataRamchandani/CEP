import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
import os
from os.path import basename

def histogram(img):
    height = img.shape[0]
    width = img.shape[1]
    hist = np.zeros((256))

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            hist[a] += 1

    return hist

def cumulative_histogram(hist):
    cum_hist = hist.copy()

    for i in np.arange(1, 256):
        cum_hist[i] = cum_hist[i-1] + cum_hist[i]

    return cum_hist

def  histeq(img,type,ran):
    imgwoext=os.path.splitext(os.path.basename(img))[0]
    imgbgr = cv2.imread(img, type)

    image = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB) #check this function
    out = np.zeros_like(image)
    blue,green,red=image[:,:,0],image[:,:,1],image[:,:,2] #manipulate this line

    plt.clf()
    plt.hist(red.flatten(),256,[0,256], color = 'r')
    plt.hist(green.flatten(),256,[0,256], color = 'g')
    plt.hist(blue.flatten(),256,[0,256], color = 'b')
    plt.savefig('static/output/'+imgwoext+str(ran)+'_histeq_inp_hist.jpg')

    # Red Band
    redheight = red.shape[0]
    redwidth = red.shape[1]
    redpixels = redwidth * redheight

    redhist = histogram(red)
    redcum_hist = cumulative_histogram(redhist)

    for i in np.arange(redheight):
        for j in np.arange(redwidth):
            a = red.item(i,j)
            b = math.floor(redcum_hist[a] * 255.0 / redpixels)
            red.itemset((i,j), b)

    # Green Band
    greenheight = green.shape[0]
    greenwidth = green.shape[1]
    greenpixels = greenwidth * greenheight

    greenhist = histogram(green)
    greencum_hist = cumulative_histogram(greenhist)

    for i in np.arange(greenheight):
        for j in np.arange(greenwidth):
            a = green.item(i,j)
            b = math.floor(greencum_hist[a] * 255.0 / greenpixels)
            green.itemset((i,j), b)

    # Blue Band
    blueheight = blue.shape[0]
    bluewidth = blue.shape[1]
    bluepixels = bluewidth * blueheight

    bluehist = histogram(blue)
    bluecum_hist = cumulative_histogram(bluehist)

    for i in np.arange(blueheight):
        for j in np.arange(bluewidth):
            a = blue.item(i,j)
            b = math.floor(bluecum_hist[a] * 255.0 / bluepixels)
            blue.itemset((i,j), b)


    out[:,:,0]=red
    out[:,:,1]=green
    out[:,:,2]=blue

    cv2.imwrite('static/output/'+imgwoext+str(ran)+'_histeq_out_img.jpg', out)

    plt.clf()
    plt.hist(red.flatten(),256,[0,256], color = 'r')
    plt.hist(green.flatten(),256,[0,256], color = 'g')
    plt.hist(blue.flatten(),256,[0,256], color = 'b')
    plt.savefig('static/output/'+imgwoext+str(ran)+'_histeq_out_hist.jpg')
    plt.clf()
