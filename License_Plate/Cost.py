
myCursorTime=0
def checkInterval (time, head, tail):
    return ((time >= head) and (time <= tail))
def interval1 (cursorTime):
    myCursorTime = 4.0
    time=4.0 - cursorTime
    return time,myCursorTime 
def interval2 (cursorTime):
    myCursorTime = 8.00
    time=8.00 - cursorTime
    return time,myCursorTime 
def interval3 (cursorTime):
    myCursorTime = 12.00
    time=12.00 - cursorTime 
    return time,myCursorTime  
def interval4 (cursorTime):
    myCursorTime = 16.00
    time=16.00 - cursorTime 
    return time,myCursorTime 
def interval5 (cursorTime):
    myCursorTime = 20.00
    time=20.00 - cursorTime 
    return time,myCursorTime 
def interval6 (cursorTime):
    myCursorTime = 24.00
    time=24.00 - cursorTime 
    return time , myCursorTime 

def getCost (startTime, endTime,p1,p2,p3,p4,p5,p6):

        start = int(startTime[0:2]) + int(startTime[3: 5]) / 60
        end = int(endTime[0:2]) + int(endTime[3:5]) / 60
        deltaTime = end - start
        totalCost = 0
        myCursorTime = start
        if (myCursorTime > 0.00 and myCursorTime <= 4.00): #interval1
            if (checkInterval(end, 0.00, 4.00)):
                totalCost += p1 * (end - myCursorTime)
                myCursorTime = end
                
            
            else:
                time,myCursorTime=interval2(myCursorTime)
                totalCost += p1 * time
                   
        if (myCursorTime >= 4.00 and myCursorTime <= 8.00): #interval2
            if (checkInterval(end, 4.00, 8.00)):
                totalCost += p2 * (end - myCursorTime)
                myCursorTime = end
                
            else:
                time,myCursorTime=interval2(myCursorTime)
                totalCost += p2 * time
        
        if (myCursorTime >= 8.00 and myCursorTime <= 12.00): #interval3
            if (checkInterval(end, 8.00, 12.00)):
                totalCost += p3 * (end - myCursorTime)
                myCursorTime = end;
            
            else:
                time,myCursorTime=interval3(myCursorTime)
                totalCost += p3 * time
        
        if (myCursorTime >= 12 and myCursorTime <= 16): #interval4
            if (checkInterval(end, 12, 16)):
                totalCost += p4 * (end - myCursorTime)
                myCursorTime = end
            else:
                time,myCursorTime=interval4(myCursorTime)
                totalCost += p4 * time
        
        if (myCursorTime >= 16 and myCursorTime <= 20):  #interval5
            if (checkInterval(end, 16, 20)):
                totalCost += p5 * (end - myCursorTime)
                myCursorTime = end;
            
            
            else:
                time,myCursorTime=interval5(myCursorTime)
                totalCost += p5 * time
                
        if (myCursorTime >= 20 and myCursorTime <= 24):#interval5
            if (checkInterval(end, 20, 24)):
                totalCost += p6 * (end - myCursorTime)
                myCursorTime = end
    
            else:
                time,myCursorTime=interval6(myCursorTime)
                totalCost += p6 * time
##.toPrecision(3);
        final = totalCost
        return float(final)

def getNormalCostByShape(shape, start, end):
    if (shape == 'car'):
        p1 = 1
        p2 = 1.25
        p3 = 2
        p4 = 2
        p5 = 2
        p6 = 1.5
        return getCost(start, end, p1, p2, p3, p4, p5, p6)


    if (shape == 'truck'): 
        p1 = 2.5
        p2 = 2.75
        p3 = 4
        p4 = 4
        p5 = 4
        p6 = 3.5
        return getCost(start, end, p1, p2, p3, p4, p5, p6)

def getWalkinCostByShape(shape, start, end):
    if (shape == 'car'):
        p1 = 2
        p2 = 2.5
        p3 = 3
        p4 = 3
        p5 = 2.75
        p6 = 2.25
        return getCost(start, end, p1, p2, p3, p4, p5, p6)
    
    if (shape == 'truck'):
        p1 = 5
        p2 = 5.5
        p3 = 6
        p4 = 6
        p5 = 5.25
        p6 = 4
        return getCost(start, end, p1, p2, p3, p4, p5, p6)

