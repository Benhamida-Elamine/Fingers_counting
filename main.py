import cv2
import matplotlib.pyplot as plt 
import os  
import time  
from Function import handDetector as htm 

wCam , hCam = 480 , 600
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)


path = "png" 
list =os.listdir(path)
print(list)
overlist = [] 
for impath in list : 
    image = cv2.imread(f'{path}/{impath}')
    
    
    if image is not None:  # Vérifiez que l'image a été chargée correctement
        # Redimensionner l'image à (200, 200)
        resized_image = cv2.resize(image, (200, 200))
        overlist.append(resized_image)
        
detector=htm.handDetector(detectionCon=0.75) 
finidx =[4,8,12,16,20]
print(len(overlist))
pTime=0
while True:
    ret, img = cap.read()  
    img=detector.findHands(img)
    
    
    cTime = time.time() 
    fps=1/(cTime-pTime)
    pTime= cTime
    cv2.putText(img,f'FPS : {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    
    lmlist= detector.findPosition(img,draw=False)
    
    if len(lmlist) != 0:
        fingers=[]
        if lmlist[finidx[0]][1]>lmlist[finidx[0]-1][1]:
                fingers.append(1)
        else: 
                fingers.append(0) 
        for idx in range(1,5):   
            if lmlist[finidx[idx]][2]<lmlist[finidx[idx]-2][2]:
                fingers.append(1)
            else: 
                fingers.append(0)
        
        
        totalfingers=fingers.count(1)
        
        
        # Determine if left or right hand
        wrist_x = lmlist[0][1]  # x-coordinate of the wrist (landmark 0)
        image_center_x = wCam / 2
        
        
        
        if wrist_x < image_center_x:
            hand_type = "Left Hand"
        else:
            hand_type = "Right Hand"
        
        
        
        print(f'Total Fingers: {totalfingers}, Hand Type: {hand_type}')
        
        # Display the total fingers and hand type
        cv2.putText(img, f'Fingers open: {totalfingers}', (300, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        cv2.putText(img, hand_type, (300, 150), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        
        img[0:200, 0:200] = overlist[totalfingers] 
        
        
        
        
     
        
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis('off')
    plt.pause(0.001)  
    plt.clf()  

    


cv2.waitKey(1)
