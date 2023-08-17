#this generates some audio output in class 
import cv2,os
import numpy as np
from PIL import Image 
import pickle
import pyttsx3#for generating voice output
def mark():
	detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#using the frontal face classifier
	recognizer=cv2.face.LBPHFaceRecognizer_create()
	recognizer.read('trainer/trainer.yml')
	cascadePath="Classifiers/face.xml"
	faceCascade=cv2.CascadeClassifier(cascadePath);
	print "\n"
	path='images'
	image_paths=[os.path.join(path, f) for f in os.listdir(path)]
	print "File name",f
	dict1={1:'sasikaran',2:'karthik',3:'ganapathy'}#creating a sample dictionary for student data
	dict2={'sasikaran':0,'karthik':0,'ganapathy':0}#status of student presence
	for image in image_paths:
	    img=cv2.imread(image)
	    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
	    print(image)
	    for(x,y,w,h) in faces:
	        nbr_predicted,conf=recognizer.predict(gray[y:y+h,x:x+w])#it returns the id of data predicted and the confidence level or accuracy of prediction
	        print "id of predicted value",nbr_predicted,"Predicted range",100-conf#prints the prediction value for easy understanding
	        n=int(input("Proceed?"))#just a check to proceed with the next image
	        if n==1:
	        	print "validating status"
	        else:
	        	exit()
	        if 100-conf>50:#keeping the threshold of the value as 50.if the value become less than 50 it should not consider the prediciton id
	        	if nbr_predicted==1:
	        		dict2[dict1[nbr_predicted]]=1
	        	elif nbr_predicted==2:
	        		dict2[dict1[nbr_predicted]]=1
	        	elif nbr_predicted==3:
	        		dict2[dict1[nbr_predicted]]=1
	       	else:#if confidence level is low they will consider it as unauthorised person
	       		print("unauthorised")
	listpr=[]#just a sample list to store the student present in class
	listab=[]#just a sample list to store the student absent in class
	for i in dict2.keys():
		if dict2[i]==1:
			listpr.append(i)
		else:
			listab.append(i)
	print("\n************************Status*****************************")#displaying the status as command line
	print "Attendees    		:",listpr
	print "absentees				:",listab
	str1=''.join(listab)
	engine=pyttsx3.init()
	engine.say("The number of absentees in this period is"+str(len(listab)))#voice output of number of absenteed in class
	engine.say("Absentees are"+str1)#voice output of number of absentees in class
	engine.setProperty('rate',120)
	engine.setProperty('volume',0.9)
	engine.runAndWait()
	cv2.waitKey(10)
if __name__ == '__main__':
    mark()