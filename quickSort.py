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

#def partition(arr,low,high): 
    #global imageNum
    #i = (low - 1)
    #pivot = arr[high]
  
    #for j in range(low , high): 
        #arr[i+1],arr[high] = arr[high],arr[i+1] 
        
        #if   arr[j] <= pivot: 
            #i = i + 1 
            #arr[i],arr[j] = arr[j],arr[i]
            
            #createImage(arr, imageNum, dim, dim)
            ##print(imageNum, arr)
            #imageNum += 1
  
    #return(i + 1) 

## Function to do Quick sort 
#def QS(array,low,high): 
    #if low <= high: 
        #pi = partition(array,low,high)   
        #QS(array, low, pi-1) 
        #QS(array, pi+1, high)
        #print(array)

#def quickSort(list_in):
    #QS(list_in, 0, len(list_in)-1)
    #global imageNum
    #createImage(list_in, imageNum, dim, dim)
    #print(imageNum)
    #imageNum += 1
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]
   global imageNum

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
           createImage(alist, imageNum, dim, dim)
           #print(imageNum)
           imageNum += 1
       
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   #createImage(alist, imageNum, dim, dim)
   #print(imageNum)
   #imageNum += 1

   return rightmark

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
    quickSort(to_sort)
    for i in range(0,60):
        createImage(to_sort, imageNum, dim, dim)
        print(imageNum)
        imageNum += 1
    
    #print(to_sort)
    total = time.time()-total_start
    print('time:',round((total)*1000)/1000,'s')
    print('each:',round((total/(dim**2))*100000)/100000,'s')
    gc.collect()
