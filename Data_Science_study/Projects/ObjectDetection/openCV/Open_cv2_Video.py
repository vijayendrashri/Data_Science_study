#!/usr/bin/env python
import cv2
cap =cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

classNames = []
classFile = '../YOLO/coco.names'
with open(classFile, 'r') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = '../YOLO/yolov3.cfg'
weightPath = '../YOLO/yolov3.weights'
net = cv2.dnn_DetectionModel(weightPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

while True:
    success,img=cap.read()
    classIds, confidence, bbox = net.detect(img, confThreshold=0.5)
    print(classIds,bbox)
    if len(classIds)!=0:
        for classId, confid, box in zip(classIds.flatten(), confidence.flatten(),bbox):
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(img, classNames[classId].upper(), (box[0] + 5, box[1] + 5),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Output', img)
    key = cv2.waitKey(1)
    if key==27:
    	break


cv2.destroyAllWindows()

