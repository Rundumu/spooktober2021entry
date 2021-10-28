import pygame, pymunk
from settings import *
from pymunk import Vec2d


def convert_coords(point):
    return point[0], HEIGHT - point[1]

def collide(arbiter, space, data):
    print("hello")
    return True

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y, space, collision_type):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vel = [0, 0]
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.jumping = False
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.rect.x, self.rect.y = self.body.position
        self.space = space
        self.shape = pymunk.Circle(self.body, 50)
        self.shape.density = 10
        self.shape.elasticity = 0
        self.shape.collision_type = collision_type
        self.space.add(self.body, self.shape)


    def update(self):

        # gravity 
        self.rect.x, self.rect.y = convert_coords(self.body.position)

    def jump(self):
        pass
    
    def move(self, up= False, left=False, right=False):
        if up == True:
            self.body.velocity = 0, 100
        if left == True:
            self.body.velocity = -100, 0
        if right == True:
            self.body.velocity = 100, 0
    

   


        

        
class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, space, collision_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = x, y
        self.rect.x, self.rect.y = self.body.position
        self.space = space
        self.vs = [(-w/2,-h/2), ((w/2),-(h/2) + 10), (w/2,h/2), ((-w/2),(h/2) + 10)]
        self.shape = pymunk.Poly(self.body, self.vs)
        self.shape.density = 100
        self.shape.friction = 2.0
        self.shape.collision_type = collision_type
        self.space.add(self.body, self.shape)


    def update(self):
        self.rect.x, self.rect.y = convert_coords(self.body.position)

class Ground(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
    def update(self):
        pass