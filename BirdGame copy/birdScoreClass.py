#birdScoreClass


import pygame, sys

pygame.init()


class BirdScore(pygame.sprite.Sprite):
    def __init__(self, screen):

        #instantiate variables
        self.screen = screen
        #variables used for keeping score and life
        self.points = 0
        self.life = 10

        #load image of bird used for the life
        self.image = pygame.image.load("Birds/Bird1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        #colors
        self.WHITE = (255,255,255)
        self.YELLOW = (255,242,0)
        self.RED = (255,0,0)
        self.TRANSP = (0,0,0,0)

    #this function displays the score on the screen
    def displayScore(self):
        #font used for the font
        scoreFont = pygame.font.SysFont("Broadway", 50)

        # Create text Surface
        SCORESURF = scoreFont.render("Score: " + str(self.points),True,self.WHITE,None)
        #puts the score on the screen
        self.screen.blit(SCORESURF,(0,625))

    #this function adds points as enemies are shot.
    def addPoints(self, enemy):

        #for loop runs through the enemy list to identify the type of enemy
        #according to type of enemy a different point value is applied
        for x in enemy:

            if x.enemy_num == 0:
                self.points += 100
            elif x.enemy_num == 1:
                self.points +=100
            elif x.enemy_num == 2:
                self.points += 150
            elif x.enemy_num == 3:
                self.points +=150
            elif x.enemy_num == 4:
                self.points +=200
            elif x.enemy_num == 5:
                self.points +=200
            elif x.enemy_num == 6:
                self.points += 300
            elif x.enemy_num == 7:
                self.points += 200
            elif x.enemy_num == 8:
                self.points += 400
            elif x.enemy_num == 9:
                self.points += 200


    #this function displays the amount of lives on the screen
    def displayLife(self):

        #establishes font used for the score
        lifeFont= pygame.font.SysFont("Broadway",50)

        LIFESURF = lifeFont.render("x " + str(self.life), True, self.WHITE, None)
        #displays the image of the bird and the text specified in the surface above
        self.screen.blit(self.image, (1045,618))
        self.screen.blit(LIFESURF, (1100,625))

    #this function subtracts 1 from total lives
    def loseLife(self):

        self.life -= 1

    #this function sets the number of lives to three and points to zero
    #in order to start the game from the beginning
    def newGame(self):

        self.life = 3
        self.points = 0

    #this function initiates the different game screens depending on number of lives
    def gameOver(self):

        #boolean to trigger game over
        gameOver = 0

        #displays GAME OVER screen when points are less than zero
        if self.life <= 0:
            GAMEOVER = pygame.image.load("gameOver.png").convert()
            self.screen.fill((0,0,0))
            self.screen.blit(GAMEOVER, (275,153))

            gameOver = 1

        #displays title screen when lives are = to ten
        elif self.life == 10:
            TITLE = pygame.image.load("title.png").convert()
            self.screen.fill((0,0,0))
            self.screen.blit(TITLE,(275,153))

            gameOver = 2
        #displays instruction screen when lives are = to 27
        elif self.life == 27:
            INSTRUCTIONS = pygame.image.load("instructions.png").convert()
            self.screen.fill((0,0,0))
            self.screen.blit(INSTRUCTIONS,(275,153))
            gameOver = 3

        #returns either a 0,1,2 or 3 depending on life value
        return gameOver





