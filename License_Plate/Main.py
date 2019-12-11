import cv2
import os
from Enter import *
from DetectBlacklisted import Detect_Blacklisted
from ShapeDetection import detect_shape
from ALPR import Take_License

h=[]

path='E:/RUTGERS/SEM1_2019-2020/SoftWareEngineering/Software_Project_G4-master/License_Plate/Images/'
for i in range(1,7):
                h.append(path+str(i)+".jpg")


def main():
        
    while True:
        
        Enter=input('''To print email : press 1Check License Plate: press 2 or Check The Shape: press 3 ''')
        
        if Enter=='1':
            for i in h:
                currentcustomer=cv2.imread(i)
                cv2.imwrite(os.path.join(path,'images_enter.png'),currentcustomer)
                images_enter = path+'images_enter.png' 
                enter_customer_plate=Take_License(images_enter)
                print(enter_customer_plate)
                Check_Enter(enter_customer_plate,images_enter)
        elif Enter=='2':
            for i in h:
                currentcustomer=cv2.imread(i)
                cv2.imwrite(os.path.join(path,'images_enter.png'),currentcustomer)
                currentimage= path+'images_enter.png'
                current_customer_plate=Take_License(currentimage)
                print(current_customer_plate)
                Detect_Blacklisted(current_customer_plate)
        elif Enter=='3':
            detect_shape(path+'1.jpg')
            detect_shape(path+'7.jpg')
            detect_shape(path+'8.jpg')
            detect_shape(path+'12.jpg')

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
 
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
