import cv2
from cvzone.HandTrackingModule import HandDetector
from button import buttonList


video_capture = cv2.VideoCapture(0)
video_capture.set(3, 1280)
video_capture.set(4, 720)

detector = HandDetector(detectionCon=0.8)

while True:
    sucess, frame = video_capture.read()
    
    frame = cv2.flip(frame, 1)
    
    hands, frame = detector.findHands(frame)
    
    for button in buttonList:
        frame = button.draw(frame)
    
    
    if frame is None:
        continue
    
    cv2.imshow('Video', frame)
    cv2.waitKey(1)
    
    