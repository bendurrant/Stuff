import pygame
import random
import math

#the base class for the enemies. Children override the move method to move in different patterns
class Enemy(pygame.sprite.Sprite):
    def __init__(self, blitSurf, p):
        #initializes sprite
        pygame.sprite.Sprite.__init__(self)

        #sets base image
        self.image = pygame.image.load("Cats/cat1.png").convert_alpha()

        #sets up rect object
        self.rect = self.image.get_rect()

        #sets random y position
        self.rect.y = random.randrange(blitSurf.get_height() - self.image.get_height())

        #enemies start just offscreen to the right
        self.rect.x = blitSurf.get_width()

        #blit surface and bird object used for various methods
        self.BLITSURF = blitSurf
        self.player = p

        #base velocities
        self.yvel = 0.0
        self.xvel = -5.0

        #for power up enemies, this will be a color
        self.color = "None"


    #called every frame
    def update(self):
        self.move()
        self.end_check()

    #if it is off the screen, kill it
    def end_check(self):
        if self.rect.x < -1 * self.image.get_width():
            self.kill()

    #overwritten for different movement patterns
    def move(self):
         self.rect.x += self.xvel

#moves straight left at constant velocity
class Straight_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.enemy_num = 0
        self.image = pygame.image.load("Cats/cat1.png").convert_alpha()

    def move(self):
        self.rect.x += self.xvel

#moves a fraction of the distance between the player and this enemy every frame, so it homes in on the player
class Homing_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.enemy_num = 1

        self.image = pygame.image.load("Cats/cat2.png").convert_alpha()

    def move(self):
        self.rect.x += self.xvel
        self.rect.y += (self.player.rect.centery - self.rect.centery) // 30

#accelerates at a constant rate
class Accel_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.enemy_num = 2
        self.image = pygame.image.load("Cats/cat3.png").convert_alpha()

    def move(self):
        self.xvel += -0.5
        self.rect.x += self.xvel

#bounces off the bottom of the screen and moves kind of like the player
class Bounce_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.image = pygame.image.load("Cats/cat4.png").convert_alpha()
        self.yaccel = self.player.yaccel
        self.enemy_num = 3

    def move(self):
        self.rect.x += self.xvel
        self.yvel += self.yaccel
        self.rect.y += self.yvel
        self.bounceChk(self.player.BLITSURF)

    def bounceChk(self, screenSurf):
        if self.rect.y + self.image.get_height() > screenSurf.get_height():
            self.rect.y = screenSurf.get_height() - self.image.get_height()
            self.yvel *= -1

#like the Bounce_Enemy but for the top of the screen
class Unbounce_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.image = pygame.image.load("Cats/cat5.png").convert_alpha()
        self.yaccel = -1 * self.player.yaccel
        self.enemy_num = 4

    def move(self):
        self.rect.x += self.xvel
        self.yvel += self.yaccel
        self.rect.y += self.yvel
        self.bounceChk(self.player.BLITSURF)

    def bounceChk(self, screenSurf):
        if self.rect.y < 0:
            self.rect.y = 0
            self.yvel *= -1

#moves in a sine wave
class Wave_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.image =pygame.image.load("Cats/cat6.png").convert_alpha()
        self.time = 0.0
        self.enemy_num = 5

    def move(self):
        self.rect.x += self.xvel
        self.rect.y += 15 * math.sin(2 * self.time / 3)
        self.time += 0.3

#moves in circle plus a constant x velocity, creating a kind of swirling motion
class Swirl_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.image = pygame.image.load("Cats/cat7.png").convert_alpha()
        self.time = 0.0
        self.enemy_num = 6

    def move(self):
        self.rect.x += self.xvel + 20 * math.cos(2 * self.time / 3)
        self.rect.y += 20 * math.sin(2 * self.time / 3)
        self.time += 0.3

