import cv2
import os
from ShapeDetection import detect_shape
from Exit import Check_Exit
from Enter import Check_Enter
from ALPR import Take_License

#test camera
##cam_enter = cv2.VideoCapture('C:/Users/Kel Nguyen/Desktop/Python/Garage/License_Plate/test.mp4')
##cam_exit=cv2.VideoCapture('C:/Users/Kel Nguyen/Desktop/Python/Garage/License_Plate/test1.mp4')

#test image
h=[]
path='C:/Users/Kel Nguyen/Desktop/Python/Garage/License_Plate/Images/'
for i in range(1,7):
    h.append(path+str(i)+".jpg")
    

def main():
    
    #enter list
    enter_list=[]
    exit_list=[]
    
    #XML classifier
    car_cascade = cv2.CascadeClassifier('cars.xml')
    
    #Path to take each photo,frames/sec on video
    while True:
        Enter='1'
        Enter=input('If you want to check when customer enters,press 1 or press 2 to check when customer exits: ')
        print(Enter)
        if Enter=='1':
            f=0
            for i in h:
                currentcustomer=cv2.imread(i)
                #Check when customer enters
                gray_enter = cv2.cvtColor(currentcustomer, cv2.COLOR_BGR2GRAY)

                #
                cv2.imwrite(os.path.join(path,'images_enter.png'),currentcustomer)
                images_enter = path+'images_enter.png'
            
                #Take the customer license plate when enters
                enter_customer_plate=Take_License(images_enter)

##                if (enter_customer_plate not in enter_list):
##                    enter_list.append(enter_customer_plate)
                print(enter_customer_plate)
                Check_Enter(enter_customer_plate,images_enter)
                f=f+1
        elif Enter=='2':
            f=0
            print(f)
            for i in h:
                currentcustomer=cv2.imread(i)
                #Check when customer exit
                cv2.imwrite(os.path.join(path,'images_exit.png'),currentcustomer)
                images_exit = path+'images_exit.png'

                #Take the customer license plate when exits
                exit_customer_plate=Take_License(images_exit)
            
##                if (exit_customer_plate not in exit_list):
##                    exit_list.append(exit_customer_plate)
                print(exit_customer_plate)
                Check_Exit(exit_customer_plate)
            

        

        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
 
    cv2.destroyAllWindows()
##    cam_enter.release()
##    cam_exit.release()

if __name__=="__main__":
    main()
