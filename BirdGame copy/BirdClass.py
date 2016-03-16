
from WeaponClass import *

#the sprite that the player controls
class bird(pygame.sprite.Sprite):
    def __init__(self, blitSurf):

        #initializes sprite
        pygame.sprite.Sprite.__init__(self)

        #loads all the different colored bird images
        self.wbird = pygame.transform.scale(pygame.image.load("Birds/Bird1.png").convert_alpha(), (50, 50))
        self.bbird = pygame.transform.scale(pygame.image.load("Birds/bb4.png").convert_alpha(), (50, 50))
        self.gbird = pygame.transform.scale(pygame.image.load("Birds/gb4.png").convert_alpha(), (50, 50))
        self.rbird = pygame.transform.scale(pygame.image.load("Birds/rb4.png").convert_alpha(), (50, 50))
        self.ybird = pygame.transform.scale(pygame.image.load("Birds/yb4.png").convert_alpha(), (50, 50))

        #sets image to the default white
        self.image = self.wbird
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.color = "white"

        #sets up the blit surface which will be passed into certain methods
        self.BLITSURF = blitSurf

        #sets up rect object and sets initial x and y position
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = self.BLITSURF.get_height() // 2

        #sets up initial y velocity and acceleration
        self.yvel = -5
        self.yaccel = 0.5

    #for when the bird goes too low or high
    def bounceChk(self):
        #if the bird goes too low, reset bird position and velocity and return true
        if self.rect.y - self.image.get_height() > self.BLITSURF.get_height():
            self.rect.y = self.BLITSURF.get_height() // 2
            self.yvel = -5
            return True

        #if the bird goes too high, reset bird position and velocity and return true
        elif (self.rect.y + self.image.get_height() < 0):
            self.rect.y = self.BLITSURF.get_height() // 2
            self.yvel = -5
            return True
        #else return false
        return False

    #Updates the position
    def update(self):
        self.yvel += self.yaccel
        self.rect.y += self.yvel

    #changes the color string and self.image vbased on color parameter
    def change_weapon(self, color):
        self.color = color
        if color == "red":
            self.image = self.rbird
        elif color == "blue":
            self.image = self.bbird
        elif color == "green":
            self.image = self.gbird
        elif color == "yellow":
            self.image = self.ybird
        elif color == "white":
            self.image = self.wbird

