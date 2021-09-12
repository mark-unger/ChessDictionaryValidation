#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#if given a board with a premade dictionary
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "6d":"wbishop", '3d':'brook'}

boardKeys = []
boardValues = []
chessPieces = ['bking', 'wking', 'bqueen', 'wqueen', 'bknight', 'wknight', 'bbishop', 'wbishop', 'brook', 'wrook', 'bpawn', 'wpawn']




possibleBoardPositions = []
number = [ 1,2,3,4,5,6,7,8]
letter = ['a','b','c','d','e','f','g','h']


# makes the possible board positions and places them into a list to be compared to later
for i in number:
    for j in range(len(letter)):
        possibleBoardPositions.append(str(number[i-1]) + letter[j])
       

    
#Counts the pieces and manipulates them in a list to count them
def CountPieces():
    
    bkingCount = 0
    wkingCount = 0
    bqueenCount = 0
    wqueenCount = 0
    bbishopCount = 0
    wbishopCount = 0
    brookCount = 0
    wrookCount = 0
    bknightCount = 0
    wknightCount = 0 
    bpawnCount = 0
    wpawnCount = 0
    trueOrFalsePieces = True
    
    # gathers the piece name
    for v in board.values():
        boardValues.append(v)




    while 'bking' in boardValues:
        bkingCount += 1
        boardValues.remove('bking')
   
    
    
    while 'wking' in boardValues:
        wkingCount += 1
        boardValues.remove('wking')
   
    
            
    while 'bqueen' in boardValues:
        bqueenCount += 1
        boardValues.remove('bqueen')
   
    
                    
    while 'wqueen' in boardValues:
        wqueenCount += 1
        boardValues.remove('wqueen')
    
    
    while 'wqueen' in boardValues:
        wqueenCount += 1
        boardValues.remove('wqueen')
   

    while 'bbishop' in boardValues:
        bbishopCount += 1
        boardValues.remove('bbishop')
    

    while 'wbishop' in boardValues:
        wbishopCount += 1
        boardValues.remove('wbishop')
      
    
   #checks if there are valid numbers of pieces on the board 
    
    if bkingCount > 1:   
        trueOrFalsePieces = False

    if wkingCount > 1:     
        trueOrFalsePieces = False
        
    if bqueenCount > 1:    
        trueOrFalsePieces = False
        
    if wqueenCount > 1:      
        trueOrFalsePieces = False
        
    if bbishopCount > 2:     
        trueOrFalsePieces = False
        
    if wbishopCount > 2:
        trueOrFalsePieces = False
    
    if trueOrFalsePieces == False:
        return False
    else:
        return True
    
 

    
def BoardPositions():
    
#gathers the piece positions and checks if they're valid
    
    trueOrFalsePositions = True
    for k in board.keys():
        boardKeys.append(k)
    
    for i in boardKeys:
        if i not in possibleBoardPositions:
            trueOrFalsePositions = False
    if trueOrFalsePositions == False:
        return False
    else: 
        return True
           
      


    
    
#Tells us if valid or not   
def IsValid(x,y):
    if x == True & y == True:
        print("This is a valid board")
    else:
        print ('This is not a valid board')
     
        

IsValid(CountPieces(),BoardPositions())


        

    

