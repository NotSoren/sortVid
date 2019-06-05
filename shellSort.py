import math
from PIL import Image
import sys
import re
import multiprocessing
import time
import gc
import os
from multiprocessing import Pool
from random import randint


def createImage(array, name, xr, yr):
    pixels = [[[0 for k in range(3)] for j in range(xr)] for i in range(yr)]
    array_tmp = array
    i = 0
    for y in range(0,yr):
        for x in range(0,xr):
            pixels[y][x] = stepToPix(array_tmp[i])
            i+=1
    
    pixels = [item for sublist in pixels for item in sublist]
    pixels = [tuple(l) for l in pixels]
    im2 = Image.new("RGB", (xr, yr))
    im2.putdata(pixels)
    im2.save(str(name)+".png")


def stepToPix(step):
    failed_colour = (255,255,255)
    #print(step,end=',')
    return([int(round(l*step/1000)) for l in (255, 255, 255)])
    if step == -1:
        o = failed_colour
    elif step >= 100000:
        o = (255, 255, 255)
    elif step > 10000:
        o = [int(round(l*step/100000)) for l in (0, 0, 255)]
    elif step > 1000:
        o = [int(round(l*step/10000)) for l in (255, 0, 255)]
    elif step > 100:
        o = [int(round(l*step/1000)) for l in (255, 0, 0)]
    elif step > 10:
        o = [int(round(l*step/100)) for l in (0, 255, 0)]
    else:
        o = [int(round(l*step/10)) for l in (0, 255, 255)]
    return(o)


def shellSort(arr): 
    global imageNum
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gaps = [1, 4, 10, 23, 57, 132, 301, 701, 1750, 4375, 10937]
    place = len(gaps) - 1
    while gaps[place] >= n:
        place+=-1
    
    while place >= 0: 
        gap = gaps[place]
        print(gap)
        for i in range(gap,n): 
            
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
            
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
                #createImage(arr, imageNum, dim, dim)
                #print(imageNum)
                #imageNum += 1
            
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
            createImage(arr, imageNum, dim, dim)
            #print(imageNum)
            imageNum += 1
        place+=-1       

if __name__ == '__main__':
    total_start = time.time() # Starting timer
    imageNum = 1
    args = sys.argv # Collecting arguments
    #print(args)
    if len(args) >= 2:
        dim = int(re.sub('[^0-9]', '', args[1]))
        to_sort=[]
        for a in range(0,dim ** 2):to_sort.append(randint(1,1000))
    else: 
        to_sort=[]
        for a in range(0,10 ** 2):to_sort.append(randint(1,1000))
    shellSort(to_sort)
    for i in range(0,60):
        createImage(to_sort, imageNum, dim, dim)
        print(imageNum)
        imageNum += 1
    
    #print(to_sort)
    total = time.time()-total_start
    print('time:',round((total)*1000)/1000,'s')
    print('each:',round((total/(dim**2))*100000)/100000,'s')
    gc.collect()
 
