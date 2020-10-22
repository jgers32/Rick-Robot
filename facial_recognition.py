#IMPORTANT:this is not my code...it was pulled so I could help my own code livestream facial recognition.

import io
import picamera
import cv2
import numpy

#create a memory stream so photos don't need to be saved in a file
stream = io.BytesIO()

#get the pic (low res, will be quite fast)
#here you can also specify other parameters (like rotating the image)
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')
    
#convert the pic into numpy array
buff = numpy.frombuffer(stream.getvalue(), dtype=numpy.uint8)

#now creates an OpenCV image
image = cv2.imdecode(buff, 1)

#https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcasade_frontalface_default.xml
#load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print ("Found {}" + str(len(faces)) + "face(s)")

#draw a rectangle around every found face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),4)
    
#save the image result
cv2.imwrite('result.jpg',image)

"""
#showing the photo
im = image.open('result.jpg')
im.show()

"""
