################################################################################
# HW7, CS103 Fall 2018 Johnstone
# name:
# blazerid:
################################################################################

################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE '99' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return '99'
################################################################################

import cv2
import decimal
import numpy as np

def paddedGray (img, b):

    """Convert a colour image to grayscale, 
    and pad the image with a black border.

    The grayscale conversion of a pixel should use the following luminance
    formula: luminance = 0.2126*R + 0.7152*G + 0.0722*B
    (see HW1 for details).
    The type of each pixel should be the same as the original image.

    Params: 
        img (np.ndarray): a colour image (len(img.shape) == 3)
        b   (int):        width of border, in pixels
    Returns: (np.ndarray) grayscale equivalent, with added border b pixels wide;
                          (this image's shape tuple should be length 2)
   """                       
    
    assert (len(img.shape) == 3)
    img2 = img[:]
    img2 = cv2.copyMakeBorder(img2,b,b,b,b,cv2.BORDER_CONSTANT,value=[000])
    height,width,channels = img2.shape
    for i in range(height):
        for j in range(width):
            rnd = decimal.ROUND_HALF_UP
            b=img2[i,j,0]
            g=img2[i,j,1]
            r=img2[i,j,2]  
            assert b>=0 and b<=255
            assert g>=0 and g<=255
            assert r>=0 and r<=255          
            lum=int(r*0.2126 + g*0.7152+ b*0.0722)
            rnd = decimal.ROUND_HALF_UP
            pix = int(decimal.Decimal(lum).to_integral_value(rounding=rnd))
            img2[i,j]=pix      
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale',img2)
    cv2.imshow('Original',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img2

def blur (img, mask):

    """Apply a kernel to an image.
    See lecture discussion for how to apply the kernel.
    Only interior pixels should be changed: 
    if the mask is (2n+1)x(2n+1), the outer border of width n is unchanged.

    Clamp the output to the range [0,255]
    (for example, a negative pixel is possible, but would be bad, 
    so move it to 0; similarly, move a pixel greater than 255 to 255).

    If the kernel is a Gaussian kernel, it blurs.
    For other kernels, it may do something else 
    (e.g., sharpen, the inverse of blur).

    Params:
        img  (np.ndarray): grayscale image
        mask (np.ndarray): (2n+1)x(2n+1) mask, whose entries sum to 1
    Returns: 'blurred' image
    """

    """ uncomment once you have real parameters
    assert len(img.shape) == 2                                 # grayscale image
    assert mask.shape[0] == mask.shape[1]                          # square mask
    assert mask.shape[0]%2 == 1                                    # odd!
    """

    assert len(img.shape) == 2 
    img2=img[:]
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    height,width,channels = img2.shape

    for i in range(height):
        for j in range(width):
            if img2[i,j,0]>255:
                img2[i,j,0]=255
            if img2[i,j,0]<0:
                img2[i,j,0]=0
            if img2[i,j,1]>255:
                img2[i,j,1]=255
            if img2[i,j,1]<0:
                img2[i,j,1]=0
            if img2[i,j,2]>255:
                img2[i,j,2]=255
            if img2[i,j,2]<0:
                img2[i,j,2]=0
            
    assert mask.shape[0] == mask.shape[1]
    assert mask.shape[0]%2 == 1 
    img2 = cv2.filter2D(img2,-1,mask)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    cv2.imshow('MASK',img2)
    cv2.imshow('Original',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img2

def pages (nDigit):

    """How many pages are in a book if n digits were used to print its pages?
    Params: nDigit (int): #digits used by printer to number the pages of a book
    Returns: (int) #pages in the book
    """
    a = 0
    b = []
    c = 0 
    assert type(nDigit)==int and nDigit>0  
    for i in range(1,nDigit+1):
        b.append(len(str(i)))
    for j in b:
        a = a+j
        c+=1
        if a > nDigit:
            break
    if c<10:
        return c
    else:
        return c-1
    

