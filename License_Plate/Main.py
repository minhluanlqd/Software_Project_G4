import cv2
import os
from ShapeDetection import detect_shape
from Exit import Check_Exit
from Enter import Check_Enter
from ALPR import Take_License


def main():
    #enter list
    enter_list=[]
    
    #test camera
    cam_enter = cv2.VideoCapture('test.mp4')
    cam_exit=cv2.VideoCapture('test.mp4')

    #XML classifier
    car_cascade = cv2.CascadeClassifier('cars.xml')
    
    #Path to take each photo,frames/sec on video
    path='C:/Users/Kel Nguyen/Desktop/Python/Garage/License_Plate/Images/'
    while True:
    
        ret, frames_enter = cam_enter.read()
        ret, frames_exit = cam_exit.read()
    
        gray_enter = cv2.cvtColor(frames_enter, cv2.COLOR_BGR2GRAY)
        gray_exit = cv2.cvtColor(frames_exit, cv2.COLOR_BGR2GRAY)

        #
        cv2.imwrite(os.path.join(path,'images_enter.png'),frames_enter)
        images_enter = path+'images_enter.png'
        #
        cv2.imwrite(os.path.join(path,'images_exit.png'),frames_exit)
        images_exit = path+'images_exit.png'
        #Take the customer license plate when enters
        enter_customer_plate=Take_License(images_enter)
        exit_customer_plate=Take_License(images_exit)
     
      

       
        if (enter_customer_plate in enter_list):
            continue
        else:
            enter_list.append(enter_customer_plate)
            print(enter_customer_plate)
            Check_Enter(enter_customer_plate,images_enter)

        
        cv2.imshow('video2', frames_enter)
        cv2.imshow('video2', frames_exit)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
 
    cv2.destroyAllWindows()
    cam_enter.release()
    cam_exit.release()
if __name__=="__main__":
    main()
