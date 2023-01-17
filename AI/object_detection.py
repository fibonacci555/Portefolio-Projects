import numpy as np
import cv2

img1 = cv2.imread("Imgs/joao.png", 1) #open image
img2 = cv2.imread("Imgs/joao (2).png", 1)


credibility = 10 # quão mais pequeno menos accurate

orb = cv2.ORB_create(nfeatures=10000) # decriptor

kp1 , des1 = orb.detectAndCompute(img1,None) #criar o keypoints de imagem
kp2 , des2 = orb.detectAndCompute(img2,None)

#imgKp1 = cv2.drawKeypoints(img1,kp1,None) #mostrar os keypoints numa image
#imgKp2 = cv2.drawKeypoints(img2,kp2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good = []


for m,n in matches:
    if m.distance < credibility*0.1 * n.distance: # distance é tipo o quão duas zonas sao parecidos na imagem
        good.append([m])

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
#cv2.imshow("Kp1", imgKp1)
#cv2.imshow("Kp2", imgKp2)


#cv2.imshow("img1",img1) # mostrar image
cv2.imshow("img3",img3)
print(len(good))

cv2.waitKey(0)
