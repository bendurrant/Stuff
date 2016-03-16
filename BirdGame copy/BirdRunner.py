#Friendly Foes
#by: Ben Durrant, Cam Jackson, and Emilee Choate
#EAE 1410 Fall 2014


import pygame, sys, random

#import classes
from BirdClass import bird
from WeaponClass import *
from SpawnerClass import *
from birdScoreClass import *

# initiate music
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.mixer.init()

#initiate pygame
pygame.init()

#create window
size = (1200, 670)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Friendly Foes")
done = False
#instantiate clock
clock = pygame.time.Clock()


go = False

#instantiates objects 
p1 = bird(screen)
allSprites = pygame.sprite.Group(p1)
spawner = Spawner(p1, allSprites, screen)
weapon = Weapon(p1, allSprites)
score = BirdScore(screen)
background = pygame.transform.scale(pygame.image.load("background.jpg").convert_alpha(), (1200, 670))

#Sound objects
theme = pygame.mixer.music.load('theme.wav')
loseLife = pygame.mixer.Sound("loselife.wav")
catScream = pygame.mixer.Sound("cat.wav")
birdcall = pygame.mixer.Sound("birdcall.wav")

#Plays constant theme music loop
pygame.mixer.music.play(loops = -1, start = 0.0)


#Main Game Loop
def main():

    while not done:

        screen.fill((125, 125, 255))
        #quit program 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #If mouse is clicked, bird's y-axis velocity changes    
            if event.type == pygame.MOUSEBUTTONDOWN:
                p1.yvel -= 10
                go = True
            #If space is pressed, bird fire's bullet
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    weapon.shoot()

        
        for bullet in weapon.bullet_list:

            hitList = pygame.sprite.spritecollide(bullet, spawner.enemies_list, False)
            #allows blue bird's bullets to pass through enemies            
            if len(hitList) > 0:
                if bullet.hitdie:
                    bullet.kill()
                #if cat is hit by bullet, cat is removed and sound is played.
                for hit in hitList:
                    hit.kill()
                    catScream.play()

            #counts cats added to the hitList, and add score per cat
            score.addPoints(hitList)
            hiting = pygame.sprite.spritecollide(bullet, spawner.upgrade, False)
            #If the player hits a colored bird upgrade, it will change the weapon type and remove the colored bird from play. 
            for hit in hiting:
                if not (hit.color == "None"):
                    p1.change_weapon(hit.color)
                    hit.kill()
                    birdcall.play()

        #if player is hit, player loses a life
        for e in spawner.enemies_list:
            p_hit = pygame.sprite.collide_mask(e, p1)
            if p_hit:
                e.kill()
                score.loseLife()
                loseLife.play()

        #If the player goes beyond the screen, they lose a life and spawn at the screen center.
        if p1.bounceChk():
            score.loseLife()
            loseLife.play()


        playing = score.gameOver()

        #If game over: 
        if playing == 1:
            for e in spawner.enemies_list:
                e.kill()
            for b in weapon.bullet_list:
                b.kill()
            for bird in spawner.upgrade:
                bird.kill()
            pygame.mixer.music.stop()
            #Starts new game if 'y' is pressed on game over screen, and brings player back to the title screen.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    pygame.mixer.music.play()
                    score.life = 10
                #If 'n' is pressed, the program quits
                if event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

        #Changes from title screen to either game state or instruction screen.
        elif playing == 2:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score.newGame()
                    spawner.reset()
                    p1.change_weapon("white")
                    catScream.play()
                elif event.key == pygame.K_i:
                    score.life = 27
        #Changes from instruction screen to game state 
        elif playing == 3:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score.newGame()
                    spawner.reset()
                    p1.change_weapon("white")
                    catScream.play()
        #If not on title screen, instruction screen, or game over screen, game is in game state. 
        else:
            allSprites.update()
            spawner.spawnChk()
            spawner.weapSpawnCheck()
            screen.blit(background, (0, 0))
            allSprites.draw(screen)
            score.displayLife()
            score.displayScore()
        pygame.display.flip()
        clock.tick(60)
        #print(clock.get_fps())


if __name__ == '__main__':main()
            
