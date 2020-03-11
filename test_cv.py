import numpy as np
import cv2
from set_up import *


def main_mask():
	image = cv2.imread('circuits/first_try01.png')
	result = image.copy()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	lower = np.array([0,50,50]) #example value
	upper = np.array([10,255,255]) #example value
	mask = cv2.inRange(image, lower, upper)
	result = cv2.bitwise_and(result, result, mask=mask)

	cols, rows = np.nonzero(np.mean(result, axis=2))
	up_left = (cols[0], rows[0])
	bottom_right = (cols[-1], rows[-1])
	dims = (cols[-1]-cols[0], rows[-1]-rows[0])
	center = (np.round(cols[-1]-dims[0]/2), np.round(rows[-1]-dims[1]/2))
	print(center)

	# cv2.imshow('mask', mask)
	cv2.imshow('result', result)
	cv2.waitKey()


def main_convert():
	img, img_np, _ = load_image('circuits/first_try01.png')
	tmp = np.asarray(img.rotate(90, expand=True))
	result = tmp.copy()
	tmp_image = cv2.cvtColor(tmp, cv2.COLOR_BGR2HSV)

	tmp2 = cv2.imread('circuits/first_try01.png')
	result2 = tmp2.copy()
	tmp_image2 = cv2.cvtColor(tmp2, cv2.COLOR_BGR2HSV)
	# print(tmp-image)


if __name__ == '__main__':
	main_convert()