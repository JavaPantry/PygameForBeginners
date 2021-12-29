import pygame
import os
from spaceShip import SpaceShip

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

GRENADE_SOUND = pygame.mixer.Sound('Assets/Small-Grenade-Explosion.mp3') 

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
HIT = pygame.USEREVENT + 3

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


redShip     = SpaceShip(RED_SPACESHIP, 700, 200, (255, 0, 0))
yellowShip  = SpaceShip(YELLOW_SPACESHIP, 100, 200, (255, 255, 0), [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_LCTRL])
redShip.setTargets([yellowShip])
yellowShip.setTargets([redShip])

# def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
def draw_window():
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    yellow_health_text = HEALTH_FONT.render("Yellow Health: " + str(yellowShip.health), 1, YELLOW)
    WIN.blit(yellow_health_text, (10, 50))
    red_health_text = HEALTH_FONT.render("Red Health: " + str(redShip.health), 1, RED )
    WIN.blit(red_health_text, (WIDTH - yellow_health_text.get_width() - 10, 50))
    
    redShip.draw(WIN)
    yellowShip.draw(WIN)

    pygame.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == HIT:
                GRENADE_SOUND.play()

        winner_text = ""
        if redShip.health <= 0:
            winner_text = "Yellow Wins!"

        if yellowShip.health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        redShip.handle_movement(keys_pressed)
        yellowShip.handle_movement(keys_pressed)
        draw_window()

if __name__ == "__main__":
    main()
