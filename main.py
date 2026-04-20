from cmu_graphics import *
import random
import math

def onAppStart(app):
    app.currentScreen = HomeScreen()
    app.width = 600
    app.height = 400
    app.imageUrls = [
    "images/112Project_coin_image.png",
    "images/basketImage.png",
    "images/bombImage.png",
    "images/presentImage.png",
    "images/flowerImage.png",
    "images/image (5).png",
    "images/lockImage.png",
    "images/completedPresent.png",
    "images/completedFlower.png",
    "images/completedTree.png"
]
    app.coins = 0
    app.extraLifePowerup = False
    app.multiplierOn = False
    
    app.screen1Colors = {
        1: rgb(189, 47, 47),
        2: rgb(173, 44, 43),
        3: rgb(56, 150, 138),
        4: rgb(66, 169, 158),
        5: rgb(75, 182, 168),
        6: rgb(50, 137, 124),
        7: rgb(156, 39, 35)
    }
    
    app.screen2Colors = {
        1: rgb(171, 93, 132),
        2: rgb(166, 79, 124),
        3: rgb(152, 44, 107),
        4: rgb(141, 196, 82),
        5: rgb(124, 173, 71),
        6: rgb(109, 154, 63)
    }
    
    app.screen3Colors = {
        1: rgb(75, 181, 96),
        2: rgb(141, 204, 165),
        3: rgb(61, 156, 81),
        4: rgb(215, 50, 53),
        5: rgb(29, 168, 106),
        6: rgb(13, 103, 76),
        7: rgb(97, 185, 85),
        8: rgb(181, 79, 42),
        9: rgb(222, 115, 64),
        10: rgb(249, 175, 118)
    }
    
    app.numberToPrice1 = {
        1: 2,
        2: 4,
        3: 5,
        4: 10,
        5: 12,
        6: 15,
        7: 20
    }
    
    app.numberToPrice2 = {
        1: 2,
        2: 6,
        3: 6,
        4: 10,
        5: 15,
        6: 20
    }
    
    app.numberToPrice3 = {
        1: 2,
        2: 2,
        3: 2,
        4: 3,
        5: 3,
        6: 5,
        7: 5,
        8: 7,
        9: 10,
        10: 20
    }
    
    app.picture1 = [
            [None, None, 1, 2, None, None, None, 2, 1, None, None],
            [None, 1, 2, None, 1, None, 1, None, 2, 1, None],
            [None, None, 2, None, 1, None, 1, None, 2, None, None],
            [None, None, None, 2, 2, 1, 2, 2, None, None, None],
            [3, 3, 2, 3, 4, 4, 4, 1, 5, 5, 5],
            [3, 3, 2, 3, 4, 4, 4, 1, 5, 5, 5],
            [None, 6, 7, 6, 3, 3, 3, 2, 3, 3, None],
            [None, 3, 2, 3, 4, 4, 4, 1, 4, 5, None],
            [None, 3, 2, 3, 4, 4, 4, 1, 4, 5, None],
            [None, 3, 2, 3, 4, 4, 4, 1, 5, 4, None],
            [None, 3, 2, 3, 4, 4, 4, 1, 5, 4, None]
        ]
    
    app.picture2 = [
        [None, None, 1, None, 1, None, 1, None, 1, None, None],
        [None, None, 1, 2, 1, 2, 1, 2, 1, None, None],
        [None, 2, 1, 2, 1, 2, 1, 2, 1, 2, None],
        [1, 2, 1, 3, 1, 3, 1, 3, 1, 2, 1],
        [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1],
        [None, 1, 3, 1, 3, 3, 3, 1, 3, 1, None],
        [None, 4, 1, 3, 4, 4, 4, 3, 1, 4, None],
        [None, 4, 4, 4, 4, 4, 4, 4, 4, 4, None],
        [None, None, 5, 4, 5, 4, 5, 4, 5, None, None],
        [None, None, None, 5, 4, 5, 4, 5, None, None, None],
        [None, None, None, None, 5, 5, 5, None, None, None, None],
        [6, 5, None, None, None, 5, None, None, None, None, None],
        [5, 6, 5, None, None, 5, None, None, None, 5, 5],
        [5, 5, 6, 5, None, 5, None, None, 5, 6, 5],
        [None, 5, 5, 6, None, 5, None, 5, 6, 5, None],
        [None, None, None, 5, 5, 6, None, 6, 5, 5, None],
        [None, None, None, None, 5, 5, 5, 5, 5, None, None],
        [None, None, None, None, None, 6, None, None, None, None, None],
        [None, None, None, None, None, 6, None, None, None, None, None],
        [None, None, None, None, None, 5, None, None, None, None, None],
        [None, None, None, None, None, 5, None, None, None, None, None]
        ]
        
    app.picture3 = [
        [None, None, None, None, None, 1, None, None, None, None, None],
        [None, None, None, None, None, 2, 2, None, None, None, None],
        [None, None, None, None, 1, 3, 4, None, None, None, None],
        [None, None, None, None, 3, 5, 2, None, None, None, None],
        [None, None, None, 6, 3, 5, 1, 2, None, None, None],
        [None, None, None, 6, 3, 5, 5, 5, None, None, None],
        [None, None, 1, 4, 3, 5, 5, 5, 1, None, None],
        [None, 3, 3, 6, 6, 5, 5, 5, 5, 1, None],
        [None, 3, 6, 6, 5, 5, 1, 6, 4, 1, None],
        [3, 3, 6, 6, 5, 5, 5, 1, 5, 7, 1],
        [6, 6, 6, 4, 5, 5, 5, 1, 1, 1, 1],
        [None, None, None, None, 8, 9, 10, None, None, None, None],
        [None, None, None, None, 8, 9, 10, None, None, None, None],
        [None, None, None, None, 8, 8, 10, None, None, None, None]
    ]
    app.colorsBought1 = set()
    app.colorsBought2 = set()
    app.colorsBought3 = set()
    app.rows1 = 11
    app.cols1 = 11
    app.board1 = [[None for col in range(app.cols1)] for row in range(app.rows1)]
    
    app.rows2 = 21
    app.cols2 = 11
    app.board2 = [[None for col in range(app.cols2)] for row in range(app.rows2)]
    
    app.rows3 = 14
    app.cols3 = 11
    app.board3 = [[None for col in range(app.cols3)] for row in range(app.rows3)]
    app.completedColors1 = set()
    app.completedColors2 = set()
    app.completedColors3 = set()
    app.picture1Completed = False
    app.picture2Completed = False
    app.picture3Completed = False

