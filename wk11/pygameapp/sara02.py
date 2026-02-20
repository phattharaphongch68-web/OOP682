import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame 01")
running = True
clock = pygame.time.Clock()
sara = pygame.image.load("sara-cal1.png")
sara_rect = pygame.Rect(0,0,34,56)
sara_pos  = pygame.Rect(120,150,34,56)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and sara_pos.x+sara_rect.width < 400:
            sara_pos.x += 5
        elif key[pygame.K_a] and sara_pos.x > 0:
            sara_pos.x -= 5
        elif key[pygame.K_w] and sara_pos.y > 0:
            sara_pos.y -= 5
        elif key[pygame.K_s] and sara_pos.y+sara_rect.height < 300:
            sara_pos.y += 5
    clock.tick(90)
    screen.fill((255,255,255))
    font = pygame.font.SysFont(None,36)
    text = font.render(f"{clock.get_fps():.0f}",True,(0,0,0))
    screen.blit(sara,sara_pos,sara_rect)
    screen.blit(text,(300,230))
    
    pygame.display.update()

pygame.quit()