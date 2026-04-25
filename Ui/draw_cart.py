import pygame

import pygame

pygame.font.init()

try:
    font_path = "Ui/fonts/HARLOWSI.TTF" 
    font_rank = "Ui/fonts/Asteroid Blaster.ttf" 
    font_title = pygame.font.Font(font_path, 18)
    font_rank = pygame.font.Font(font_rank, 18)
    font_stat = pygame.font.Font(font_path, 18)
except Exception as e:
    print(f"Aviso: No se pudo cargar {font_path}. Usando Arial. Error: {e}")
    pygame.font.init() 
    font_title = pygame.font.SysFont("arial", 18, bold=True)
    font_rank = pygame.font.SysFont("arial", 18, bold=True)
    font_stat = pygame.font.SysFont("arial", 18, bold=True)


image_cache = {}

def load_image(path):
    if path not in image_cache:
        image_cache[path] = pygame.image.load(path).convert_alpha()
    return image_cache[path]

def draw_text_outline(surface, text, font, col, out_col, pos):
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        out_surf = font.render(text, True, out_col)
        surface.blit(out_surf, (pos[0] + dx, pos[1] + dy))
    main_surf = font.render(text, True, col)
    surface.blit(main_surf, pos)

def draw_card(screen, carta, x, y):
    width, height = 200, 300
    
    # FONDO
    fondo = load_image(carta.marco.ruta_fondo)
    fondo = pygame.transform.scale(fondo, (width, height))
    screen.blit(fondo, (x, y))

    # NOMBRE (Usando Nicholas)
    text_nombre = font_title.render(carta.nombre, True, (0, 0, 0))
    text_rect = text_nombre.get_rect(center=(x + 80, y + 20)) # Centrado a 100
    screen.blit(text_nombre, text_rect)

    # IMAGEN
    img = load_image(carta.marco.ruta_imagen)
    w, h = img.get_size()
    scale = min(140 / w, 300 / h)
    img = pygame.transform.scale(img, (int(w * scale), int(h * scale)))
    img_rect = img.get_rect(center=(x + 100, y + 155))
    screen.blit(img, img_rect)

    # RANK (Usando Nicholas)
    text_rank = font_rank.render(carta.marco.rank, True, (0, 0, 0))
    rank_rect = text_rank.get_rect(center=(x + width - 32, y + 20))
    screen.blit(text_rank, rank_rect)

    # STATS CON CONTORNO
    color_contorno = (0, 0, 0)
    
    # HP (Verde)
    draw_text_outline(screen, f"{carta.vida}", font_stat, (0, 255, 0), color_contorno, (x + 15, y + height - 25))
    
    # ATK (Rojo)
    draw_text_outline(screen, f"{carta.atk}", font_stat, (255, 0, 0), color_contorno, (x + width - 32, y + height - 25))
