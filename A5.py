###############################
# Assignment 3                #
# Name: Eric Fong             #
# UCID: 30087457              #
# Class: CPSC 217             #  
# Tutorial: 02                #  
###############################
#PROGRAM FUNCTION- The function of this program operates exactly like Conway's "Game of Life" except it includes a new
#function called fileRead, which essentially takes any file from user, inserts it into the program, reads it and 
#displays it into a 2D - list. This then allows for the critters in the file to live in a space of various sizes 
#but still follow the game rules of birth and death.
#PROGRAM LIMITATIONS- The limitations of this program that has been run into is that the program only opens a file with the
#limit of 50x50, and anything beyond is considered "Unable to open or processed." 
SIZE = 10
debugOn = False
CRITTER = "*"
EMPTY = " "
#Game of Life simulation
#Author:  James Tam
#Version: June 6, 2020
#This version of the program initializes the oldWorld (during the turn)
#and the newWorld (appearance of the world after the turn) as well as
#displaying the two versions side by side. Since the original state of
#the biosphere was empty the state of the new state is correct. However,
#no rules of births and deaths was applied in this version of the
#simulation.

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @oneEmpty()
  @Arguments: None
  @The biosphere is initialized to a completely empty state.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def oneEmpty():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @twoSingleCritter()
  @Arguments: None
  @The biosphere is empty except for one location which contains a 
  @Critter.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def twoSingleCritter():
    world = []
    world = [
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @threeSingleBirth()
  @Arguments: None
  @The biosphere is empty except for 3 locations which contain Critters.
  @The 3 Critters are all in proximity to a single location in the 
  @biosphere.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def threeSingleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " ","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @fourthSimpleBirth()
  @Arguments: None
  @The biosphere contains a number of Critters which are close enough
  @proximity to produce new births for a number of turns.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def fourthSimpleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", "*","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " ","*", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @fifthCreateListEdgeCases()
  @Arguments: None
  @The biosphere has a Critter located at the edge of the biosphere at
  @each of the 4 compass ponts. Also there is a Critter in each of the
  @corners.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def fifthCreateListEdgeCases():
    world = []
    world = [
     ["*"," ", "*"," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", "*", " "],
     ["*","*", " "," ", " ", " ", " ", " ", " ", "*"]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @sixthComplexCases()
  @Arguments: None
  @The biosphere contains a starting pattern that will require a 
  @program to handle births, deaths and edge cases. 
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def sixthComplexCases():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", "*", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", "*", " ", " ", " ", " "],
     [" "," ", " ","*", "*", "*", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# @ This function works in conjunction with readFromFile()
# @intialize()
# @Argument: None
# @Return value: the game world in the form of a 2D list (each element
# @is set to an exclamation mark).
# '''
def initialize():
    world = []                  
    for r in range (0, SIZE, 1):   
        world.append ([])       
        for c in range (0, SIZE, 1): 
            world[r].append ("!")
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# @display()
# @Argument: two references to the 2D list which is game world.
# @The list must be already created and properly initialized
# @prior to calling this function!
# @Return value: None
# @Displays each element of the world with each row all on one line
# @Each element is bound: above, left, right and below with a bar (to
# @make elements easier to see.
# @Each list is displayed side by side
# <Old list>#<TAB><New list>
# '''
def copy(world):
    temp=[]
    for r in range(0,SIZE,1):
        temp.append([])
        for c in range(0,SIZE,1):
            temp[r].append(world[r][c])
    return(temp)
def critterBirth(row,column,count,newWorld):
    if (count == 3):
        newWorld[row][column] = CRITTER
        if (debugOn == True):
            print("<<<Critter born at %d/%d>>>" %(row, column))
def critterDeath(row,column,count,newWorld):
    if ((count <=1) or (count>=4)):
        newWorld[row][column] = EMPTY
        if (debugOn == True):
            print("<<<Critter death at %d/%d>>>" %(row,column))
def display(turn,oldWorld,newWorld):
    # Displays a row at a time of each list
    print("Turn #%d" %turn)
    print("BEFORE\t\t\tAFTER")
    for r in range (0,SIZE,1):

        # Row of dashes before each row of old and new list
        # (Dashes for old list)
        for i in range (0, SIZE, 1): 
            print("%s" %(" -"), end="")
        print("#\t",end="")
        # (Dashes for new list)
        for i in range (0, SIZE, 1): 
            print("%s" %(" -"), end="")
        print()

        # Display one row of old world list
        for c in range (0,SIZE,1):
            # Display: A vertical bar and then element (old list) 
            print("|%s" %(oldWorld[r][c]), end = "")
        # Separate the lists with a number sign and a tab
        print("", end = "#\t")    

        # Display one row of new world list
        for c in range (0,SIZE,1):
            # Display: A vertical bar and then element (new list) 
            print("|%s" %(newWorld[r][c]), end = "")
        print("|")

    # Row of dashes after end of last row (old world list)
    for i in range (0, SIZE, 1): 
        print("%s" %(" -"), end="")
    print("#\t",end="")

    # Row of dashes after end of each row (new world list)
    for i in range (0, SIZE, 1): 
        print("%s" %(" -"), end="")
    print()
def displaySelectionMenu():
    print("""
Choices for starting biospheres
  (1) Empty
  (2) Single critter
  (3) Single birth
  (4) Simple birth
  (5) Edgey testing
  (6) It's a complex world
""")
def inBounds(row,column):
    bounds = True
    if ((row<0) or (row >= SIZE) or
        (column<0) or (column >= SIZE)):
          bounds = False
    return(bounds)
def isCritter(row,column,world):
    critter = False
    if (world[row][column] == CRITTER):
        critter = True
    return(critter)
def processSelection():
    selection = -1
    world = []
    while selection not in (1,2,3,4,5,6):
        displaySelectionMenu()
        selection=int(input("Selection: "))
    if (selection ==1):
        world = oneEmpty()
    elif (selection ==2):
        world = twoSingleCritter()
    elif (selection ==3):
        world = threeSingleBirth()
    elif (selection ==4):
        world = fourthSimpleBirth()
    elif (selection ==5):
        world = fifthCreateListEdgeCases()
    elif (selection ==6):
        world = sixthComplexCases()
    return(world)
def scan(oldWorld, newWorld):
    for r in range(0,SIZE,1):
        for c in range(0,SIZE,1):
            count=0
            r1 = r-1
            if (debugOn == True):
                print("Counting for the 'After' case")
                print("(ROW,COL): %d/%d" %(r,c))
            while (r1 <= (r+1)):
                c1 = c-1
                while(c1 <= (c+1)):
                    if (debugOn == True):
                        print("(row,col): %d/%d" %(r1,c1))
                    if (inBounds(r1,c1) == True):
                        if (isCritter(r1,c1,oldWorld) == True):
                            count = count + 1
                    c1 = c1+1
                r1 = r1 + 1
                if (isCritter(r,c,oldWorld)== True):
                    count = count - 1
                    critterDeath(r,c,count,newWorld)
                else:
                    critterBirth(r,c,count,newWorld)

                if (debugOn == True):
                    print("ROW/COL %d/%d count=%d" %(r,c,count))
                    print("###")
def toggleDebug():
    global debugOn
    if (debugOn == True):
        print("<<< DEBUG messages OFF! >>>")
        debugOn = False
    else:
        print("<<< DEBUG messages ON! >>>")
        debugOn = True
NEWLINE = "\n"
SPACE = " "
#Function fileRead() checks for the file to see whether or not the file is capable of running, and if the file is
#not corrupt or accesible then the program will read this file. Basically it checks the file, if it meets the guidelines/
#program checklist, it will read the file.
def fileRead():
	fileOK = False
	char= []


	while(fileOK == False):
		
		try:
			filename = input("Name of input file: ")
			inputfile = open(filename, "r")
			fileOK = True
			aLine = inputfile.readline()

			if(aLine == ""):
				print("%s is an empty file" %filename)
			
			else:
				aLine = inputfile.readline()
				currentRow = 0
			
				while(len(aLine) > 0):
					currentCharacter = 0
					char.append([])
			
					while(aLine[currentCharacter] != NEWLINE):
						if(aLine[currentCharacter] != SPACE):
							char[currentRow].append(aLine[currentCharacter])
			
						currentCharacter = currentCharacter + 1
			
					currentRow = currentRow + 1
					aLine = inputfile.readline()
			
				inputfile.close()
		
		except IOError:
			print("Problem reading from file %s" %filename)
			fileOK = False

	numRows = currentRow
	numColumns = len(char[0])

	return (char, numRows, numColumns)


#################################################################
# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
def start():
    choice = ""
    world = []
    turn = 0
    fileRead()
    while ((choice!= "q") and (choice!= "Q")):
        choice = input("Hit enter to continue ('q' to quit): ")
        if ((choice == "d") or (choice == "D")):
            toggleDebug()
        turn = turn +1
start()

