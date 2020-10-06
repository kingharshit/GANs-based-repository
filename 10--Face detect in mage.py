import cv2
import numpy
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #for detecting face
eye = cv2.CascadeClassifier('haarcascade_eye.xml') #for detecting eyes

image=cv2.imread("a.jpg")
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert into gray so color not effect accuracy


faces = face.detectMultiScale(gray,1.3,5)   #for multiple faces

if faces is ():
    print("no face")
    
for(x,y,w,h) in faces:
    
    image=cv2.rectangle(image,(x,y),(x+w,y+w),(127,0,205),3)
cv2.imshow("Face Detected",image)
cv2.waitKey(0)
cv2.destroyAllWindows()    
