import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame 01")
running = True
clock = pygame.time.Clock()
sara = pygame.image.load("sprite_PP.png").convert_alpha()
sara_scale = pygame.transform.scale(sara,(150,150))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(90)
    screen.fill((255,255,255))
    font = pygame.font.SysFont(None,36)
    text = font.render(f"{clock.get_fps():.0f}",True,(0,0,0))
    screen.blit(sara_scale,(120,100))
    screen.blit(text,(300,230))
    
    pygame.display.update()

pygame.quit()