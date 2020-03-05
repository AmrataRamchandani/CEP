import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from os.path import basename

def stdev(img1,type,ran,kscale):
    imgwoext=os.path.splitext(os.path.basename(img1))[0]
    imgbgr=cv2.imread(img1, type)
    k=float(kscale)
    img = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB) #check this function
    out = np.zeros_like(img)
    blue,green,red=img[:,:,0],img[:,:,1],img[:,:,2] #manipulate this line

    # Red Band
    red=red.astype(float)
    red_mean=red.mean()
    red_std=red.std()
    red_min=red_mean-(k*red_std)
    red_max=red_mean+(k*red_std)
    red_range=(red_max-red_min)
    red_new= ((red - red_min)* 255/red_range)
    red_new[red_new<0]=0
    red_new[red_new>255]=255

    # Green Band
    green=green.astype(float)
    green_mean=green.mean()
    green_std=green.std()
    green_min=green_mean-(k*green_std)
    green_max=green_mean+(k*green_std)
    green_range=(green_max-green_min)
    green_new=((green - green_min)*255/green_range)
    green_new[green_new<0]=0
    green_new[green_new>255]=255

    # Blue Band
    blue=blue.astype(float)
    blue_mean=blue.mean()
    blue_std=blue.std()
    blue_min=blue_mean-(k*blue_std)
    blue_max=blue_mean+(k*blue_std)
    blue_range=(blue_max-blue_min)
    blue_new= ((blue - blue_min)*255/blue_range)
    blue_new[blue_new<0]=0
    blue_new[blue_new>255]=255

    out[:,:,0]=red_new
    out[:,:,1]=green_new
    out[:,:,2]=blue_new

    cv2.imwrite('static/output/'+imgwoext+str(ran)+'_stdev_out_img.jpg', out)

    plt.clf()
    plt.hist(red.flatten(),256,[0,256], color = 'r')
    plt.hist(green.flatten(),256,[0,256], color = 'g')
    plt.hist(blue.flatten(),256,[0,256], color = 'b')
    plt.savefig('static/output/'+imgwoext+str(ran)+'_stdev_inp_hist.jpg')

    plt.clf()
    plt.hist(red_new.flatten(),256,[0,256], color = 'r')
    plt.hist(green_new.flatten(),256,[0,256], color = 'g')
    plt.hist(blue_new.flatten(),256,[0,256], color = 'b')
    plt.savefig('static/output/'+imgwoext+str(ran)+'_stdev_out_hist.jpg')
    plt.clf()
