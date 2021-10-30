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

        # barrier
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def jump(self):
        pass
    
    def move(self, up= False, left=False, right=False):
        if up == True:
            self.body.velocity = 0, 100
        if left == True:
            self.body.velocity = -100, 0
        if right == True:
            self.body.velocity = 100, 0
         

    

class Enemies():

    def __init__(self, game, x, y, space, collision_type):
        #self.image = pygame.Surface((w, h))
        #self.image.fill(RED)
        self.game = game
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.space = space
        self.shape = pymunk.Circle(self.body, 50)
        self.shape.density = 1
        self.shape.elasticity = 10
        self.shape.collision_type = collision_type
        self.space.add(self.body, self.shape)
    
    def draw(self):
        x, y = convert_coords(self.body.position)
        pygame.draw.circle(self.game.window, (255, 0, 0), convert_coords(self.body.position), 15)

class Barrier():

    def __init__(self, game, a, b, radius, space, collision_type):
        #self.image = pygame.Surface((w, h))
        #self.image.fill(RED)
        self.game = game
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.space = space
        self.radius = radius
        self.shape = pymunk.Segment(self.body, a, b, self.radius)
        self.shape.density = 1
        self.shape.elasticity = 10
        self.shape.collision_type = collision_type
        self.space.add(self.body, self.shape)
    
    def draw(self):
        pygame.draw.line(self.game.window, (255, 255, 255), convert_coords(self.shape.a), convert_coords(self.shape.b), self.radius)

        
        