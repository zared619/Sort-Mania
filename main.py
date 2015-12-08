# Card Game Project 2
# Seth Loew and Zared Hollabaugh 

#import the necessary libraries
import pygame, random, sys, time
import string
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)

windowx = 726
windowy = 719

movesx = 145
movesy = 175

titlex = 350
titley = 40

score = 25

# where the grid starts
play_lcorner_x = 60
play_lcorner_y = 204

#width of the cell in the grid
box_width = 100

# number of boxes in each row and column
grid_width = 6
grid_height = 5

# the right bottom corner of the grid
play_rcorner_x = play_lcorner_x + grid_width*box_width
play_rcorner_y = play_lcorner_y + grid_height*box_width

mycards = [ "cards\card1.png",  "cards\card2.png",  "cards\card3.png",  "cards\card4.png",
            "cards\card5.png", "cards\card6.png"]

def getBoard():
    # one dimensional list
    icons = []
    for card in mycards:
        icons.append(card)
        icons.append(card)
        icons.append(card)
        icons.append(card)
        icons.append(card)
    random.shuffle(icons)

    # two dimensional list
    board = []
    for x in range(grid_width):
        column = []
        for y in range(grid_height):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

myboard = getBoard()
print(myboard)

def checkHorz():
    isGood = 1
    for x in range (0,5):
        myString = myboard[0][x]
        print("Row: " + str(x))
        for y in range (1,5):
            if myString == myboard[y][x]:
                print("We're good")
                continue
            else:
                isGood = 0;
                break;
    return isGood

def checkVert():
    isGood =1
    for x in range (0,5):
        myString = myboard[x][0]
        print("Column: " + str(x))
        for y in range (1,5):
            curString = myboard[x][y]
            if myString == curString:
                print("We're good")
                continue
            else:
                isGood = 0;
                break;
    return isGood

#variables to keep track of where the user clicked
box_x = -1
box_y = -1
selected_x = -1
selected_y = -1

#variables to keep track of mouse clicks
first_click = False
second_click = False

pygame.init()

displaysurf = pygame.display.set_mode((windowx,windowy))
pygame.display.set_caption('Memory Game')

fontObj = pygame.font.SysFont('bookantiqua', 18, True, False)
largefontObj = pygame.font.SysFont('bookantiqua', 48, True, False)

#refresh the screen
pygame.display.update()

#game loop (means this will never become false and will always run
while True:
    displaysurf.fill(black)
    title = "Swap Mania"
    titleSurfaceObj = largefontObj.render(title, True, white )
    titleRectObj = titleSurfaceObj.get_rect()
    titleRectObj.center = (360, 40)
    displaysurf.blit(titleSurfaceObj, titleRectObj)

    msg = "Score: \t" + str(score)
    textSurfaceObj = fontObj.render(msg, True, white )
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (movesx, movesy)
    displaysurf.blit(textSurfaceObj, textRectObj)

    colindex = 0
    for cardlist in myboard:
        rowindex = 0
        for card in cardlist:
            imgx = colindex * box_width + play_lcorner_x
            imgy = rowindex * box_width + play_lcorner_y
            myimg = pygame.image.load(myboard[colindex][rowindex])
            displaysurf.blit(myimg, (imgx, imgy))

            rowindex += 1
        colindex += 1
        if(rowindex>=5):
            rowindex = 4

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONUP:
            mousex,mousey = event.pos
            if mousex > play_lcorner_x and mousey > play_lcorner_y and mousex < play_rcorner_x and mousey < play_rcorner_y:
                box_x = int((mousex - play_lcorner_x)/box_width)
                box_y = (mousey - play_lcorner_y)//box_width
                print("Column: " + str(box_x) + "Row: " + str(box_y))
                print(myboard[box_x][box_y])
                if first_click == True:
                    first_click = False
                    second_click = True
                    score -= 1
                    box_selected = myboard[box_x][box_y]
                    prev_selected = myboard[selected_x][selected_y]

                    #swaps the selections
                    myboard[box_x][box_y] = prev_selected
                    myboard[selected_x][selected_y] = box_selected

                    #checks to see if we've won
                    #checkWinHorz = checkHorz()
                    checkWinVert = checkVert()

                    if checkWinVert == 1:
                        print("You've won!")

                    if box_x == selected_x and box_y == selected_y:
                        print("Same box")
                else:
                    selected_x = box_x
                    selected_y = box_y
                    first_click = True
                    second_click = False


   
            
    pygame.display.update()



    
