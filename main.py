from pygame.sprite import Sprite
from settings import *
from sprites import *
#from spritesheet import Spritesheet
from os import path
import pygame
import pymunk
import random


class Game():
    
    def __init__(self):


        pygame.init()
        pygame.mixer.init()

        self.running = True
        self.clock = pygame.time.Clock()
        #self.camera = Camera(WIDTH, HEIGHT)
        self.ring_count = 0
        self.window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.space = pymunk.Space()
        self.space.gravity = 0, -50
        self.handler = self.space.add_collision_handler(1, 2)

        

    def new_game(self):

        # groups
        self.sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()

        # player
        self.player = Player(self, WIDTH / 2, 150, self.space, 1)
        self.sprites.add(self.player)

        # platforms

        
        # barriers
        self.left = Barrier(self, (0, HEIGHT), (0, 0), 20, self.space, 2)
        self.top = Barrier(self, (0, 0), (1000, WIDTH), 20, self.space, 2)
        self.bottom = Barrier(self, (10, HEIGHT), (0, 0), 20, self.space, 2)
        self.right = Barrier(self, (10, HEIGHT), (0, 0), 20, self.space, 2)


        # enemies
        width = random.randrange(50, 100)

        self.enemies = [Enemies(self, 
                        random.randrange(50, WIDTH-width),
                        random.randrange(700, 750),
                        self.space,
                        2) for i in range(10)]
            
        
        self.run()

    def run(self):
        self.playing = True
        
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def draw(self):
        # draw
        self.window.fill(BLACK)

        [e.draw() for e in self.enemies]
        self.left.draw()
        self.top.draw()


        self.sprites.draw(self.window)

        pygame.display.flip()

    def update(self):     
        print(self.player.rect.top)
        if self.player.rect.top <= 100:
            self.player.rect.y += max(abs(10), 2)

            for plat in self.plats:
                plat.rect.y += max(abs(10), 2)
                if plat.rect.top >= HEIGHT:
                    plat.kill()



        self.handler.begin = collide

        self.sprites.update()

        self.clock.tick(FPS)
        self.space.step(1/FPS)

             
        

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move(right=True)
                if event.key == pygame.K_LEFT:
                    self.player.move(left=True)
                if event.key == pygame.K_SPACE:
                    self.player.move(up=True)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.move(up=False)                



    def game_over():
        pass

    def start():
        pass


g = Game()

while g.running:
    g.new_game()

pygame.quit()