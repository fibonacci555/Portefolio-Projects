import os
import pickle
import random

import cv2

os.system("python face_recog_train.py")
logs = open("logs.txt", "r+")

curr_log = int(logs.readline()) + 1

logs.truncate()
logs.write(str(curr_log))

frontal_face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')
profile_face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_profileface.xml')
smile_cascade = cv2.CascadeClassifier('Cascades/data/haarscascade_smile.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {"persons_name": 0}

filename = "labels.pickle"

with open(filename, 'rb') as file:
    og_lables = pickle.load(file)
    labels = {v: k for k, v in og_lables.items()}

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frontal_faces = frontal_face_cascade.detectMultiScale(gray, scaleFactor=1.5,
                                                          minNeighbors=3)  # minNeighbors. numeros maiores resultam em maior qualidade mas menos detetações
    profile_faces = profile_face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)

    for (x, y, w, h) in frontal_faces:

        face_width = x + w
        face_height = y + h
        roi_gray = gray[y:y + h, x:x + w]  # roi - region of interest
        roi_color = frame[y:y + h, x:x + w]
        id, conf = recognizer.predict(roi_gray)
        font = cv2.FONT_HERSHEY_TRIPLEX

        color = (0, 0, 0)

        name = None

        if 70 <= conf:
            print(labels[id])
            name = labels[id].replace("-", " ")
            cv2.putText(frame, name + " " + str(round(conf, 2)), (x, y - 20), font, 1, color, 2, cv2.LINE_AA)
        if 83 <= conf:
            img = f'Imgs/{labels[id].replace("-", " ")}/{curr_log}.{random.randint(0, 100000)}.png'
            cv2.imwrite(img, roi_color)
        if name is None:
            img = f'Imgs/new_faces/{curr_log}.{random.randint(0, 100000)}.png'
            cv2.imwrite(img, roi_color)

        img_item = f"{labels[id]}.png"
        cv2.imwrite(img_item, roi_color)
        cv2.rectangle(frame, (x, y + 20), (face_width, face_height), (255, 0, 100), 5)


    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
