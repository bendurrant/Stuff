from bulletClassCloud import *
import pygame

class Weapon():
    def __init__(self, p, a):

        #instantiates bullet list group used for collision detection
        self.bullet_list = pygame.sprite.Group()
        #uses the allspriteslist and player
        self.all_list = a
        self.player = p

    #this function shoots a different type of bullet depending on your bird color
    def shoot(self):


        if self.player.color == "white":
            #shoots the bullet
            b = Bullet()
            #tells the bullet to appear at the middle of the bird up and down but just slightly
            #in front of it
            b.rect.centery = self.player.rect.centery
            b.rect.x = self.player.rect.x + 25
            #adds the fired bullet to lists
            self.bullet_list.add(b)
            self.all_list.add(b)

        elif self.player.color == "red":
            #creates two bullets one that goes upwards and one that goes downwards
            b1 = Red_Bullet(1)
            b2 = Red_Bullet(-1)

            b1.rect.centery = self.player.rect.centery
            b2.rect.centery = self.player.rect.centery
            b1.rect.x = self.player.rect.x + 25
            b2.rect.x = self.player.rect.x + 25
            self.bullet_list.add(b1, b2)
            self.all_list.add(b1, b2)

        elif self.player.color == "blue":
            b = Blue_Bullet()
            b.rect.centery = self.player.rect.centery
            b.rect.x = self.player.rect.x + 25
            self.bullet_list.add(b)
            self.all_list.add(b)

        if self.player.color == "yellow":
            b = Yellow_Bullet()
            b.rect.centery = self.player.rect.centery
            b.rect.x = self.player.rect.x + 25
            self.bullet_list.add(b)
            self.all_list.add(b)

        if self.player.color == "green":
            b = Green_Bullet()
            b.rect.centery = self.player.rect.centery
            b.rect.x = self.player.rect.x + 25
            self.bullet_list.add(b)
            self.all_list.add(b)