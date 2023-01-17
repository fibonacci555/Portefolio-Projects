import os
import cv2
import numpy as np
from PIL import Image
import pickle


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "imgs")

frontal_face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_label = []
x_train = []

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith('jpg') or file.endswith('png') or file.endswith('jpeg'):
            path = os.path.join(root,file)
            label = os.path.basename(root).replace(" ", "-")

            if not label in label_ids:
                label_ids[label] = current_id
                current_id = current_id +1
            id = label_ids[label]
            #convert image to numbers,

            #size = (550,500)

            pil_image = Image.open(path).convert("L") # graysclae
            #final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(pil_image, "uint8")

            faces = frontal_face_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=3)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_label.append(id)

#print(x_train)
#print(y_label)
print(label_ids)

with open("labels.pickle",'wb') as file:
    pickle.dump(label_ids,file)

recognizer.train(x_train,np.array(y_label))
recognizer.save("trainer.yml")








