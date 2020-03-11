import numpy as np
import cv2

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