#moves straight left, up, left again, and down, in that order and then repeats
class Herkyjerk_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.image = pygame.image.load("Cats/cat8.png").convert_alpha()
        self.time = 0.0
        self.xvel = -15.0
        self.enemy_num = 7

    def move(self):
        if self.time < 1:
            self.rect.x += self.xvel

        elif self.time < 2:
            self.rect.y += self.xvel

        elif self.time < 3:
            self.rect.x += self.xvel

        elif self.time < 4:
            self.rect.y -= self.xvel

        else:
            self.time = 0.0

        self.time += 0.05

#moves diagonally and bounces off the top and bottom of the screen
class Diagonal_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.image =pygame.image.load("Cats/cat9.png").convert_alpha()
        self.yvel = self.xvel * random.randrange(-1, 2, 2)
        self.enemy_num = 8


    def move(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.bounceChk(self.player.BLITSURF)

    def bounceChk(self, screenSurf):
        if self.rect.y + self.image.get_height() > screenSurf.get_height():
            self.rect.y = screenSurf.get_height() - self.image.get_height()
            self.yvel *= -1

        if self.rect.y < 0:
            self.rect.y = 0
            self.yvel *= -1

#stops at a random point on the screen then continues
class Stop_Enemy(Enemy):
    def __init__(self, bs, p):
        super().__init__(bs, p)
        self.image = pygame.image.load("Cats/cat10.png").convert_alpha()
        self.time = 0.0
        self.stopx = random.randrange(self.player.rect.x + self.player.image.get_width() + 1, self.BLITSURF.get_width())
        self.stopped = False
        self.xvel *= 3
        self.enemy_num = 9

    def move(self):
        if self.rect.x <= self.stopx and not self.stopped and self.time < 5:
            self.time += 0.1
            if self.time > 5:
                self.stopped = True

        else:
            self.rect.x += self.xvel

#The following are subclasses for the power up enemies. They should probably have their own parent class but don't for some reason.
#All of them fall from the top of the screen to the bottom at constant velocity.
class RedBird(Enemy):
    def __init__(self, bs, p):
        super(). __init__(bs,p)
        self.image = pygame.image.load("Birds/rb4.png").convert_alpha()
        self.color = "red"
        self.enemy_num = 1000000000
        self.rect.x = self.BLITSURF.get_width() // 2
        self.rect.y = -1 * self.image.get_height()

    def move(self):
        self.rect.y += 4
        if self.rect.y >= self.BLITSURF.get_height():
            self.kill()

class GreenBird(Enemy):
    def __init__(self, bs, p):
        super(). __init__ (bs,p)
        self.image = pygame.image.load("Birds/gb4.png").convert_alpha()
        self.color = "green"
        self.enemy_num = 30000000
        self.rect.x = self.BLITSURF.get_width() // 2
        self.rect.y = -1 * self.image.get_height()

    def move(self):
        self.rect.y += 4
        if self.rect.y >= self.BLITSURF.get_height():
            self.kill()

class BlueBird(Enemy):
    def __init__(self,bs,p):
        super(). __init__(bs,p)
        self.image = pygame.image.load("Birds/bb4.png").convert_alpha()
        self.color = "blue"
        self.enemy_num = 3939399393939339393
        self.rect.x = self.BLITSURF.get_width() // 2
        self.rect.y = -1 * self.image.get_height()

    def move(self):
        self.rect.y += 4
        if self.rect.y >= self.BLITSURF.get_height():
            self.kill()

class YellowBird(Enemy):
    def __init__(self,bs,p):
        super(). __init__(bs,p)
        self.image = pygame.image.load("Birds/yb4.png").convert_alpha()
        self.color = "yellow"
        self.enemy_num = 25237472364193248902349
        self.rect.x = self.BLITSURF.get_width() // 2
        self.rect.y = -1 * self.image.get_height()

    def move(self):
        self.rect.y += 4
        if self.rect.y >= self.BLITSURF.get_height():
            self.kill()


