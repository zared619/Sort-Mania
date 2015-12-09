# Card Game Project 2
# Seth Loew and Zared Hollabaugh 

#import the necessary libraries
import pygame, random, sys, time
import string
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)

windowx = 800
windowy = 600

movesx = 150
movesy = 70

titlex = 350
titley = 40

score = 25

# where the grid starts
play_lcorner_x = 100
play_lcorner_y = 80

#width of the cell in the grid
box_width = 100

# number of boxes in each row and column
grid_width = 6
grid_height = 5

# the right bottom corner of the grid
play_rcorner_x = play_lcorner_x + grid_width*box_width
play_rcorner_y = play_lcorner_y + grid_height*box_width

mycards = [ "cards\whiteCards\card1_white.png",  "cards\whiteCards\card2_white.png",  "cards\whiteCards\card3_white.png",  "cards\whiteCards\card4_white.png",
            "cards\whiteCards\card5_white.png", "cards\whiteCards\card6_white.png"]

mycoloredcards = ["cards\pinkCards\card1_pink.png",  "cards\pinkCards\card2_pink.png",  "cards\pinkCards\card3_pink.png",  "cards\pinkCards\card4_pink.png",
            "cards\pinkCards\card5_pink.png", "cards\pinkCards\card6_pink.png", "cards\purpleCards\card1_purple.png",  "cards\purpleCards\card2_purple.png",
            "cards\purpleCards\card3_purple.png",  "cards\purpleCards\card4_purple.png","cards\purpleCards\card5_purple.png", "cards\purpleCards\card6_purple.png",
            "cards\yellowCards\card1_yellow.png",  "cards\yellowCards\card2_yellow.png",  "cards\yellowCards\card3_yellow.png",  "cards\yellowCards\card4_yellow.png",
            "cards\yellowCards\card5_yellow.png", "cards\yellowCards\card6_yellow.png","cards\card1_red.png",  "cards\card2_red.png",
            "cards\card3_red.png",  "cards\card4_red.png","cards\card5_red.png", "cards\card6_red.png",
            "cards\greenCards\card1_green.png",  "cards\greenCards\card2_green.png","cards\greenCards\card3_green.png",  "cards\greenCards\card4_green.png",
            "cards\greenCards\card5_green.png", "cards\greenCards\card6_green.png",
            ]

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

def getcoloredBoard():
    # one dimensional list
    icons = []
    for card in mycoloredcards:
        icons.append(card)
    random.shuffle(icons)

    # two dimensional list
    coloredboard = []
    for x in range(grid_width):
        column = []
        for y in range(grid_height):
            column.append(icons[0])
            del icons[0]
        coloredboard.append(column)
    return coloredboard

myboard = getBoard()
print(myboard)

mycoloredboard = getcoloredBoard()
print(mycoloredboard)

def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

def checkHorz():
    isGood = 1
    for x in range (0,5):
        myString = mycoloredboard[0][x]
        print(myString)
        for y in range (1,5):
            levDistance = minimumEditDistance(myString,mycoloredboard[y][x])
            print(levDistance)
            if  levDistance ==1:
                continue
            else:
                isGood = 0;
                break;
    return isGood

def checkVert():
    isGood =1
    for x in range (0,5):
        myString = myboard[x][0]
        for y in range (1,5):
            curString = myboard[x][y]
            if myString == curString:
                continue
            else:
                isGood = 0;
                break;
    return isGood

def gameOver():
    pygame.draw.rect(displaysurf, white, (125, 125, 550, 450))
    fontObj = pygame.font.SysFont('times', 25)
    textSurf = fontObj.render('Game Over!!!', True, black, white)
    textRect = textSurf.get_rect()
    textRect.center = (400, 150)
    displaysurf.blit(textSurf, textRect)

    if score > 0:
        fontObj2 = pygame.font.SysFont('times', 25)
        textSurf2 = fontObj2.render('You WON! Your score is: ' + str(score+1), True, black, white)
        textRect2 = textSurf2.get_rect()
        textRect2.center = (400, 250)
        displaysurf.blit(textSurf2, textRect2)
        pygame.display.update()
        time.sleep(7)
    else:
        fontObj2 = pygame.font.SysFont('times', 25)
        textSurf2 = fontObj2.render('Sorry, you lost... Your score is ' + str(score), True, black, white)
        textRect2 = textSurf2.get_rect()
        textRect2.center = (400, 250)
        displaysurf.blit(textSurf2, textRect2)
        pygame.display.update()
        time.sleep(7)


