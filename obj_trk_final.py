import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture("footvolleyball.mp4")
#load tracker 
tracker = cv2.TrackerCSRT_create()

#read the first frame of the video
success,img = video.read()

#selct the bounding box on the image
bbox = cv2.selectROI("tracking",img,False)

#initialise the tracker on the img and the bounding box
tracker.init(img,bbox)

def goal_track(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)
    cv2.circle(img,(c1,c2),2,(0,0,255),5)

    cv2.circle(img,(int(p1),int(p2)),2,(0,255,0),3)
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(dist)

    if(dist<=20):
        cv2.putText(img,"Goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),2,(0,0,255),5)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)



while True:
   #Write the code inside loop here
   check,img=video.read()
   success,bbox=tracker.update(img)
   if success:
     drawBox(img,bbox)
   else:
       cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
   goal_track(img,bbox)
   cv2.imshow("result",img)
   cv2.waitKey(0)

video.release()
cv2.destroyALLwindows() 

