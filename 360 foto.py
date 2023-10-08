import pygame

clock = pygame.time.Clock()
WIDTH = 1600
HEIGHT = 900
BACKGROUND = (0, 0, 0)
scale1 = 5
x_position = 0
movingr = False
movingr1 = False
mov = False
dadds = False
eeeee = 6000


screen = pygame.display.set_mode((WIDTH, HEIGHT))

image = pygame.image.load("download.jpg").convert()

image1 = pygame.transform.scale(image, (int(image.get_width() * scale1), int(image.get_height() * scale1)))

asaad = image1.get_width()
print(asaad)
rect = (0, 0), (WIDTH, HEIGHT)

edame = True
while edame:
    print(x_position)
    if movingr:
        x_position -= 5

    if movingr1:
        x_position += 5

    if x_position < -asaad / 2:
        x_position = 0
        print(x_position)

    if x_position > 0:
        x_position = -asaad / 2 + 65
        print(x_position)

    if dadds == True and mov == False:
        eeeee -= 1

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                movingr = False
                mov = False
            if event.key == pygame.K_a:
                movingr1 = False
                mov = False
                dadds = True

    screen.blit((image1), (x_position, -500))
    pygame.display.update()
    clock.tick(60)