def redrawAll(app):
    app.currentScreen.draw(app)
    drawImage(app.imageUrls[0], 520, 5,
                        width=40, height=35)
    drawLabel(str(app.coins), 568, 22, size=20, bold=True, align='center')

def onMousePress(app, mouseX, mouseY):
    app.currentScreen.onMousePress(app, mouseX, mouseY)

def onKeyPress(app, key):
    if hasattr(app.currentScreen, 'onKeyPress'):
        app.currentScreen.onKeyPress(app, key)
    if key == 'c':
        app.coins = 500
    elif key == '1':
        app.colorsBought1 = app.completedColors1 = {1,2,3,4,5,6,7}
        app.picture1Completed = True
        app.board1 = app.picture1
    elif key == '2':
        app.colorsBought2 = app.completedColors2 = {1,2,3,4,5,6}
        app.picture2Completed = True
        app.board2 = app.picture2
    elif key == '3':
        app.colorsBought3 = app.completedColors3 = {0,1,2,3,4,5,6,7,8,9,10}
        app.picture3Completed = True
        app.board3 = app.picture3

def onKeyHold(app, keys):
    if hasattr(app.currentScreen, 'onKeyHold'):
        app.currentScreen.onKeyHold(app, keys)

def onStep(app):
    if hasattr(app.currentScreen, 'onStep'):
        app.currentScreen.onStep(app)

def onMouseDrag(app, mouseX, mouseY):
    if hasattr(app.currentScreen, 'onMouseDrag'):
        app.currentScreen.onMouseDrag(app, mouseX, mouseY)


class HomeScreen:
    def __init__(self):
        pass
    
    def draw(self, app):
        #background
        drawRect(0, 0, app.width, app.height, fill='lightSkyBlue')
        
        drawLabel("112 Pay-To-Paint!", app.width/2, 50, size=40, bold=True,
                    fill='midnightBlue')
        
        #buttons
        drawRect(300, 150, 150, 50, fill='black', align='center')
        drawRect(300, 230, 150, 50, fill='black', align='center')
        drawRect(300, 310, 150, 50, fill='black', align='center')
        
        #labels
        drawLabel("PLAY", 300, 150, fill='yellow', align='center', size=25, bold=True)
        drawLabel("COLOR", 300, 230, fill='lightGreen', align='center', size=25, bold=True)
        drawLabel("SHOP", 300, 310, fill='darkOrange', align='center', size=25, bold=True)
        
    def onMousePress(self, app, mouseX, mouseY):
        if self.insidePlay(app, mouseX, mouseY):
            app.currentScreen = PlayScreen(app)
        elif self.insideColor(app, mouseX, mouseY):
            app.currentScreen = ColorScreen(app)
        elif self.insideShop(app, mouseX, mouseY):
            app.currentScreen = ShopScreen()
    
    def insidePlay(self, app, mouseX, mouseY):
        return 225<=mouseX<=375 and 125<=mouseY<=175
    
    def insideColor(self, app, mouseX, mouseY):
        return 225<=mouseX<=375 and 205<=mouseY<=255
    
    def insideShop(self, app, mouseX, mouseY):
        return 225<=mouseX<=375 and 285<=mouseY<=335

