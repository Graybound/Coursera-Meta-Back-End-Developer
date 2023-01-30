import numpy as np
import math
import time

startTime = time.perf_counter()
iterations = 0

print('**************\n', 'Tower of Hanoi\n', '**************')


class Disk:
    def __init__(self, num, size, location, position):
        self.num = num
        self.size = size
        self.location = location
        self.position = position


def timer():
    ct = time.perf_counter()
    return round(ct-startTime+waitTime, 3)


def timeConstraint():
    timeOut = 600
    if timer() > timeOut:
        print('Timeout Error. ', timeOut, ' sec')
        quit()
    return timer


def initialize(numOfDisks):
    tempTowerMatrix = [[0]*numOfDisks, [0]*numOfDisks,
                       [0]*numOfDisks]  # np.zeros((3, numOfDisks), int)
    num = 1
    iDiskList = {}
    iDiskList[0] = ['disk number', 'size',
                    'location', 'position']
    while num < numOfDisks + 1:
        if num > numOfDisks + 1:
            break
        else:
            # Create disk
            d = Disk(num, num, 1, num)
            # Add new disk to list
            iDiskList[num] = [d.num, d.size, d.location, d.position]
            # Create towerMatrix
            tempTowerMatrix[0][num-1] = d.num
            tempTowerMatrix[1][num-1] = 0
            tempTowerMatrix[2][num-1] = 0
            num += 1
    return (iDiskList, tempTowerMatrix)


def checkSize(d1, d2, d3, dOldMoveFrom, dOldMoveTo):
    dMax = max(d1, d2, d3)
    dMin = min(d1, d2, d3)
    Min = 0

    """ if d2 and d3 == 0:
        moveFrom = 0
        moveTo = 2
        moveNot = 1
        return moveFrom,moveTo,moveNot """

    if d3 == dMax:
        moveTo = 2
    elif d2 == dMax:
        moveTo = 1
    else:
        moveTo = 0

    if d1 == dMin:
        Min = 0
    elif d2 == dMin:
        Min = 1
    else:
        Min = 2

    if ((moveTo == 2) and (Min == 1)):
        moveFrom = 0
    elif ((moveTo == 0) and (Min == 2)):
        moveFrom = 1
    else:
        moveFrom = 2

    if (dMin == 0):
        moveNot = moveTo
        moveTo = Min
        return moveFrom, moveTo, moveNot
    elif ((dOldMoveFrom != moveTo)):
        moveNot = Min
        return moveFrom, moveTo, moveNot
    # Checks to make sure it is not repeating it self
    elif ((dOldMoveFrom == moveTo) and (dOldMoveTo != Min)):
        moveNot = moveFrom
        moveFrom = Min
        return moveFrom, moveTo, moveNot
    else:
        print('Tower Looping Error.')
        quit()

    # return moveFrom, moveTo, Min  # disk will move to largest disk or Min to the middle


def checkState(towerMatrix, sum):
    checkSum = np.sum(towerMatrix)
    if checkSum == sum:
        return True
    else:
        return False


def hanoi(numOfDisks):
    temp = initialize(numOfDisks)
    diskList = temp[0]
    TM = temp[1]
    TM1 = TM
    sum = np.sum(TM[0])

    try:

        # Check if disks are on tower 3
        if checkState(TM[2], sum) == True:
            return TM
        else:
            moveFrom = 5
            moveTo = 5
            while checkState(TM[2], sum) == False:
                timer = timeConstraint()
                check = checkSize(int(TM[0][0]), int(
                    TM[1][0]), int(TM[2][0]), moveFrom, moveTo)
                moveFrom = int(check[0])
                moveTo = int(check[1])
                moveNot = int(check[2])
                if ((TM[1][0] == 0) and (TM[2][0] == 0)):
                    moveNot = 1
                    moveTo = 2
                    moveFrom = 0
                    diskID = TM[moveFrom][0]
                elif (TM[2][0] == 0):
                    moveFrom = 0
                    moveNot = moveTo
                    moveTo = 2
                    diskID = TM[moveFrom][0]
                elif ((TM[1][0] == 0)):
                    moveNot = 2
                    moveTo = 1
                    moveFrom = 0
                    diskID = TM[moveFrom][0]
                else:
                    diskID = TM[moveFrom][0]
                tmf = list(TM[moveFrom][1:numOfDisks+1])  # Tower moved from
                tmt = list(TM[moveTo][0:numOfDisks-1])  # Tower moved to
                tmn = list(TM[moveNot][:])  # Tower un-touched
                tmf = list(np.append(tmf, 0))
                tmt = list(np.insert(tmt, 0, diskID))
                tmt = list(tmt[0:numOfDisks])
                # creates a matrix and assigns the rows appropriately
                TM1[moveFrom] = tmf
                TM1[moveTo] = tmt
                TM1[moveNot] = tmn
                TM = TM1
                """
                TM[[move, Max], [0, 0]] = some_array[[3, 0], [0, 0]]
                """
            # print('Finished in: ',timer, ' seconds')
                print('Results: \n', TM)
        return TM

    except Exception as e:
        print('Error: ', e)


n = int(input('Enter the number of disks:\n'))
waitTime = time.perf_counter() - startTime
# result = initialize(n)
towerMatrix = hanoi(n)

# print('Results:')
# print('Tower 1: \n', towerMatrix[0], '\nTower 2: \n',towerMatrix[1], '\nTower 3: \n', towerMatrix[2])


endTime = time.perf_counter()
timed = round(endTime-startTime-waitTime, 3)
print(timed, 'sec')
