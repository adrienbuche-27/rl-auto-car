import numpy as np
from PIL import Image, ImageOps
import cv2
import pygame

def load_image( infilename ) :
    img = Image.open( infilename ).convert('RGB')
    img = img.rotate(270, expand=True)
    img = ImageOps.mirror(img)
    data = np.asarray(img, dtype="int32" )
    return img, data, img.size
    
def load_image_invert( infilename ) :
    img = Image.open( infilename ).convert('RGB')
    img = img.rotate(270, expand=True)
    img = ImageOps.mirror(img)
    return invert_image(img)

def invert_image(img) :
    img = ImageOps.invert(img)
    data = np.asarray(img, dtype="int32" )
    return img, data, img.size

def find_start_ind(img):
    # img : original image loaded via "load_image"
    image = np.asarray(img.rotate(90, expand=True))
    shapes = image.shape
    result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    lower = np.array([0,50,50]) #example value
    upper = np.array([10,255,255]) #example value
    mask = cv2.inRange(image, lower, upper)
    result = cv2.bitwise_and(result, result, mask=mask)

    cols, rows = np.nonzero(np.mean(result, axis=2))
    if len(cols) != 0:
        up_left = (cols[0], rows[0])
        bottom_right = (cols[-1], rows[-1])
        dims = (cols[-1]-cols[0], rows[-1]-rows[0])
        center = (np.round(rows[-1]-dims[1]/2), shapes[0] - np.round(cols[-1]-dims[0]/2))
        return center, dims
    else:
        return None

    # cv2.imshow('mask', mask)
    # cv2.imshow('result', result)
    # cv2.waitKey()

def find_start(img, center, dims):
    img_gray = np.mean(img, axis=2)
    shape = img_gray.shape
    # print(shape)
    row, col = center

    size = int(dims[0]/2)+3
    threshold = 150
    max = 0
    max_ind = None

    for index, f in [((row+size, col, row+threshold, col+1), 'Right'),
                ((row-threshold, col, row-size, col+1), 'Left'),
                ((row, col+size, row+1, col+threshold), 'Down'),
                ((row, col-threshold, row+1, col-size), 'Up')]:
        index = np.array(index)
        index = np.where(index > 0, index, 0).astype(int)
        index = np.where(index < shape[0], index, shape[0]).astype(int)
        i,j, k,l = np.where(index < shape[1], index, shape[1]).astype(int)
        if np.mean(img_gray[i:k, j:l]) > max:
            max = np.mean(img_gray[i:k, j:l])
            max_ind = [i,j,k,l]
            flag = f

    i, j , k, l = max_ind
    src = img_gray[i:k, j:l].flatten()
    if flag in ['Up', 'Left']:
        tmp = np.nonzero(src[::-1])
    else:
        tmp = np.nonzero(src)

    middle = (tmp[0][-1], tmp[0][0])
    middle_point = int((middle[0] - middle[1])/2)

    if flag == 'Up':
        tmp = (i, l - middle[1] - middle_point)
        k = i
    elif flag == 'Down':
        tmp = (i, j + middle[1] + middle_point)
        k = i
    elif flag == 'Right':
        tmp = (i + middle[1] + middle_point, j)
        l = j
    elif flag == 'Left':
        tmp = (k - middle[1] - middle_point, j)
        l = j

    return np.array([i, j , k, l]), (flag, tmp)


colors = {'black':(0,0,0),
        'white':(255,255,255),
        'gray':(128,128,128),
        'aqua':(0,128,128),
        'navy blue':(0,0,128),
        'green':(0,255,0),
        'orange':(255,165,0),
        'yellow':(255,255,0),
        'red':(255,0,0),
        'blue':(0,0,255)}