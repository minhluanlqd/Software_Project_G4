import cv2
import os
import pymongo
from ShapeDetection import detect_shape
from Exit import Check_Exit
from Enter import Check_Enter
from ALPR import Take_License
from SendEmailReserves import Send_Email_Reserve
#test camera
cam_enter = cv2.VideoCapture('C:/Users/Kel Nguyen/Desktop/Python/Garage/License_Plate/test.mp4')
cam_exit=cv2.VideoCapture('C:/Users/Kel Nguyen/Desktop/Python/Garage/License_Plate/test1.mp4')

#database
connection= pymongo.MongoClient("mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority")
database=connection['parkinglot']
collection=database['garage']

#count
countdata=collection.count()
print (countdata)
def main():
    
    #enter list
    enter_list=[]
    exit_list=[]
    
    #XML classifier
    car_cascade = cv2.CascadeClassifier('cars.xml')
    
    #Path to take each photo,frames/sec on video
    path='C:/Users/Kel Nguyen/Desktop/Python/Garage/License_Plate/Images/'
    while True:
        try:
            ret, frames_enter = cam_enter.read()
        except:
            frames_enter=None

        try:
            ret, frames_exit = cam_exit.read()
        except:
            frames_enter=None

        #New reservation,send email
        if collection.count()>countdata:
            countdata=collection.count
            for i in collection.find({},{'Time_start':1,'Time_end':1,'Cost':1,
                                         'Email':1,'ID':1}).sort('ID',-1):
                Send_Email_Reserve(i['Email'],i['Cost'],i['Time_start'],i['Time_end'])
                break
         
        #Check when customer enters
        if frames_enter is not None:
            gray_enter = cv2.cvtColor(frames_enter, cv2.COLOR_BGR2GRAY)

            #
            cv2.imwrite(os.path.join(path,'images_enter.png'),frames_enter)
            images_enter = path+'images_enter.png'
            
            #Take the customer license plate when enters
            enter_customer_plate=Take_License(images_enter)

            if (enter_customer_plate not in enter_list):
                enter_list.append(enter_customer_plate)
                print(enter_customer_plate)
                Check_Enter(enter_customer_plate,images_enter)

        
            cv2.imshow('CustomerEnter', frames_enter)
            
        #Check when customer exits
        if frames_exit is not None:
            gray_exit = cv2.cvtColor(frames_exit, cv2.COLOR_BGR2GRAY)

        
            #
            cv2.imwrite(os.path.join(path,'images_exit.png'),frames_exit)
            images_exit = path+'images_exit.png'

            #Take the customer license plate when exits
            exit_customer_plate=Take_License(images_exit)
            
            if (exit_customer_plate not in exit_list):
                exit_list.append(exit_customer_plate)
                print(exit_customer_plate)
                Check_Exit(exit_customer_plate,images_exit)

                
            cv2.imshow('CustomerExit', frames_exit)
        

        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
 
    cv2.destroyAllWindows()
    cam_enter.release()
    cam_exit.release()

if __name__=="__main__":
    main()
