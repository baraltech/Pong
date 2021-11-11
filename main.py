import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 1280, 720

FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))

S = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")
C = pygame.time.Clock()

player = pygame.Rect(0, 0, 10, 100)
player.center = (WIDTH-100, HEIGHT/2)

opponent = pygame.Rect(0, 0, 10, 100)
opponent.center = (100, HEIGHT/2)

player_score, opponent_score = 0, 0

ball = pygame.Rect(0, 0, 20, 20)
ball.center = (WIDTH/2, HEIGHT/2)

y_speed = 1
x_speed = 1

while True:
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -= 2
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom < HEIGHT:
            player.bottom += 2
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if ball.y >= HEIGHT:
        y_speed = -1
    if ball.y <= 0:
        y_speed = 1
    if ball.x >= player.x - 15 and ball.y in range(player.top, player.bottom):
        x_speed = -1
    if ball.x <= opponent.x + 15 and ball.y in range(opponent.top, opponent.bottom):
        x_speed = 1
    if ball.x <= 0 or ball.x < opponent.x and ball.y == HEIGHT:
        player_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
    if ball.x >= WIDTH or ball.x > player.x and ball.y == HEIGHT:
        opponent_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)

    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")

    ball.x += x_speed
    ball.y += y_speed

    if opponent.y < ball.y:
        opponent.top += 1
    if opponent.bottom > ball.y:
        opponent.bottom -= 1

    S.fill('black')
    pygame.draw.rect(S, "white", player)
    pygame.draw.rect(S, "white", opponent)
    pygame.draw.circle(S, "white", ball.center, 10)

    S.blit(player_score_text, (WIDTH/2+50, 50))
    S.blit(opponent_score_text, (WIDTH/2-50, 50))

    pygame.display.update()
    C.tick(360)