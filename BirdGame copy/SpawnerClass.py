from enemyClass import *
import time

#class that handles the spawning of enemies
class Spawner():
    def __init__(self, p, a, bs):
        #sets player, list of all sprites, and blit surface objects
        self.player = p
        self.all_list = a
        self.screen = bs

        #the list of all the active enemies
        self.enemies_list = pygame.sprite.Group()

        #spawn patterns based on amount of time in game
        time.clock()

        #time at which the spawner last spawned an enemy
        self.last_spawn = 0.0

        #time between enemy spawns
        self.spawn_rate = 1.5

        #represents how many enemies will spawn at a time
        self.level = 1

        #time at which the spawner last spawned a power up enemy
        self.lastWepSpawn = 0

        #group of upgrade enemies
        self.upgrade = pygame.sprite.Group()

    #spawns enemies at the appropriate time
    def spawnChk(self):
        #gets current time
        now = time.clock()

        #time since last spawn
        time_diff = now - self.last_spawn

        #if the time since the last spawn is greater than self.spawn_rate
        if self.spawn_rate < time_diff:
            #
            self.last_spawn = now
            #spawns a number of random enemies equal to self.level
            for i in range(self.level):
                self.rand_enemy()
        #this means the time between spawns gets slowly shorter
        self.spawn_rate -= 0.0005

        #Once it reaches a certain threshold, increase the level
        if self.spawn_rate < 0.1:
            self.level_up()
        #print(self.spawn_rate)

    #resets the spawner
    def reset(self):
        self.last_spawn = 0.0
        self.spawn_rate = 1.5
        self.level = 1

    #spawns a random enemy into the game
    def rand_enemy(self):
        i = random.randrange(0, 10)

        if i == 0:
            e = Straight_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 1:
            e = Homing_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 2:
            e = Accel_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 3:
            e = Bounce_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 4:
            e = Unbounce_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 5:
            e = Wave_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 6:
            e = Swirl_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 7:
            e = Herkyjerk_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 8:
            e = Diagonal_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)
        elif i == 9:
            e = Stop_Enemy(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.enemies_list)


    def level_up(self):
        #resets spawn rate
        self.spawn_rate = 1

        #increases level to a max of 9
        if self.level < 9:
            self.level += 1

    #spawns upgrade enemies at apropriate times
    def weapSpawnCheck(self):
        now = time.clock()

        spawnRate = 30
        time_diff = now - self.lastWepSpawn
        if spawnRate < time_diff:
            self.lastWepSpawn = now

            self.randBirdWeap()

    #spawns random upgrade enemy
    def randBirdWeap(self):

        i = random.randrange(0,4)
        if i == 0:
            e = RedBird(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.upgrade)

        elif i == 1:
            e = GreenBird(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.upgrade)

        elif i == 2:
            e = BlueBird(self.screen, self.player)
            e.add(self.all_list)
            e.add(self.upgrade)
        elif i == 3:
            e = YellowBird(self.screen,self.player)
            e.add(self.all_list)
            e.add(self.upgrade)




