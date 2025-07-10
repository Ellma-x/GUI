import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
image = pygame.image.load('roblox.png')
image = pygame.transform.scale(image, (200,200))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False


    screen.fill((58,58,58))
    screen.blit(image, (150,150))

    pygame.display.update()


pygame.quit()
