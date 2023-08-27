import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np



width,height = 1280,720 
cap = cv2.VideoCapture(0)
cap.set(10,width)
cap.set(10,height)

folderpath = "present"

pathImages = os.listdir(folderpath)
#print(pathImages)

hs,ws = int(120*1),int(200*1)

detector = HandDetector(detectionCon=0.8,maxHands=2)


#variable 
imgnum  = 0
gestureThreshold = 450
buttonpressed = False
pressedCounter = 0
buttondelay = 15
annote_list = []
annote_num = -1
annote_start = False   #annotation list

while True:
    success,img = cap.read()
    img  = cv2.flip(img,1)
    pathFullImage = os.path.join(folderpath,pathImages[imgnum])
    imgCurrent = cv2.imread(pathFullImage)

   #resize the img 

    hands, img  = detector.findHands(img,flipType=False)
    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)
    
    if hands and buttonpressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx,cy = hand['center']
        lmlist = hand['lmList']   #landmark of fingers
        
        indexfinger = lmlist[8][0],lmlist[8][1]

        if cy <= gestureThreshold:
            #gesture-1 left

            if fingers == [1, 0, 0, 0, 0]:
              #  print("left") 
               if imgnum > 0:
                buttonpressed = True
                annote_list = []
                annote_num = -1
                annote_start = False
                imgnum -= 1


             #gesture-1 right 
            if fingers == [0, 0, 0, 0, 1]:
             #   print("Right")     
                if imgnum < len(pathImages)-1:
                    buttonpressed = True
                    annote_list = []
                    annote_num = -1
                    annote_start = False
                    imgnum += 1



        #gesture for pointer 
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent,indexfinger,10,(0, 0, 255),cv2.FILLED)
            annote_start = False


            #gesture for drawing
        if fingers == [0, 1, 0, 0, 0]:
            if annote_start is False:
                annote_start = True
                annote_num += 1
                annote_list.append([])

            cv2.circle(imgCurrent,indexfinger,8,(0, 0, 255),cv2.FILLED)
            annote_list[annote_num].append(indexfinger)

        else:
            annote_start = False  


       # Gesture for erase
        if fingers == [0, 1, 1, 1, 0]:
            if annote_list:
                annote_list.pop(-1)
                annote_num -= 1
                buttonpressed = True
        
    else:
        annote_start = False

    #buttonpressed itteration
    if buttonpressed:
        pressedCounter += 1
        if pressedCounter > buttondelay:
            pressedCounter = 0 
            buttonpressed = False
    

    for i in range(len(annote_list)):
        for j in range(len(annote_list[i])):
         if j!= 0:
              cv2.line(imgCurrent,annote_list[i][j-1],annote_list[i][j],(0, 0, 200),6)


    Small_img = cv2.resize(img,(ws,hs))
    h, w, _ = imgCurrent.shape 
    imgCurrent[0:hs,w - ws:w] = Small_img

    cv2.imshow("image",img)
    cv2.imshow("Slides",imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
       break