import pygame
from Bullet import Bullet

# spaceShip class
class SpaceShip(object):
    image = pygame.Surface((50, 40))
    color = (255, 0, 0)
    SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
    SPACESHIP_VEL = 5
    MAX_BULLETS = 5
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    FIRE = pygame.K_RCTRL
    WIDTH = 900
    HEIGHT = 600
    hitRect = pygame.Rect(0, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    health = 10
    bullets = []
    targets = []
    velocity = -5
    BULLET_FIRE_SOUND  = None

    def __init__(self, image : pygame.Surface, x, y, color, keys = None):
        super(SpaceShip, self)
        self.image = image
        self.color = color
        self.hitRect = pygame.Rect(x, y, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)
        self.BULLET_FIRE_SOUND  = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')
        if(keys != None): # keys.__len__() == 4
            self.LEFT = keys[0]
            self.RIGHT = keys[1]
            self.UP = keys[2]
            self.DOWN = keys[3]
            self.FIRE = keys[4]
            self.velocity = 5

    def setTargets(self, targets):
        self.targets = targets

    def handle_movement(self, keys_pressed):
        if keys_pressed[self.LEFT] and self.hitRect.x - self.SPACESHIP_VEL > 0:  # LEFT
            self.hitRect.x -= self.SPACESHIP_VEL
        if keys_pressed[self.RIGHT] and self.hitRect.x + self.SPACESHIP_VEL + self.SPACESHIP_WIDTH < self.WIDTH:  # RIGHT
            self.hitRect.x += self.SPACESHIP_VEL
        if keys_pressed[self.UP] and self.hitRect.y - self.SPACESHIP_VEL > 0:  # UP
            self.hitRect.y -= self.SPACESHIP_VEL
        if keys_pressed[self.DOWN] and self.hitRect.y + self.SPACESHIP_VEL + self.SPACESHIP_HEIGHT < self.HEIGHT - 15:  # DOWN
            self.hitRect.y += self.SPACESHIP_VEL
        if keys_pressed[self.FIRE]:
            self.shoot()

    def shoot(self):
        # if LEFT != pygame.K_LEFT:
        #     self.velocity = -5
        if len(self.bullets) < self.MAX_BULLETS:
            self.bullets.append(Bullet(self.hitRect.x + self.hitRect.width / 2, self.hitRect.y, self.color, self.targets, self.velocity))
            self.BULLET_FIRE_SOUND.play()

    def hit(self):
        self.health -= 1
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.hitRect.x, self.hitRect.y, self.hitRect.width, self.hitRect.height))
        win.blit(self.image, (self.hitRect.x, self.hitRect.y))

        for bullet in self.bullets:
            bullet.move()
            if bullet.hitRect.x > self.WIDTH or bullet.hitRect.x < 0 or bullet.hitRect.y > self.HEIGHT or bullet.hitRect.y < 0:
                self.bullets.remove(bullet)
                # TODO destroy bullet
                continue
            if bullet.hit():
                self.bullets.remove(bullet)
                # TODO destroy bullet
                continue
            bullet.draw(win)