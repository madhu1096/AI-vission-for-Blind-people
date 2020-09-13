import cv2
import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
from imageai.Detection import ObjectDetection
#
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel(detection_speed="fastest")
#detector.loadModel()



def imgpreprocess(temp):

    detections = detector.detectObjectsFromImage(input_image="img1.jpg",
                                             output_image_path="6flash.jpg")
    if temp !=[]:
         if detections == []:        
            speak.Speak('Brace your self..')
            print('Watch your self..')
            print("--------------------------------")
            temp=[]

    
    for eachObject in detections:
        print(eachObject["name"] + " : " +str(eachObject["percentage_probability"]) )
        print("--------------------------------")        
        if temp != eachObject["name"]:
            pred = eachObject["name"].replace('_',' ')
            if eachObject["percentage_probability"] > 60:
                print(str(pred)+' is there')
                speak.Speak(str(pred)+' is there')
                speak.Speak('Turn left or right')
                temp = eachObject["name"]
    
            elif eachObject["percentage_probability"] > 40:
                
                print(str(pred))
                speak.Speak(str(pred)+'.. Go straight')
                
            elif eachObject["percentage_probability"] < 10:
                speak.Speak('Nothing.. Go straight')
    
    return temp
          
temp,label=' ',' '
while True:
    
    url = "**************************" # Your url might be different, check the app
    vs = cv2.VideoCapture(url+"/video")
    ret, frame = vs.read()
    cv2.imshow('Frame', frame)
    img_item = 'my-image.jpg'
    cv2.imwrite(img_item,frame)
    label = imgpreprocess(temp)
    temp=label
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break