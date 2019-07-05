from tkinter import *
import cv2
import boto3
from tkinter import filedialog
import boto3
from ctypes import *
from tkinter import messagebox

from tkinter import messagebox
def Camera():
    cam = cv2.VideoCapture(0)  # Camera Function
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    sampleNum = 0  # Create the dataset of employees
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the colored image into gray
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder
            cv2.imwrite("dataSet/User." + "DY" + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

            cv2.imshow('frame', img)
            # wait for 100 miliseconds
        if cv2.waitKey(100) == ord('q'):
            break;

        elif sampleNum > 1:
            break;
    cam.release()
    messagebox.showinfo("Image Captured")
    cv2.destroyAllWindows()


def CalculateEmotion():
    imageFile = 'dataSet/User.DY.1.jpg'

    client = boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])

        b=0

        for emotion in response['FaceDetails']:

            for sentiment in emotion['Emotions']:

             # print(sentiment['Confidence'])
            #  print(sentiment['Type'])
               a=sentiment['Confidence']

               if b<a:
                  b=a
                  c = sentiment['Type']

            print(b)
            print(c)
                    #for i in range (4):

             #print('With the confidence of ' + str(sentiment['Confidence']))
             #print('The Emotion of face is ' + str(sentiment['Type']))

                #print(type(sentiment['Confidence']))
                #new = [[i] for i in sentiment['Confidence']]
                #print(new)

                #for A in sentiment['Confidence']:



                # for i in range(6):
                # print(sentiment)
               # if (sentiment['Confidence']):
                    #print(sentiment['Confidence'])
                   # A=sentiment['Confidence']
                   # new = [[i] for i in A]


                   # a = float(sentiment['Confidence'])

                    #messagebox.showinfo('The Emotion of face is ' + str(sentiment['Type']))



root = Tk()

b3 = Button(root, text="Create Dataset", command=Camera)
b4 = Button(root,text="Know Emotion", command=CalculateEmotion)
b3.pack()
b4.pack()
root.mainloop()



