# Recursion example: Tower of Hanoi
---
## Objective and rules of the puzzle:
### *The objective is to move n number of disks from tower 1 to tower 3 following a set of rules. These rules are as follows:*
1. Only one disk can be moved at a time
2. Only the upper disk of any of the towers can be moved
3. Larger disks cannot be placed over smaller disks
---
## Basic approach to requirements
1. Only one disk can be moved at a time
    
    - no async functions and no more than 1 move per operation
2. Only the upper disk of any of the towers can be moved 

    - Create value that stores current tower and vertical position
3. Larger disks cannot be placed over smaller disks

    - Create value to store size of disk

___
## Attack Plan
1. Start with making a disk dictionary with keys:         {diskNum:, towerNum:, posNum:, size:}.
2. Create 3 lists or a matrix for the towers that is a reference for disk location.
3. Create a function to generateDiskList(# of disks).
    1. Create for loop to initialize disks.
        1. diskNum = idx
        4. size = diskNum (redundant for better understanding)
        2. location = 1 (ie. tower 1)
        3. position = idx (this will not remain = to idx, only for initialization)
    2. Return diskList, towerMatrix
4. Create function (hanoi) that calls itself to move the disks from one tower to another until all disks are on tower 3.
    1. Call generateDiskList(n). (returns diskList & towerMatrix)
    2. Find way to have disks prefer to move right (towards tower 3).
    3. Check that the 'top' disk on the newTower is not smaller than selected disk.
    4. Update the disks location.
    5. Function returns the towerMatrix storing disk locations.
5. Main code:
    1. Ask user for the number of disks (n).
    2. Call hanoi(n)
    3. Print('Tower 1:\n', towerMatrix[0]) for all 3 towers
