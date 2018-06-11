import os
import numpy
from PIL import Image
import math
 
from matplotlib import pyplot as plt
import cv2


 

def robertMATRIX(img):
    if img.mode != "RGB":
        img = img.convert("RGB")
 
    out_img = Image.new("L", img.size, None)
    img_data = img.load()
    out_data = out_img.load()
 
    
    matrix_x = [[0, 0, 0], [0, 1, 0 ], [0, 0,-1]]
    matrix_y = [[0, 0, 0], [0, 0, 1], [0,-1, 0]]
    matrix_size = 3
    matrix_middle = matrix_size/2
 
    rows, cols = img.size
 
    for row in xrange(rows-matrix_size):
        for col in xrange(cols-matrix_size):
            # each matrix placement
 
            pixel_x = 0
            pixel_y = 0
            for i in xrange(matrix_size):
                for j in xrange(matrix_size):
                     
                    val = sum(img_data[row+i,col+j])/3
                    
                    pixel_x += matrix_x[i][j] * val
                    pixel_y += matrix_y[i][j] * val
 
            new_pixel = math.sqrt(pixel_x * pixel_x + pixel_y * pixel_y)
            new_pixel = int(new_pixel)
            out_data[row+matrix_middle,col+matrix_middle] = new_pixel
    out_img.save("output.jpg", "JPEG")
    return out_img

def Main():
 
  
   file = Image.open('dave.jpg')
    
    
   img = cv2.imread('dave.jpg',0)
   
   laplacian = cv2.Laplacian(img,cv2.CV_16S)
   sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
   plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
   plt.title('Original'), plt.xticks([]), plt.yticks([])
   plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
   plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
   plt.subplot(2,2,3),plt.imshow(sobelx8u,cmap = 'gray')
   plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
   #plt.subplot(2,2,4),plt.imshow(robert,cmap = 'gray')
   #plt.title('Roberts Cross'), plt.xticks([]), plt.yticks([])
   plt.show()
   print ("Robert cross image generate in directory")
   robert = robertMATRIX(file)
 
Main()	  