class PlayScreen():
    def __init__(self, app):
        self.resetGame(app)
    
    def resetGame(self, app):
        self.paused = True
        self.basketX, self.basketY = 300, 330
        
        self.coins = []
        self.obstacles = []
        self.lives = 4 if app.extraLifePowerup == True else 3
        self.multiplier = 2 if app.multiplierOn == True else 1
        self.steps = 0
        self.gameOver = False
    
    def draw(self, app):
        #background
        drawRect(0, 0, app.width, app.height, fill='lightSkyBlue')
        
        if not self.gameOver:
            drawLabel("Press p to start/pause the game", 300, 25, size=20, 
                        bold=True, align='center')
            drawLabel(f'Lives: {self.lives}', 550, 45, size=15, bold=True,
                        align='center')
            drawLabel(f'Multiplier: {self.multiplier}', 550, 65, size=15,
                        bold=True, align='center')
            
            #draw basket
            drawImage(app.imageUrls[1], self.basketX, self.basketY, width=40, height=60)
            
            #draw coins
            for coin in self.coins:
                drawImage(app.imageUrls[0], coin['cx'], coin['cy'], width=40, height=35)
            
            for obstacle in self.obstacles:
                drawImage(app.imageUrls[2], obstacle['cx'], obstacle['cy'],
                            width=40, height=40)
        
        #draw back & play again buttons
        if self.gameOver:
            drawLabel("GAME OVER!", 300, 140, size=40, bold=True, fill='red')
            drawRect(300, 200, 140, 40, align='center', fill='black')
            drawLabel("Play Again?", 300, 200, align='center', 
                        fill='yellow', size=20, bold=True)
            drawRect(300, 260, 100, 40, align='center', fill='black')
            drawLabel("Back", 300, 260, align='center', 
                        fill='lightGreen', size=20, bold=True)
    
    #check if back button was pressed
    def onMousePress(self, app, mouseX, mouseY):
        if self.gameOver:
            if self.playAgainClicked(app, mouseX, mouseY):
                app.gameOver = False
                self.resetGame(app)
            
            if self.backClicked(app, mouseX, mouseY):
                app.currentScreen = HomeScreen()
    
    def playAgainClicked(self, app, mouseX, mouseY):
        return 225<=mouseX<=375 and 175<=mouseY<=225
    
    def backClicked(self, app, mouseX, mouseY):
        return 250<=mouseX<=350 and 240<=mouseY<=280
    
    def onKeyPress(self, app, key):
        if key == 'p':
            self.paused = not self.paused
    
    def onKeyHold(self, app, keys):
        if not self.paused and not self.gameOver:
            if ('left' in keys):
                if self.basketX > 0:
                    self.basketX -= 5
            elif ('right' in keys):
                if self.basketX < app.width:
                    self.basketX += 5
    
    def onStep(self, app):
        if not self.paused and not self.gameOver:
            self.steps += 1
            
            # add coins at random positions to app.coins
            if self.steps % 8 == 0:
                self.coins.append({
                    'cx': random.randint(20, app.width-20),
                    'cy': 0
                })
            
            # add obstacles at random positions to app.obstacles
            if self.steps % 10 == 0:
                self.obstacles.append({
                    'cx': random.randint(20, app.width-20),
                    'cy': 0,
                    'r': 10
                })
            
            # check if basket and coin touch
            for c in self.coins:
                if self.catchesCoin(c):
                    app.coins += self.multiplier
                    self.coins.remove(c)
                elif c['cy'] > app.height:
                    self.coins.remove(c)
            
            # check if basket and obstacle touch, reduce lives
            for o in self.obstacles:
                if self.hitsObstacle(o):
                    self.lives -= 1
                    self.obstacles.remove(o)
                if self.lives <= 0:
                    self.gameOver = True
                elif o['cy'] > app.height:
                    self.obstacles.remove(o)
            
            for c in self.coins:
                c['cy'] += 5
            for o in self.obstacles:
                o['cy'] += 3
            
            # if basket and obstacle touch, lives -= 1
            # check if game over (if lives == 0)
    def catchesCoin(self, c):
        #c['cx'] between 300 and 340
        #c['cy'] between 370 and 390
        return (self.basketX <= c['cx'] <= self.basketX + 40 and
                self.basketY <= c['cy'] <= self.basketY+60)
    
    def hitsObstacle(self, o):
        return (self.basketX <= o['cx'] <= self.basketX + 40 and
                self.basketY+30 <= o['cy'] <= self.basketY+60)

