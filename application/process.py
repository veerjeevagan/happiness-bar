# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:27:09 2021

@author: Mahaveerj
"""

from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import os
from application import APP_ROOT

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classifier = load_model(os.path.join(APP_ROOT,'EmotionDetectionModel.h5'))

class_labels=['Angry','Happy','Neutral','Sad','Surprise' ]


def predict_img(filename):   
    cap=cv2.imread(os.path.join(APP_ROOT,'temp\\'+filename)) 
    labels=[]
    gray=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    target=os.path.join(APP_ROOT,'temp\\'+filename)
    for (x,y,w,h) in faces:
        cv2.rectangle(cap,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray])!=0:
            roi=roi_gray.astype('float')/255.0
            roi=img_to_array(roi)
            roi=np.expand_dims(roi,axis=0)

            preds=classifier.predict(roi)[0]
            label=class_labels[preds.argmax()]
            label_position=(x,y)
            d={} #dictionary that will save results
            d[label]=preds.argmax()
            # cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            # cv2.putText(frame,'No Face Found',(20,20),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            label = "no face"
            d[label]=0
    os.remove(target)
    # cap.release()
    results = {"label" : label , "value":d[label]}
    cv2.destroyAllWindows()
    return results
        # cv2.imshow('Emotion Detector',frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
