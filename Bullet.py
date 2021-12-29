import pygame

class Bullet:
    velocity = 5
    color = None
    hitRect = pygame.Rect( 0 , 0 , 5, 2)
    targets = []
    HIT = pygame.USEREVENT + 3

    def __init__(self, x, y, color, targets, velocity = 5):
        self.color = color
        self.velocity = velocity
        self.targets = targets
        self.hitRect = pygame.Rect( x , y , 5, 2)
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.hitRect.x, self.hitRect.y, self.hitRect.width, self.hitRect.height))
    
    def move(self):
        # self.hitRect.y -= self.velocity
        self.hitRect.x += self.velocity
    
    def hit(self):
        for target in self.targets:
            if target.hitRect.colliderect(self.hitRect):
                pygame.event.post(pygame.event.Event(self.HIT))
                target.hit()
                return target