class ColorScreen():
    def __init__(self, app):
        self.currentPicture = None
        self.imageSelected = False
        self.left = 220
        self.top = 15
        self.rows = 14
        self.cols = 11
        self.width = 600
        self.height = 500
        
        self.selectedColorIndex1 = None
        
        self.selectedColorIndex2 = None
        
        self.selectedColorIndex3 = None
    
    def draw(self, app):
        if app.picture1Completed and app.picture2Completed and app.picture3Completed:
            self.gameOverScreen(app)
        elif self.currentPicture == 1:
            self.drawPicture1(app)
        elif self.currentPicture == 2:
            self.drawPicture2(app)
        elif self.currentPicture == 3:
            self.drawPicture3(app)
        else:
            #background
            drawRect(0, 0, app.width, app.height, fill='lightSkyBlue')
            
            drawLabel("Pick a picture!", 300, 40, size=30, bold=True, align='center')
            drawLabel("1", 120, 90, align='center', size=20, fill='red')
            if app.picture1Completed:
                drawImage(app.imageUrls[7], 120, 210, align='center', height=200, width=170)
            else:
                drawImage(app.imageUrls[3], 120, 210, align='center', 
                        height=200, width=170)
            
            drawLabel("2", 300, 90, align='center', size=20, fill='red')
            if app.picture2Completed:
                drawImage(app.imageUrls[8], 300, 210, align='center', height=200, width=150)
            else:
                drawImage(app.imageUrls[4], 300, 210, align='center', 
                            height=200, width=170)
            
            drawLabel("3", 480, 90, align='center', size=20, fill='red')
            if app.picture3Completed:
                drawImage(app.imageUrls[9], 480, 210, align='center', height=200, width=170)
            else:
                drawImage(app.imageUrls[5], 480, 210, align='center', 
                        height=200, width=170)
        
        #draw back button
        drawRect(70, 360, 100, 40, align='center', fill='black')
        drawLabel("Back", 70, 360, align='center', fill='lightGreen', size=20, bold=True)
    
    #check if back button was pressed
    def onMousePress(self, app, mouseX, mouseY):
        if self.backClicked(app, mouseX, mouseY):
            app.currentScreen = HomeScreen()
        
        if self.imageSelected == False:
            if self.picture1Clicked(app, mouseX, mouseY):
                self.currentPicture = 1
            elif self.picture2Clicked(app, mouseX, mouseY):
                self.currentPicture = 2
            elif self.picture3Clicked(app, mouseX, mouseY):
                self.currentPicture = 3
        
        #picture 1 - checking which color was clicked (from the bottom)
        if self.currentPicture == 1:
            startX = 230
            for i in range(1, 5):
                if startX<=mouseX<=startX+30 and 310<=mouseY<=340:
                    if i in app.colorsBought1 and i not in app.completedColors1:
                        self.selectedColorIndex1 = i
                        return
                startX += 50
            
            startX = 250
            for i in range(5, 8):
                if startX<=mouseX<=startX+30 and 350<=mouseY<=380:
                    if i in app.colorsBought1:
                        self.selectedColorIndex1 = i
                        return
                startX += 50
        
        #picture 2
        if self.currentPicture == 2:
            startX = 160
            for i in range(1, 7):
                if startX<=mouseX<=startX+30 and 345<=mouseY<=375:
                    if i in app.colorsBought2:
                        self.selectedColorIndex2 = i
                        return
                startX += 50
        
        #picture 3
        if self.currentPicture == 3:
            startX = 210
            for i in range(1, 6):
                if startX<=mouseX<=startX+30 and 310<=mouseY<=340:
                    if i-1 in app.colorsBought3:
                        self.selectedColorIndex3 = i
                        return
                startX += 50
            
            startX = 210
            for i in range(6, 11):
                if startX<=mouseX<=startX+30 and 350<=mouseY<=380:
                    if i-1 in app.colorsBought3:
                        self.selectedColorIndex3 = i
                        return
                startX += 50
    
    def colorOver(self, app, picture, colorIndex, board):
        paintedCount = 0
        totalCount = 0
        for row in range(len(picture)):
            for col in range(len(picture[row])):
                if picture[row][col] == colorIndex:
                    totalCount += 1
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == colorIndex:
                    paintedCount += 1
        return paintedCount == totalCount and totalCount > 0
    
    def onMouseDrag(self, app, mouseX, mouseY):
        #picture 1
        if self.selectedColorIndex1 != None or self.selectedColorIndex1 in app.colorsBought1:
            cellSize = 23
            for row in range(len(app.picture1)):
                for col in range(len(app.picture1[row])):
                    x = self.left + col*cellSize - 25
                    y = self.top + row*cellSize + 10
                    if x<=mouseX<=x+cellSize and y<=mouseY<=y+cellSize:
                        correctIndex = app.picture1[row][col]
                        if correctIndex == self.selectedColorIndex1:
                            app.board1[row][col] = self.selectedColorIndex1
                            if self.colorOver(app, app.picture1, self.selectedColorIndex1, app.board1):
                                app.completedColors1.add(self.selectedColorIndex1)
                                if len(app.completedColors1) == len(app.screen1Colors):
                                    app.picture1Completed = True
                            return
        
        #picture 2
        if self.selectedColorIndex2 != None or self.selectedColorIndex2 in app.colorsBought2:
            cellSize = 15
            for row in range(len(app.picture2)):
                for col in range(len(app.picture2[row])):
                    x = self.left + col*cellSize
                    y = self.top + row*cellSize
                    if x<=mouseX<=x+cellSize and y<=mouseY<=y+cellSize:
                        correctIndex = app.picture2[row][col]
                        if correctIndex == self.selectedColorIndex2:
                            app.board2[row][col] = self.selectedColorIndex2
                            if self.colorOver(app, app.picture2, self.selectedColorIndex2, app.board2):
                                app.completedColors2.add(self.selectedColorIndex2)
                                if len(app.completedColors2) == len(app.screen2Colors):
                                    app.picture2Completed = True
                            return
        
        #picture 3
        if self.selectedColorIndex3 != None and self.selectedColorIndex3-1 in app.colorsBought3:
            cellSize = 19
            for row in range(len(app.picture3)):
                for col in range(len(app.picture3[row])):
                    x = self.left + col*cellSize
                    y = self.top + row*cellSize
                    if x<=mouseX<=x+cellSize and y<=mouseY<=y+cellSize:
                        correctIndex = app.picture3[row][col]
                        if correctIndex == self.selectedColorIndex3:
                            app.board3[row][col] = self.selectedColorIndex3
                            if self.colorOver(app, app.picture3, self.selectedColorIndex3, app.board3):
                                app.completedColors3.add(self.selectedColorIndex3)
                                if len(app.completedColors3) == len(app.screen3Colors):
                                    app.picture3Completed = True
                            return
    
    def picture1Clicked(self, app, mouseX, mouseY):
        return 35<=mouseX<=205 and 110<=mouseY<=310
    
    def picture2Clicked(self, app, mouseX, mouseY):
        return 215<=mouseX<=385 and 110<=mouseY<=310
    
    def picture3Clicked(self, app, mouseX, mouseY):
        return 395<=mouseX<=565 and 110<=mouseY<=310
    
    def backClicked(self, app, mouseX, mouseY):
        return 20<=mouseX<=120 and 340<=mouseY<=380
    
    def gameOverScreen(self, app):
        drawLabel("Congrats. You did it!", 300, 50, size=30)
        drawImage(app.imageUrls[7], 120, 210, align='center', 
                        height=200, width=170)
        drawImage(app.imageUrls[8], 300, 210, align='center', 
                    height=200, width=150)
        drawImage(app.imageUrls[9], 480, 210, align='center', 
                    height=200, width=170)
        
        drawLabel("You are a true artist.", 300, 350, size=20)

    def drawPicture1(self, app):
        self.imageSelected = True
        drawLabel("Picture 1!", 80, 40, size=20)
        colorsAvailable1 = dict()
        for i in app.screen1Colors:
            if i in app.colorsBought1:
                colorsAvailable1[i] = app.screen1Colors[i]
        
        #drawing the picture
        cellSize = 23
        for row in range(len(app.picture1)):
            for col in range(len(app.picture1[row])):
                x = self.left + col*cellSize - 25
                y = self.top + row*cellSize + 15
                
                painted = app.board1[row][col] #whether it's colored in
                correctIndex = app.picture1[row][col] #whether it should be colored in
                
                if painted != None:
                    color = app.screen1Colors[painted]
                    drawRect(x, y, cellSize, cellSize, fill=color)
                else:
                    color = 'lightGray'
                
                #if it's not painted, and if there is a selected color and
                #if the picture[row][col] is the same as the selected color,
                #set the color to a darker gray
                if painted is None:
                    if (self.selectedColorIndex1 != None and
                        correctIndex == self.selectedColorIndex1):
                            color = 'gray'
                
                if correctIndex != None:
                    drawRect(x, y, cellSize, cellSize, fill=color, border='black',
                                borderWidth=0.5)
                    drawLabel(str(correctIndex), x+cellSize/2, y+cellSize/2,
                                size=12, fill='black')
        
        #drawing the colors at the bottom
        startX = 230
        for i in range(4):
            color = app.screen1Colors[i+1]
            if i+1 == self.selectedColorIndex1 and i+1 not in app.completedColors1:
                drawRect(startX+15, 310+15, 35, 35, fill='black', align='center')
            drawRect(startX, 310, 30, 30, fill=color)
            if i+1 not in app.completedColors1:
                drawLabel(str(i+1), startX+15, 325, size=15)
            if i+1 not in colorsAvailable1:
                drawImage(app.imageUrls[6], startX, 310,
                            width=30, height=30)
            startX += 50
        
        startX = 250
        for i in range(3):
            color = app.screen1Colors[i+5]
            if i+5 == self.selectedColorIndex1 and i+5 not in app.completedColors1:
                drawRect(startX+15, 350+15, 35, 35, fill='black', align='center')
            drawRect(startX, 350, 30, 30, fill=color)
            if i+5 not in app.completedColors1:
                drawLabel(str(i+5), startX+15, 365, size=15)
            if i+5 not in colorsAvailable1:
                drawImage(app.imageUrls[6], startX, 350,
                            width=30, height=30)
            startX += 50
    
    def drawPicture2(self, app):
        self.imageSelected = True
        drawLabel("Picture 2!", 80, 40, size=20)
        colorsAvailable2 = dict()
        for i in app.screen2Colors:
            if i in app.colorsBought2:
                colorsAvailable2[i] = app.screen2Colors[i]
        
        #drawing the picture
        cellSize = 15
        for row in range(len(app.picture2)):
            for col in range(len(app.picture2[row])):
                x = self.left + col*cellSize
                y = self.top + row*cellSize
                
                painted = app.board2[row][col] #whether it's colored in
                correctIndex = app.picture2[row][col] #whether it should be colored in
                
                if painted != None:
                    color = app.screen2Colors[painted]
                    drawRect(x, y, cellSize, cellSize, fill=color)
                else:
                    color = 'lightGray'
                
                if painted is None:
                    if (self.selectedColorIndex2 != None and
                        correctIndex == self.selectedColorIndex2):
                            color = 'gray'
                
                if correctIndex != None:
                    drawRect(x, y, cellSize, cellSize, fill=color, border='black',
                                borderWidth=0.5)
                    drawLabel(str(correctIndex), x+cellSize/2, y+cellSize/2,
                                size=10, fill='black')
        
        #drawing the colors at the bottom
        startX = 160
        for i in range(6):
            color = app.screen2Colors[i+1]
            if i+1 == self.selectedColorIndex2 and i+1 not in app.completedColors2:
                drawRect(startX+15, 345+15, 35, 35, fill='black', align='center')
            drawRect(startX, 345, 30, 30, fill=color)
            if i+1 not in app.completedColors2:
                drawLabel(str(i+1), startX+15, 360, size=15)
            if i+1 not in colorsAvailable2:
                drawImage(app.imageUrls[6], startX, 345,
                            width=30, height=30)
            startX += 50
    
    def drawPicture3(self, app):
        self.imageSelected = True
        drawLabel("Picture 3!", 80, 40, size=20)
        colorsAvailable3 = dict()
        
        for i in app.screen3Colors:
            if i-1 in app.colorsBought3:
                colorsAvailable3[i] = app.screen3Colors[i]
        
        #drawing the picture
        cellSize = 19
        for row in range(len(app.picture3)):
            for col in range(len(app.picture3[row])):
                x = self.left + col*cellSize
                y = self.top + row*cellSize
                
                painted = app.board3[row][col] #whether it's colored in
                correctIndex = app.picture3[row][col] #whether it should be colored in
                
                if painted != None:
                    color = app.screen3Colors[painted]
                    drawRect(x, y, cellSize, cellSize, fill=color)
                else:
                    color = 'lightGray'
                
                if painted is None:
                    if (self.selectedColorIndex3 != None and
                        correctIndex == self.selectedColorIndex3):
                            color = 'gray'
                
                if correctIndex != None:
                    drawRect(x, y, cellSize, cellSize, fill=color, border='black',
                                borderWidth=0.5)
                    drawLabel(str(correctIndex), x+cellSize/2, y+cellSize/2,
                                size=10, fill='black')
        
        #drawing the colors at the bottom
        startX = 210
        for i in range(5):
            color = app.screen3Colors[i+1]
            if i+1 == self.selectedColorIndex3 and i+1 not in app.completedColors3:
                drawRect(startX+15, 310+15, 35, 35, fill='black', align='center')
            drawRect(startX, 310, 30, 30, fill=color)
            if i+1 not in app.completedColors3:
                drawLabel(str(i+1), startX+15, 325, size=15)
            if i+1 not in colorsAvailable3:
                drawImage(app.imageUrls[6], startX, 310,
                            width=30, height=30)
            startX += 50
        
        startX = 210
        for i in range(5, 10):
            color = app.screen3Colors[i+1]
            if i+1 == self.selectedColorIndex3 and i+1 not in app.completedColors3:
                drawRect(startX+15, 350+15, 35, 35, fill='black', align='center')
            drawRect(startX, 350, 30, 30, fill=color)
            if i+1 not in app.completedColors3:
                drawLabel(str(i+1), startX+15, 365, size=15)
            if i+1 not in colorsAvailable3:
                drawImage(app.imageUrls[6], startX, 350,
                            width=30, height=30)
            startX += 50
    
    def getCellSize(self):
        cellWidth = self.width / self.cols
        cellHeight = self.height / self.rows
        return (cellWidth, cellHeight)
    
    def getCell(self, mouseX, mouseY):
        dx = mouseX - self.left
        dy = mouseY - self.top
        cellWidth, cellHeight = self.getCellSize()
        row = math.floor(dy/cellHeight)
        col = math.floor(dx/cellWidth)
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return (row, col)
        return None

