#bulletClassCloud
#11/19/14




import pygame, math

pygame.init()


class Bullet(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("bullet2.png" ).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.xvel = 10
        self.yvel = 0
        self.hitdie = True

    #this function updates the bullets on the screen to make them appear to fire
    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        #kills the bullet as it leaves the screen
        if self.rect.x > 1200:
            self.kill()
        #bounces the bullets off the top or bottom
        if self.rect.y < 0 or self.rect.y > 670 - self.image.get_height():
            self.yvel *= -1


class Red_Bullet(Bullet):
    def __init__(self,  direction):
        super().__init__()
        #takes in the direction of the bullet and then shoots it up or down from there
        self.yvel = 5 * direction

class Blue_Bullet(Bullet):
    def __init__(self):
        super().__init__()
        #this boolean makes the bullet not disappear once it hits an enemy
        self.hitdie = False

class Green_Bullet(Bullet):
    def __init__(self):
        super().__init__()
        #makes the bullet image bigger
        self.image = pygame.image.load("bullet2.png" ).convert_alpha()
        self.rect = self.image.get_rect()

class Yellow_Bullet(Bullet):
    def __init__(self):
        super().__init__()
        self.time = 0.0

    #makes the bullets shoot in an upward spiral like motion.
    def update(self):
        self.rect.x += self.xvel + 20 * math.cos(2 * self.time / 3)
        self.rect.y += 20 * math.sin(-2 * self.time / 3)
        self.time += 0.3
        if self.rect.x > 1200:
            self.kill()


