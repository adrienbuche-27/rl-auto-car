import numpy as np
from PIL import Image, ImageOps


def load_image( infilename ) :
    img = Image.open( infilename ).convert('RGB')
    img = img.rotate(270, expand=True)
    img = ImageOps.mirror(img)
    data = np.asarray(img, dtype="int32" )
    return data, img.size
    
def load_image_invert( infilename ) :
    img = Image.open( infilename ).convert('RGB')
    img = img.rotate(270, expand=True)
    img = ImageOps.mirror(img)
    img = ImageOps.invert(img)
    data = np.asarray(img, dtype="int32" )
    return data, img.size

def search_start(array):
	rows, cols, dims = array.shape
	for i in range(rows):
		for j in range(cols):
			if array[i,j,1] != 0 and array[i,j,1] != 255:
				print(i,j,array[i,j,1])

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