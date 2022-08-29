import pygame
from random import randrange
# размер экрана
RES = 700
SIZE = 50
# создание переменых
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 1
shake = [(x, y)]
dx, dy = 0, 0
fps = 1
score = 0
# pygame.init()
pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)

while True:
    # цвета нашей игры
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1))) for i, j in shake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    # вывод счета на экран
    render_score = font_score.render(f'Очки: {score}', True, pygame.Color('red'))
    sc.blit(render_score, (10, 10))
    # оброботка змеи
    x += dx * SIZE
    y += dy * SIZE
    shake.append((x, y))
    shake = shake[-length:]
    # оброботка яблоки
    if shake[-1] == apple:
        apple = randrange(SIZE, RES-SIZE, SIZE), randrange(SIZE, RES-SIZE, SIZE)
        length += 1
        score += 1
        # + скорость
        if fps < 10:
            fps += 1
    # вывод на экран all()
    pygame.display.flip()
    clock.tick(fps)
    for event in pygame.event.get():
        # кнопка выхода
        if event.type == pygame.QUIT:
            exit()
        # движение змейки
        elif event.type == pygame.KEYDOWN:
            # направо
            if event.key == pygame.K_d:
                dx, dy = 1, 0
            # налево
            elif event.key == pygame.K_a:
                dx, dy = -1, 0
            # наверх
            elif event.key == pygame.K_w:
                dx, dy = 0, -1
            # вниз
            elif event.key == pygame.K_s:
                dx, dy = 0, 1