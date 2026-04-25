import pygame

def draw_card(screen, carta, x, y):
    width, height = 200, 300


    # Marco 
    pygame.draw.rect(screen, carta.marco.color, (x, y, width, height), 30)

    # Nombre
    font_title = pygame.font.SysFont("arial", 24, bold=True)
    text_nombre = font_title.render(carta.nombre, True, (0, 0, 0))
    screen.blit(text_nombre, (x + 50, y + 5))

    # Imagen 
    if carta.marco.imagen:
        screen.blit(carta.marco.imagen, (x+10 , y + 30)) 
    
    #  Rank 
    pygame.draw.circle(screen, carta.marco.color, (x + width - 30, y + 30), 30)

    font_rank = pygame.font.SysFont("arial", 28, bold=True)
    text_rank = font_rank.render(carta.marco.rank, True, (0, 0, 0))
    screen.blit(text_rank, (x + width - 40, y + 15))

    # HP 
    pygame.draw.rect(screen, (0, 200, 0), (x, y + height-30 - 20, 60, 50))
    pygame.draw.rect(screen, carta.marco.color, (x, y + height-30 - 20, 60, 50), 10)

    font_stat = pygame.font.SysFont("arial", 20, bold=True)
    hp_text = font_stat.render(f"{carta.vida}", True, (0, 0, 0))
    screen.blit(hp_text, (x + 16, y + height - 37))

    # ATK 
    pygame.draw.rect(screen, (200, 0, 0), (x + width - 60, y + height - 30 - 20, 60, 50))
    pygame.draw.rect(screen,carta.marco.color, (x + width - 60, y + height - 30 - 20, 60, 50), 10)
    atk_text = font_stat.render(f"{carta.atk}", True, (0, 0, 0))
    screen.blit(atk_text, (x + width - 46, y + height - 37))
