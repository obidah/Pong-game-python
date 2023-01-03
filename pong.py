import pygame
import random
import os
import secondry_windows

pygame.mixer.init()
secondry_windows.start()
pygame.mixer.music.load(os.path.join('sound_effects', 'start.mp3'))
pygame.mixer.music.play()

WIDTH,HEIGHT = 900,600
WHITE = (255,255,255)
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
icon = pygame.image.load(os.path.join('imgs', 'pong_icon.ico'))
pygame.display.set_icon(icon)
pygame.display.set_caption("PONG")
PLAYER_WIDTH = 150
PLAYER_HEIGHT = 25
BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_HIT = pygame.USEREVENT + 1

def draw_window(player_one, player_two, ball):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, (207, 159, 255), player_one)
    pygame.draw.rect(WIN, (207, 159, 255), player_two)
    pygame.draw.rect(WIN, (0,0,0), ball)
    pygame.display.update()

def player_one_movement(keys, player_one):
    if keys[pygame.K_a] and player_one.x - 17 > 0:
        player_one.x -= 17
    if keys[pygame.K_d] and player_one.x + 17 < WIDTH-PLAYER_WIDTH:
        player_one.x += 17

def player_two_movement(keys, player_two):
    if keys[pygame.K_LEFT] and player_two.x - 17 > 0:
        player_two.x -= 17
    if keys[pygame.K_RIGHT] and player_two.x + 17 < WIDTH-PLAYER_WIDTH:
        player_two.x += 17

def ball_movement_up_left(ball, y_random = 5, BALL_X_STRENGTH = 5):
    ball.x += -1*BALL_X_STRENGTH
    ball.y -= y_random

def ball_movement_up_right(ball, y_random = 5, BALL_X_STRENGTH = 5):
    ball.x += BALL_X_STRENGTH
    ball.y -= y_random

def ball_movement_down_left(ball, y_random = 5, BALL_X_STRENGTH = 5):
    ball.x -= BALL_X_STRENGTH
    ball.y += y_random

def ball_movement_down_right(ball, y_random = 5, BALL_X_STRENGTH = 5):
    ball.x += BALL_X_STRENGTH
    ball.y += y_random

def main():
    player_one = pygame.Rect(450-PLAYER_WIDTH//2, 50, PLAYER_WIDTH, PLAYER_HEIGHT)
    player_two = pygame.Rect(450-PLAYER_WIDTH//2, 525, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = pygame.Rect(450-BALL_WIDTH, 300-BALL_HEIGHT, BALL_WIDTH, BALL_HEIGHT)
    
    y_random = 3
    run = True
    clock = pygame.time.Clock()
    PLAYER_ONE_TURN = True
    PLAYER_TWO_TURN = False
    WALL_TOUCH = False
    BALL_X_STRENGTH = 5
    BALL_DIRECTION = ["left", "right"]
    COUNTER = 0 
    BALL_CHOICE = random.choice(BALL_DIRECTION)
    BALL_CHOICE2 = random.choice(BALL_DIRECTION)
    COUNTER2 = 0


    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        kyes_pressed = pygame.key.get_pressed()
        player_one_movement(kyes_pressed, player_one)
        player_two_movement(kyes_pressed, player_two)
        draw_window(player_one, player_two, ball)

        if ball.x > WIDTH - ball.width:
            BALL_X_STRENGTH *= -1
        
        if ball.x < 0:
            BALL_X_STRENGTH *= -1

        if ball.y > HEIGHT-BALL_HEIGHT:
            pygame.mixer.music.load(os.path.join('sound_effects', 'win.mp3'))
            pygame.mixer.music.play()
            secondry_windows.player_above_won()
            run = False

        if ball.y < 0:
            pygame.mixer.music.load(os.path.join('sound_effects', 'win.mp3'))
            pygame.mixer.music.play()
            secondry_windows.player_bottom_won()
            run = False

        if PLAYER_ONE_TURN:
            if COUNTER == 0 or BALL_CHOICE == "left":
                ball_movement_up_left(ball, y_random, BALL_X_STRENGTH)
            else:
                ball_movement_up_right(ball,y_random,BALL_X_STRENGTH)
            if player_one.colliderect(ball):
                BALL_CHOICE = random.choice(BALL_DIRECTION)
                y_random = random.randrange(8,15)
                BALL_X_STRENGTH = random.randrange(1,10)
                PLAYER_TWO_TURN = True
                PLAYER_ONE_TURN = False
                pygame.mixer.music.load(os.path.join('sound_effects', 'player_one_hit.mp3'))
                pygame.mixer.music.play()

        if PLAYER_TWO_TURN:
            if COUNTER2 == 0 or BALL_CHOICE2 == "left":
                ball_movement_down_left(ball, y_random, BALL_X_STRENGTH)
            else:
                ball_movement_down_right(ball, y_random, BALL_X_STRENGTH)
            if player_two.colliderect(ball) :
                BALL_CHOICE2 = random.choice(BALL_DIRECTION)
                y_random = random.randrange(8,15)
                BALL_X_STRENGTH = random.randrange(1,10)
                PLAYER_ONE_TURN = True
                PLAYER_TWO_TURN = False
                pygame.mixer.music.load(os.path.join('sound_effects', 'player_two_hit.mp3'))
                pygame.mixer.music.play()
        
        COUNTER += 1
        COUNTER2 += 1



    pygame.quit()

if __name__ == "__main__":
    main()
