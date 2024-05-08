import cv2
from cvzone.HandTrackingModule import HandDetector
from button import buttonList
import time
from pynput.keyboard import Controller, Key

last_click_time = 0
cooldown = 0.7

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
        
    if hands:
        lmList = hands[0]['lmList']
        bbox = hands[0]['bbox']
        
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            
            over = button.isOver(lmList, frame)
            
            if over:
                lenght, _, _ = detector.findDistance(lmList[8][:2], lmList[4][:2], frame)
                click = button.click(lenght, frame)
                
                if click and (time.time() - last_click_time) > cooldown:
                    last_click_time = time.time()
                    
                    if button.text == "SPACE":
                        Controller().press(key=Key.space)
                    elif button.text == "DEL":
                        Controller().press(key=Key.backspace)
                    else:
                        Controller().press(key=button.text)
    
    if frame is None:
        continue
    
    cv2.imshow('Virtual Keyboard', frame)
    cv2.waitKey(1)
    
    