class ShopScreen():
    def __init__(self):
        self.shopScreen = 1
        self.shopBackButtonCoords = [240, 320, 240, 360, 210, 340]
        self.shopForwardButtonCoords = [360, 320, 360, 360, 390, 340]
    
    def draw(self, app):
        #background
        drawRect(0, 0, app.width, app.height, fill='lightSkyBlue')
        
        #title
        drawLabel("Shop", 300, 25, size=30, bold=True, align='center')
        drawLabel("What would you like to buy?", 300, 60, size=20, bold=True, align='center')
        
        #draw back button
        drawRect(70, 360, 100, 40, align='center', fill='black')
        drawLabel("Back", 70, 360, align='center', fill='lightGreen', size=20, bold=True)
        if self.shopScreen == 1:
            self.drawScreen1(app, app.screen1Colors)
        elif self.shopScreen == 2:
            self.drawScreen2(app, app.screen2Colors)
        elif self.shopScreen == 3:
            self.drawScreen3(app, app.screen3Colors)
        elif self.shopScreen == 4:
            self.drawScreen4(app)
    
    def drawScreen1(self, app, colors):
        drawLabel(f'Picture 1', 300, 110, fill='white', align='center',
                    size=20, bold=True)
        
        startX = 160
        for i in range(4):
            fillColor = colors[i+1]
            labelColor='white'
            drawRect(startX, 160, 40, 40, fill=fillColor)
                
            drawLabel(str(i+1), startX+20, 180, fill=labelColor, align='center',
                        size=20, bold=True)
            
            #drawing x's
            if i+1 in app.colorsBought1:
                self.drawX1(startX, 160)
            drawImage(app.imageUrls[0], startX-15, 128,
                        width=40, height=35)
            price = app.numberToPrice1[i+1]
            drawLabel(str(price), startX+27, 145, size=18)
            startX += 80
        
        startX = 200
        for i in range(3):
            labelColor='white'
            color = colors[i+5]
            drawRect(startX, 250, 40, 40, fill=color)
            drawLabel(str(i+5), startX+20, 270, fill=labelColor, align='center',
                        size=20, bold=True)
            
            #drawing the x's
            if i+5 in app.colorsBought1:
                self.drawX1(startX, 250)
            drawImage(app.imageUrls[0], startX-15, 218,
                        width=40, height=35)
            price = app.numberToPrice1[i+5]
            drawLabel(str(price), startX+27, 235, size=18)
            startX += 80
        
        #draw shop arrows
        drawPolygon(*self.shopBackButtonCoords, fill='black')
        drawPolygon(*self.shopForwardButtonCoords, fill='black')
    
    def drawScreen2(self, app, colors):
        drawLabel(f'Picture 2', 300, 110, fill='white', align='center',
                    size=20, bold=True)
        
        startX = 200
        for i in range(3):
            fillColor = colors[i+1]
            labelColor='white'
            drawRect(startX, 160, 40, 40, fill=fillColor)
            
            drawLabel(str(i+1), startX+20, 180, fill=labelColor,
                        size=20, bold=True)
            
            #drawing x's
            if i+1 in app.colorsBought2:
                self.drawX2(startX, 160)
            drawImage(app.imageUrls[0], startX-15, 128,
                        width=40, height=35)
            price = app.numberToPrice1[i+1]
            drawLabel(str(price), startX+27, 145, size=18)
            startX += 80
        
        startX = 200
        for i in range(4, 7):
            labelColor='white'
            color = colors[i]
            drawRect(startX, 250, 40, 40, fill=color)
            drawLabel(str(i), startX+20, 270, fill=labelColor, align='center',
                        size=20, bold=True)
            
            #drawing the x's
            if i in app.colorsBought2:
                self.drawX2(startX, 250)
            drawImage(app.imageUrls[0], startX-15, 218,
                        width=40, height=35)
            #fix: make a dictionary mapping the index (1-10) to the price, and set that = to what we draw in the label
            price = app.numberToPrice2[i]
            drawLabel(str(price), startX+27, 235, size=18)
            startX += 80
        
        #draw shop arrows
        drawPolygon(*self.shopBackButtonCoords, fill='black')
        drawPolygon(*self.shopForwardButtonCoords, fill='black')

    def drawScreen3(self, app, colors):
        drawLabel(f'Picture 3', 300, 110, fill='white', align='center',
                    size=20, bold=True)
        
        startX = 120
        for i in range(5):
            fillColor = colors[i+1]
            labelColor='white'
            if self.shopScreen==2:
                if i==2:
                    labelColor='black'
            drawRect(startX, 160, 40, 40, fill=fillColor)
                
            drawLabel(str(i+1), startX+20, 180, fill=labelColor, align='center',
                        size=20, bold=True)
            
            #drawing x's
            if i in app.colorsBought3:
                self.drawX3(startX, 160)
            drawImage(app.imageUrls[0], startX-15, 128,
                        width=40, height=35)
            price = app.numberToPrice3[i+1]
            drawLabel(str(price), startX+27, 145, size=18)
            startX += 80
        
        startX = 120
        for i in range(5):
            labelColor='white'
            color = colors[i+6]
            drawRect(startX, 250, 40, 40, fill=color)
            drawLabel(str(i+6), startX+20, 270, fill=labelColor, align='center',
                        size=20, bold=True)
            
            #drawing the x's
            if i+5 in app.colorsBought3:
                self.drawX3(startX, 250)
            drawImage(app.imageUrls[0], startX-15, 218,
                        width=40, height=35)
            #fix: make a dictionary mapping the index (1-10) to the price, and set that = to what we draw in the label
            price = app.numberToPrice3[i+6]
            drawLabel(str(price), startX+27, 235, size=18)
            startX += 80
        
        #draw shop arrows
        drawPolygon(*self.shopBackButtonCoords, fill='black')
        drawPolygon(*self.shopForwardButtonCoords, fill='black')
    
    def drawX1(self, left, top):
        drawLine(left, top, left+40, top+40, fill='red')
        drawLine(left+40, top, left, top+40, fill='red')
    
    def drawX2(self, left, top):
        drawLine(left, top, left+40, top+40, fill='red')
        drawLine(left+40, top, left, top+40, fill='red')
    
    def drawX3(self, left, top):
        drawLine(left, top, left+40, top+40, fill='red')
        drawLine(left+40, top, left, top+40, fill='red')
    
    def drawScreen4(self, app):
        drawLabel("Minigame Powerups", 300, 110, fill='white', align='center',
                    size=20, bold=True)
        
        drawRect(200, 160, 200, 40, fill='black')
        drawLabel("Extra Life -      15", 300, 180, fill='white', size=20,
                    bold=True)
        drawImage(app.imageUrls[0], 325, 162.8, width=40, height=35)
        
        drawRect(200, 240, 200, 40, fill='black')
        drawLabel("2x Multiplier -     75", 300, 260, fill='white', size=20,
                    bold=True)
        drawImage(app.imageUrls[0], 357, 260, width=40, height=35,
                    align='center')
        
        #drawing x's
        if app.extraLifePowerup:
            drawLine(200, 160, 400, 200, fill='red')
            drawLine(400, 160, 200, 200, fill='red')
        if app.multiplierOn:
            drawLine(200, 240, 400, 280, fill='red')
            drawLine(400, 240, 200, 280, fill='red')
        
        #draw shop arrows
        drawPolygon(*self.shopBackButtonCoords, fill='black')
        drawPolygon(*self.shopForwardButtonCoords, fill='black')
    
    #check if back button or shop buttons were pressed
    def onMousePress(self, app, mouseX, mouseY):
        if self.backClicked(app, mouseX, mouseY):
            app.currentScreen = HomeScreen()
        
        #can't figure out how to check whether a click is inside the triangles
        
        #check whether a powerup was clicked
        if self.shopScreen == 4:
            p = self.powerupClicked(app, mouseX, mouseY)
            if p == 'extra life':
                self.buyExtraLife(app)
            elif p == 'multiplier':
                self.buyMultiplier(app)
        
        #on screen 1, check which color was clicked
        elif self.shopScreen == 1:
            s = self.colorClicked1(app, mouseX, mouseY) #returns the index (0-9)
            if s != None:
                price = app.numberToPrice1[s]
                if app.coins >= price and s not in app.colorsBought1:
                    app.coins -= price
                    app.colorsBought1.add(s)
        #screen 2
        elif self.shopScreen == 2:
            s = self.colorClicked2(app, mouseX, mouseY)
            if s != None:
                price = app.numberToPrice2[s]
                if app.coins >= price and s not in app.colorsBought2:
                    app.coins -= price
                    app.colorsBought2.add(s)
        #screen 3
        elif self.shopScreen == 3:
            s = self.colorClicked3(app, mouseX, mouseY)
            if s != None:
                price = app.numberToPrice3[s+1]
                if app.coins >= price and s not in app.colorsBought3:
                    app.coins -= price
                    app.colorsBought3.add(s)
    
    def powerupClicked(self, app, mouseX, mouseY):
        if 200<=mouseX<=400 and 160<=mouseY<=200:
            return 'extra life'
        elif 200<=mouseX<=400 and 240<=mouseY<=280:
            return 'multiplier'
        return None
    
    def buyExtraLife(self, app):
        price = 15
        if app.coins >= price:
            app.coins -= price
            app.extraLifePowerup = True
    
    def buyMultiplier(self, app):
        price = 75
        if app.coins >= price:
            app.coins -= price
            app.multiplierOn = True
    
    def colorClicked1(self, app, mouseX, mouseY):
        firstX = 160
        for i in range(4):
            if firstX<=mouseX<=firstX+40 and 160<=mouseY<=200:
                return i+1
            firstX += 80
        
        secondX = 200
        for i in range(3):
            if secondX<=mouseX<=secondX+40 and 250<=mouseY<=290:
                return i+5
            secondX += 80
        return None
    
    def colorClicked2(self, app, mouseX, mouseY):
        firstX = 200
        for i in range(1, 4):
            if firstX<=mouseX<=firstX+40 and 160<=mouseY<=200:
                return i
            firstX += 80
        
        secondX = 200
        for i in range(4, 7):
            if secondX<=mouseX<=secondX+40 and 250<=mouseY<=290:
                return i
            secondX += 80
        return None
    
    def colorClicked3(self, app, mouseX, mouseY):
        firstX = 120
        for i in range(5):
            if firstX<=mouseX<=firstX+40 and 160<=mouseY<=200:
                return i
            firstX += 80
        
        secondX = 120
        for i in range(5,10):
            if secondX<=mouseX<=secondX+40 and 250<=mouseY<=290:
                return i
            secondX += 80
        return None
    
    def backClicked(self, app, mouseX, mouseY):
        return 20<=mouseX<=120 and 340<=mouseY<=380
    
    def onKeyPress(self, app, key):
        if key == 'right':
            if self.shopScreen < 4:
                self.shopScreen += 1
        elif key == 'left':
            if self.shopScreen > 1:
                self.shopScreen -= 1

def main():
    runApp()

main()