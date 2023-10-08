import pygame

clock = pygame.time.Clock()
WIDTH = 1600
HEIGHT = 900
BACKGROUND = (0, 0, 0)
scale1 = 9
x_position = 0
y_position = 0
movingr = False
movingr1 = False
movingr2 = False
movingr3 = False
mov = False
dadds = False



screen = pygame.display.set_mode((WIDTH, HEIGHT))

image = pygame.image.load("download.jpg").convert()


rect = (0, 0), (WIDTH, HEIGHT)

edame = True
while edame:
    image1 = pygame.transform.scale(image, (int(image.get_width() * scale1), int(image.get_height() * scale1)))

    asaad = image1.get_width()
    if movingr:
        x_position -= 10

    if movingr1:
        x_position += 10

    if movingr2:
        y_position -= 10

    if movingr3:
        y_position += 10

    if x_position < -asaad / 2:
        x_position = 0


    if x_position > 0:
        x_position = -asaad / 2 + 65



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            edame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                movingr = True
                mov = True
            if event.key == pygame.K_a:
                movingr1 = True
                mov = True
            if event.key == pygame.K_s:
                movingr2 = True
                mov = True
            if event.key == pygame.K_w:
                movingr3 = True
                mov = True



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                movingr = False
                mov = False
            if event.key == pygame.K_a:
                movingr1 = False
                mov = False
                dadds = True
            if event.key == pygame.K_s:
                movingr2 = False
                mov = False
            if event.key == pygame.K_w:
                movingr3 = False
                mov = False
                dadds = True
            if event.key == pygame.K_e:
                scale1 += 1
                print(scale1)
                pygame.display.update()
            if event.key == pygame.K_q:
                scale1 -= 1
                print(scale1)
                pygame.display.update()


    screen.blit((image1), (x_position, y_position + -1800))
    pygame.display.update()
    clock.tick(60)
