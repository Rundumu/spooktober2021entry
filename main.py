from math import e
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
        self.plats = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()

        # player
        self.player = Player(self, WIDTH / 2, HEIGHT - 10, self.space, 1)
        self.sprites.add(self.player)

        # platforms
        self.ground = Platform(0, 50, WIDTH, 50)

        self.sprites.add(self.ground)
        self.floor.add(self.ground)

        for i in range(6):
            width = random.randrange(50, 100)
            p = Platform(random.randrange(200, WIDTH-width), 
                        random.randrange(100, HEIGHT - 50), 
                        random.randrange(100, 150),
                        50,
                        self.space,
                        2)

            self.sprites.add(p)
            self.plats.add(p)

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
        
        self.sprites.draw(self.window)

        pygame.display.flip()

    def update(self):     
        
        hits = pygame.sprite.spritecollide(self.player, self.floor, False)
        
        if hits:
            if self.player.rect.bottom >= hits[0].rect.top:
                self.player.rect.bottom = hits[0].rect.top


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