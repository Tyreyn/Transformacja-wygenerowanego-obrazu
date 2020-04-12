import cv2  
import numpy as np  
# ***** WCZYTANIE ZDJECIA *****
prev = cv2.imread('grid.jpg')
# ***** ZMNIEJSZENIE ZDJECIA DO WYMIARÓW 600X600 *****
img = cv2.resize(prev,(600,600),interpolation = cv2.INTER_AREA)
rows,cols,ch = img.shape

# ***** RYSOWANIE KÓŁ NA OBRAZIE ABY BARDZIEJ UWIDOCZNIĆ EFEKTY PRZEKSZTAŁCEŃ *****
cv2.circle(img, (30, 30), 5, (0, 0, 255), -1)
cv2.circle(img, (570, 30), 5, (0, 0, 255), -1)
cv2.circle(img, (570, 570), 5, (0, 0, 255), -1)
cv2.circle(img, (30, 570), 5, (0, 0, 255), -1)

# ***** WYZNACZANIE PUNKTÓW DLA PRZEKSZTAŁCENIA PERSPEKTYWICZNEGO*****
# ***** pers1 - POCZĄTKOWE WSPÓŁRZĘDNE *****
# ***** pers2 - WSPÓŁRZEDNE DO KTÓRYCH DĄŻYMY *****
# ***** WYZNACZAMY SOBIE JAKIŚ OBSZAR ZA POMOCĄ pers1
# ***** W pers2 USTAWIAMY JAK MA SIĘ ZMIENIĆ TEN OBRAZ
pers1 = np.float32([[0, 0],
                   [600, 0],
                   [0, 600],
                   [600, 600]])
pers2 = np.float32([[0, 0],
                   [600, 0],
                   [275, 400],
                   [325, 400]])

# ***** WYKONANIE PRZEKSZTAŁCENIA *****
matrix = cv2.getPerspectiveTransform(pers1, pers2)
persp = cv2.warpPerspective(img, matrix, (600, 600))

# ***** WYZNACZENIE PUNKTÓW DLA PRZEKSZTAŁCENIA AFINICZNEGO *****
# ***** aff1 - PUNKTY NA PODSTAWIE ***** 
aff1 = np.float32([[30,30],
                   [570,30],
                   [570,570]])
aff2 = np.float32([[60,60],
                   [400,30],
                   [450,450]])

# ***** WYZNACZENIE DANYCH DO ROTACJI I SKALI *****
# ***** center - PUNKT WOKÓŁ KTÓREGO ROBIMY ROTACJE *****
# ***** angle - KĄT WYKONYWANEJ ROTACJI *****
# ***** scale - PRZESKALONOWANIE || >1 POWIĘKSZENIE || <1 POMNIEJSZENIE  || 1 - ORYGINAŁ*****
center = ( 300, 300 )
angle = 30
scale = 1
# ***** WYKONANIE PRZEKSZTAŁCEŃ  AFINICZNYCH*****
M = cv2.getAffineTransform(aff1,aff2)
affine = cv2.warpAffine(img,M,(cols,rows))
# ***** WYKONANIE ROTACJI 
#M = cv2.getRotationMatrix2D(center, angle, scale)
#affine = cv2.warpAffine(img,M,(cols,rows))

# ***** WYSWIETLENIE UZYSKANYCH PRZEKSZTAŁCEŃ *****
cv2.imshow("Image", img)
cv2.imshow("Perspective transformation", persp)
cv2.imshow("Affine transformation", affine)

# ***** ZAPIS OBRAZKOW *****
cv2.imwrite("wyjsciowe/affiniczne.jpg",affine)
cv2.imwrite("wyjsciowe/perspektywiczne.jpg",persp)

cv2.waitKey(0)
cv2.destroyAllWindows()