import numpy as np
from PIL import Image, ImageOps
import cv2


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

def find_start(img):
    # img : original image loaded via "load_image"
    image = np.asarray(img.rotate(90, expand=True))
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
        center = (np.round(cols[-1]-dims[0]/2), np.round(rows[-1]-dims[1]/2))
        print(center)
        return center
    else:
        return None

    # cv2.imshow('mask', mask)
    # cv2.imshow('result', result)
    # cv2.waitKey()

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