
floor1=[True, True, True, True, True]
floor2=[True, True, True, True, True]
floor3=[True, True, True, True, True]
floor4=[True, True, True, True, True]
floor5=[True, True, True, True, True]





def Get_Slot_Number(floor, order):
        
        return floor * 100 + order;
     

def Is_Empty_Slot(slotNum): 
        order = slotNum % 10;
        floor = int(slotNum / 100)
        if (floor == 1):
            return floor1[order - 1]
        if (floor == 2):
            return floor2[order - 1]
        if (floor == 3):
            return floor3[order - 1]
        if (floor == 4):
            return floor4[order - 1]
        if (floor == 5):
            return floor5[order - 1]

def Remain_Slot(shape): 
        if (shape == 'truck'):
            return (Is_Empty_Slot(103) | Is_Empty_Slot(104)
                    | Is_Empty_Slot(105) | Is_Empty_Slot(203)
                    | Is_Empty_Slot(204) | Is_Empty_Slot(205)
                    | Is_Empty_Slot(303) | Is_Empty_Slot(304)
                    | Is_Empty_Slot(305) | Is_Empty_Slot(403)
                    | Is_Empty_Slot(404) | Is_Empty_Slot(405)
                    | Is_Empty_Slot(503) | Is_Empty_Slot(504)
                    | Is_Empty_Slot(505))

        if (shape == 'car'):
            return (Is_Empty_Slot(101) | Is_Empty_Slot(102)
                    | Is_Empty_Slot(201) | Is_Empty_Slot(202)
                    | Is_Empty_Slot(301) | Is_Empty_Slot(302)
                    | Is_Empty_Slot(401) | Is_Empty_Slot(402)
                    | Is_Empty_Slot(501) | Is_Empty_Slot(502))

def Slot_Left():
        i=0
        for f in floor1:
                if f:
                        i+=1
        for f in floor2:
                if f:
                        i+=1
        for f in floor3:
                if f:
                        i+=1
        for f in floor4:
                if f:
                        i+=1
        for f in floor5:
                if f:
                        i+=1
        return i


def Fill_Slot(floor, order):
        if (floor == 1):
            floor1[order - 1] = False;
        if (floor == 2):
            floor2[order - 1] = False;
        if (floor == 3):
            floor3[order - 1] = False;
        if (floor == 4):
            floor4[order - 1] = False;
        if (floor == 5):
            floor5[order - 1] = False;

def Release_Slot(slotNum): 
        order = slotNum % 10;
        floor = int(slotNum / 100);
        if (floor == 1):
            floor1[order - 1] = True;
        if (floor == 2):
            floor2[order - 1] = True;
        if (floor == 3):
            floor3[order - 1] = True;
        if (floor == 4):
            floor4[order - 1] = True;
        if (floor == 5):
            floor5[order - 1] = True;


def Assign_Slot(shape): 
        if (not Remain_Slot(shape)):
            return print('no more slot for ' + shape)
        else:
            for floor in range (1,6):
                if (shape == 'car'):
                    for order in range(1,3):
                        if (Is_Empty_Slot(Get_Slot_Number(floor, order))):
                            Fill_Slot(floor, order)
                            print ("Your slot number is: "+str(Get_Slot_Number(floor, order)))
                            
                            return Get_Slot_Number(floor, order)
                        
                elif (shape == 'truck'): 
                    for order in range(3,6):
                        if (Is_Empty_Slot(Get_Slot_Number(floor, order))):
                            Fill_Slot(floor, order)
                            print ("Your slot number is: "+str(Get_Slot_Number(floor, order)))
                            return Get_Slot_Number(floor, order)

