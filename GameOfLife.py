import pygame, sys, random
from pygame.locals import *

#Set size of grid
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10

#Number of cells per dimensions
CELLWIDTH = WINDOWWIDTH / CELLSIZE 
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE 

#Set up the colours
BLACK    = (0,  0,  0)
WHITE    = (255,255,255)
DARKGRAY = (40, 40, 40)
GREEN    = (0,255,0)

#Set n. of frames
FPS = 10

#Draw the grid lines
def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH, y))

#Colour the cells green for life and white for no life
def colourGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE #translates array index to y coord
    x = x * CELLSIZE #translates array index to x coord
    if lifeDict[item] == 0:
        pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELLSIZE, CELLSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, CELLSIZE, CELLSIZE))
    return None

#Create a dictionary of all the cells
def blankGrid():
    gridDict = {}
    for y in range(int(CELLHEIGHT)):
        for x in range(int(CELLWIDTH)):
            gridDict[x,y] = 0 #Set all cells as dead
    return gridDict

#Assign a 0 or a 1 to all cells
def startingGridRandom(lifeDict):
    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)
    return lifeDict

#Determine how many alive neighbours there are around each cell
def getNeighbours(item,lifeDict):
    neighbours = 0
    for x in range (-1,2):
        for y in range (-1,2):
            checkCell = (item[0]+x,item[1]+y)
            if checkCell[0] < CELLWIDTH  and checkCell[0] >=0:
                if checkCell [1] < CELLHEIGHT and checkCell[1]>= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0: #Exclude the cell itself
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

#Determine the next generation by running a 'tick'
def tick(lifeDict):
    newTick = {}
    for item in lifeDict:
        numberNeighbours = getNeighbours(item, lifeDict)
        if lifeDict[item] == 1: 
            if numberNeighbours < 2: #Kill for under-population
                newTick[item] = 0
            elif numberNeighbours > 3: #Kill for over-population
                newTick[item] = 0
            else:
                newTick[item] = 1 #Keep status quo (life)
        elif lifeDict[item] == 0:
            if numberNeighbours == 3: #Cell reproduces
                newTick[item] = 1
            else:
                newTick[item] = 0 #Keep status quo (death)
    return newTick

#main function
def main():
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Game of Life')

    DISPLAYSURF.fill(WHITE)

    lifeDict = blankGrid() #Create window and populate to match blank grid
    lifeDict = startingGridRandom(lifeDict) #Assign random start
    
    #Colour the cells
    for item in lifeDict:
        colourGrid(item, lifeDict)

    drawGrid()
    pygame.display.update()
    
    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #Run a tick
        lifeDict = tick(lifeDict)

        #Colour the new cells
        for item in lifeDict:
            colourGrid(item, lifeDict)

        drawGrid()
        pygame.display.update()    
        FPSCLOCK.tick(FPS)
        
if __name__=='__main__':
    main()
