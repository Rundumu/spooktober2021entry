from pygame.sprite import Sprite
from settings import *
from sprites import *
#from spritesheet import Spritesheet
from os import path
import pygame
import pymunk


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

        

    def new_game(self):

        # sprites group
        self.sprites = pygame.sprite.Group()

        # player
        self.player = Player(self, WIDTH / 2, HEIGHT - 10, self.space)
        self.sprites.add(self.player)

        # platforms
        self.plat = Platform(WIDTH / 2, HEIGHT / 2, 100, 50, self.space)
        self.sprites.add(self.plat)

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
                if event.key == pygame.K_UP:
                    self.player.move(up=True)



    def game_over():
        pass

    def start():
        pass


g = Game()

while g.running:
    g.new_game()

pygame.quit()