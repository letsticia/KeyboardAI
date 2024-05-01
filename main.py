import cv2
from cvzone.HandTrackingModule import HandDetector
from button import buttonList
import time
from pynput.keyboard import Controller

final_text = ""

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
                click = button.click(lenght, frame, final_text)
                
                if click and (time.time() - last_click_time) > cooldown:
                    final_text = click
                    last_click_time = time.time()
                    Controller().press(key=button.text)
                
                
                cv2.rectangle(frame, (50, 420), (700, 550), (175, 0, 175), cv2.FILLED)
                cv2.putText(frame, final_text, (68, 525), 
                            cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 4)
    
    if frame is None:
        continue
    
    cv2.imshow('Video', frame)
    cv2.waitKey(1)
    
    