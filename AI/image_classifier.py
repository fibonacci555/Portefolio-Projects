import numpy as np
import cv2
import os


# Import Images
path = 'Imgs'
images = []
classNames = []
myList = os.listdir(path)

print('Total Classes Detected', len(myList))

for img in myList:
    cur = cv2.imread(f'{path}/{img}')
    images.append(cur)
    classNames.append(os.path.splitext(img)[0])

print(classNames)


orb = cv2.ORB_create(nfeatures=10000) # decriptor
def findDes(imgs):
    desList = []
    for img in imgs:
        kp,des = orb.detectAndCompute(img,None)
        desList.append(des)
    return desList

def findID(img,desList,op):
    kp2,des2 = orb.detectAndCompute(img,None)
    bf = cv2.BFMatcher()
    matchList = []
    finalValue = -1
    for a in desList:
        matches = bf.knnMatch(a, des2, k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.9 * n.distance:  # distance é tipo o quão duas zonas sao parecidos na imagem
                good.append([m])

        matchList.append(len(good))
    print(matchList)
    if len(matchList) != 0:
        if op < max(matchList):
            finalValue = matchList.index(max(matchList))
        else: pass

    return finalValue


desList = findDes(images)

print(len(desList))

cap = cv2.VideoCapture(0)

while True:
    sucess, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    try:

        id = findID(img2,desList,3)
        if id != -1:
            cv2.putText(imgOriginal,classNames[id],(50,50),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),1)
    except:
        pass


    cv2.imshow("img2",imgOriginal)
    cv2.waitKey(1)




