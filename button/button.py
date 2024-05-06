import cv2

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size
        
        
    def draw(self, frame):
        
        if self.text == "SPACE":
            self.size = [300, 85]
            self.pos = [100, 400]
           
        if self.text == "DEL":
            self.size = [200, 85]
            self.pos = [480, 400]
        
        if self.text == "QUIT":
            self.size = [200, 85]
            self.pos = [780, 400]
  
        x, y = self.pos
        w, h = self.size
        
        cv2.rectangle(frame, self.pos, (x+w, y+h), RETANGLE_COLOR, cv2.FILLED)
        cv2.putText(frame, self.text, (x+20, y+65), 
                    cv2.FONT_HERSHEY_PLAIN, 4, TEXT_COLOR, 4)
 
        return frame
    
    def isOver(self, lmList, frame):
        x, y = self.pos
        w, h = self.size
        
        if x < lmList[8][0] < x+w and y < lmList[8][1] < y+h:
            cv2.rectangle(frame, self.pos, (x+w, y+h), OVER_COLOR, cv2.FILLED)
            cv2.putText(frame, self.text, (x+20, y+65), 
                        cv2.FONT_HERSHEY_PLAIN, 4, TEXT_COLOR, 4)
            return True
    
    def click(self, lenght, frame):
        x, y = self.pos
        w, h = self.size
        
        if lenght < 25: 
            cv2.rectangle(frame, self.pos, (x+w, y+h), CLICK_COLOR, cv2.FILLED)
            cv2.putText(frame, self.text, (x+20, y+65), 
                        cv2.FONT_HERSHEY_PLAIN, 4, TEXT_COLOR, 4)
            
            if self.text =="QUIT":
                cv2.destroyAllWindows()
                exit()
            
            return True
      
            
    
buttonList = []

RETANGLE_COLOR = (255, 0, 255)
TEXT_COLOR = (255, 255, 255)
OVER_COLOR = (175, 0, 175)
CLICK_COLOR = (0, 255, 0)
POS = (100, 100)


keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        ["SPACE", "DEL", "QUIT"]]

for row in range(len(keys)):
    for numkey, key in enumerate(keys[row]):
        buttonList.append(Button([100+ numkey*POS[0], 100 + row*POS[1]], key))