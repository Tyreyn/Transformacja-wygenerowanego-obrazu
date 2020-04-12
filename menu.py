import cv2  
import numpy as np  

prev = cv2.imread('grid.jpg')
img = cv2.resize(prev,(600,600),interpolation = cv2.INTER_AREA)
rows,cols,ch = img.shape

cv2.circle(img, (30, 30), 5, (0, 0, 255), -1)
cv2.circle(img, (570, 30), 5, (0, 0, 255), -1)
cv2.circle(img, (570, 570), 5, (0, 0, 255), -1)
cv2.circle(img, (30, 570), 5, (0, 0, 255), -1)

pts1 = np.float32([[0, 0],
                   [600, 0],
                   [0, 600],
                   [600, 600]])
pts2 = np.float32([[0, 0],
                   [600, 0],
                   [275, 400],
                   [325, 400]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
persp = cv2.warpPerspective(img, matrix, (600, 600))

aff1 = np.float32([[50,50],
                   [200,50],
                   [50,200]])
aff2 = np.float32([[30,30],
                   [150,50],
                   [70,200]])
M = cv2.getAffineTransform(aff1,aff2)
affine = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Image", img)
cv2.imshow("Perspective transformation", persp)
cv2.imshow("Affine transformation", affine)

cv2.waitKey(0)
cv2.destroyAllWindows()