#variables to keep track of where the user clicked
box_x = -1
box_y = -1
selected_x = -1
selected_y = -1

#variables to keep track of mouse clicks
first_click = False
second_click = False
endGame = False
welcomeMode = True
whiteSide = True

pygame.init()

displaysurf = pygame.display.set_mode((windowx,windowy))
pygame.display.set_caption('Memory Game')

fontObj = pygame.font.SysFont('bookantiqua', 18, True, False)
largefontObj = pygame.font.SysFont('bookantiqua', 48, True, False)

#refresh the screen
pygame.display.update()

#game loop (means this will never become false and will always run
while True:
    backgroundImg = pygame.image.load('background.png')
    displaysurf.blit(backgroundImg, (0, 0))

    if welcomeMode == True:
        pygame.draw.rect(displaysurf, white, (125, 125, 550, 450))
        fontObj = pygame.font.SysFont('times', 25)
        textSurf = fontObj.render('Choose a Level', True, black, white)
        textRect = textSurf.get_rect()
        textRect.center = (400, 150)
        displaysurf.blit(textSurf, textRect)
        whiteCards = ["cards\whiteCards\card1_white.png", "cards\whiteCards\card2_white.png",
                      "cards\whiteCards\card3_white.png"]
        coloredCards = ["cards\purpleCards\card1_purple.png", "cards\greenCards\card2_green.png",
                        "cards\pinkCards\card3_pink.png"]

        temp = 0
        tempx = 200
        tempy = 200
        for card in whiteCards:
            cardImage = pygame.image.load(whiteCards[temp])
            displaysurf.blit(cardImage, (tempx, tempy))
            tempy += 100
            temp += 1

        temp2 = 0
        tempx2 = 500
        tempy2 = 200
        for card in coloredCards:
            cardImage2 = pygame.image.load(coloredCards[temp2])
            displaysurf.blit(cardImage2, (tempx2, tempy2))
            tempy2 += 100
            temp2 += 1
        mousex = 0
        mousey = 0
 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
            if mousex < 400 and mousey > 100:
                print(whiteSide)
                whiteSide = True
                welcomeMode = False
            elif mousex > 400 and mousey > 100:
                whiteSide = False
                welcomeMode = False


    if welcomeMode == False and whiteSide == True:
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
                            gameOver()
                            endGame = True
                            break
                        if score == 0:
                            gameOver()
                            endGame = True
                            break

                        if box_x == selected_x and box_y == selected_y:
                            print("Same box")
                    else:
                        selected_x = box_x
                        selected_y = box_y
                        first_click = True
                        second_click = False
                if endGame == True:
                    break
            if endGame == True:
                break
        if endGame == True:
            break

    if welcomeMode == False and whiteSide == False:
        msg = "Score: " + str(score)
        textSurfaceObj = fontObj.render(msg, True, white )
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (movesx, movesy)
        displaysurf.blit(textSurfaceObj, textRectObj)

        colindex = 0
        for cardlist in mycoloredboard:
            rowindex = 0
            for card in cardlist:
                imgx = colindex * box_width + play_lcorner_x
                imgy = rowindex * box_width + play_lcorner_y
                myimg = pygame.image.load(mycoloredboard[colindex][rowindex])
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
                    print(mycoloredboard[box_x][box_y])
                    if first_click == True:
                        first_click = False
                        second_click = True
                        score -= 1
                        box_selected = mycoloredboard[box_x][box_y]
                        prev_selected = mycoloredboard[selected_x][selected_y]

                        #swaps the selections
                        mycoloredboard[box_x][box_y] = prev_selected
                        mycoloredboard[selected_x][selected_y] = box_selected

                        #checks to see if we've won
                        checkWinHorz = checkHorz()
                        #checkWinVert = checkVert()

                        if checkWinHorz == 1:
                            gameOver()
                            endGame = True
                            break
                        if score == 0:
                            gameOver()
                            endGame = True
                            break

                        if box_x == selected_x and box_y == selected_y:
                            print("Same box")
                    else:
                        selected_x = box_x
                        selected_y = box_y
                        first_click = True
                        second_click = False
                if endGame == True:
                    break
        
        if endGame == True:
            break
        
    pygame.display.update()



    
