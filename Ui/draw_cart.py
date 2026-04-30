import os
from tkinter import font
import pygame

pygame.font.init()

try:
    font_path = "Ui/fonts/HARLOWSI.TTF" 
    font_rank = "Ui/fonts/Asteroid Blaster.ttf" 
    font_path_ui = "./Ui/fonts/DeutscheZierschrift.ttf"

    font_title = pygame.font.Font(font_path, 18)
    font_rank = pygame.font.Font(font_rank, 18)
    font_stat = pygame.font.Font(font_path, 18)
    font_ui = pygame.font.Font(font_path_ui, 40)
    font_ui_mini = pygame.font.Font(font_path_ui, 18)
except Exception as e:
    print(f"Aviso: No se pudo cargar {font_path}. Usando Arial. Error: {e}")
    pygame.font.init() 
    font_title = pygame.font.SysFont("arial", 18, bold=True)
    font_rank = pygame.font.SysFont("arial", 18, bold=True)
    font_stat = pygame.font.SysFont("arial", 18, bold=True)
    font_ui = pygame.font.SysFont("arial", 40, bold=True)
    font_ui_mini = pygame.font.SysFont("arial", 18, bold=True)

count=0
image_cache = {}

def load_image(path):
    if path not in image_cache:
        image_cache[path] = pygame.image.load(path).convert_alpha()
    return image_cache[path]

def draw_text(surface, text, font,col=(255,255,255), out_col=(0,0,0),pos=(0,0), center=False):

    main_surf = font.render(text, True, col)
    rect = main_surf.get_rect()

    if center:
        rect.center = pos
    else:
        rect.topleft = pos

    # contorno
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        out_surf = font.render(text, True, out_col)
        surface.blit(out_surf, rect.move(dx, dy))

    surface.blit(main_surf, rect)


def draw_card(screen, carta, x, y, info=False, scale=1):
    import random

    base_w, base_h = 200, 300
    width, height = int(base_w * scale), int(base_h * scale)

    # -------------------------
    # 🎬 ANIMACIÓN
    # -------------------------
    offset_x = 0
    offset_y = 0
    anim_scale = 1

    if carta.anim_state == "hurt":
        offset_x = random.randint(-carta.shake, carta.shake)
        offset_y = random.randint(-carta.shake, carta.shake)

    elif carta.anim_state == "heal":
        anim_scale = 1.05

    final_scale = scale * anim_scale

    # -------------------------
    # 🧱 FONDO
    # -------------------------
    fondo = load_image(carta.Characteristics.fondo)
    fondo = pygame.transform.scale(
        fondo,
        (int(base_w * final_scale), int(base_h * final_scale))
    )
    screen.blit(fondo, (x + offset_x, y + offset_y))

    # -------------------------
    # 🏷️ NOMBRE
    # -------------------------
    text_nombre = font_title.render(carta.Characteristics.nombre, True, (0, 0, 0))
    text_rect = text_nombre.get_rect(
        center=(x + width // 2 + offset_x, y + int(20 * scale) + offset_y)
    )
    screen.blit(text_nombre, text_rect)

    # -------------------------
    # 🖼️ IMAGEN
    # -------------------------
    ruta_img = (
        carta.Characteristics.Info
        if info else carta.Characteristics.sprite
    )

    img = load_image(ruta_img)

    w, h = img.get_size()
    img_scale = min(140 / w, 300 / h)

    img = pygame.transform.scale(
        img,
        (
            int(w * img_scale * final_scale),
            int(h * img_scale * final_scale)
        )
    )

    img_rect = img.get_rect(
        center=(
            x + width // 2 + offset_x,
            y + int(155 * scale) + offset_y
        )
    )
    screen.blit(img, img_rect)

    # -------------------------
    # 🏅 RANK
    # -------------------------
    text_rank = font_rank.render(carta.Characteristics.rank, True, (0, 0, 0))
    rank_rect = text_rank.get_rect(
        center=(
            x + width - int(30 * scale) + offset_x,
            y + int(20 * scale) + offset_y
        )
    )
    screen.blit(text_rank, rank_rect)

    # -------------------------
    # 📊 STATS
    # -------------------------
    draw_text(
        screen,
        f"{carta.HP}",
        font_stat,
        (0, 255, 0),
        (0, 0, 0),
        (x + int(15 * scale) + offset_x, y + height - int(25 * scale) + offset_y)
    )

    draw_text(
        screen,
        f"{carta.Atk}",
        font_stat,
        (255, 0, 0),
        (0, 0, 0),
        (x + width - int(35 * scale) + offset_x, y + height - int(25 * scale) + offset_y)
    )

    # -------------------------
    # 📊 STATS
    # -------------------------
    color_contorno = (0, 0, 0)

    draw_text(
        screen,
        f"{carta.HP}",
        font_stat,
        (0, 255, 0),
        color_contorno,
        (x + 15 + offset_x, y + height - 25 + offset_y)
    )

    draw_text(
        screen,
        f"{carta.Atk}",
        font_stat,
        (255, 0, 0),
        color_contorno,
        (x + width - 32 + offset_x, y + height - 25 + offset_y)
    )

def draw_item(screen, item, x, y, cantidad, img_size=None, info=False, scale=1):

    base_dir = os.path.dirname(__file__)
    
    img_dir = os.path.join(base_dir, "items")
    ruta_item = os.path.join(img_dir, f"{item}.png")

    if info:
        img_dir = os.path.join(base_dir, "items_info")
        ruta_item = os.path.join(img_dir, f"{item}_info.png")

    try:
        img = load_image(ruta_item)
    except:
        print("Error cargando:", ruta_item)
        return

    ITEM_W, ITEM_H = img_size if img_size else (200, 300)
    ITEM_W = int(ITEM_W * scale)
    ITEM_H = int(ITEM_H * scale)
    img = pygame.transform.scale(img, (ITEM_W, ITEM_H))
    screen.blit(img, (x, y))

    text_x = x + ITEM_W - 150
    text_y = y + ITEM_H - 40

    draw_text(
       screen,"x"+ f"{cantidad}",font_stat, (255, 255, 255),(0, 0, 0), (text_x, text_y)
    )

def draw_options(screen, item, x, y, offset_y=0, player=False):

    base_dir = os.path.dirname(__file__)
    img_dir = os.path.join(base_dir, "options")
    ruta_item = os.path.join(img_dir, f"{item}.png")

    try:
        img = load_image(ruta_item)
    except:
        print("Error cargando:", ruta_item)
        return

    ITEM_W, ITEM_H = 80, 130
    img = pygame.transform.scale(img, (ITEM_W, ITEM_H))

    if player:
        match item:
            case "Piedra": number = "1"
            case "Papel": number = "2"  
            case "Tijera": number = "3"

        draw_text(screen,number,font_ui, (255, 255, 255),(0, 0, 0), (x + 30, y + ITEM_H - 5 + offset_y)
    )

    screen.blit(img, (x, y + offset_y))


def draw_pocion(screen, pocion, x, y, cantidad,):

    base_dir = os.path.dirname(__file__)
    img_dir = os.path.join(base_dir, "items")
    ruta_item = os.path.join(img_dir, f"{pocion}_g.png")

    try:
        img = load_image(ruta_item)
    except:
        print("Error cargando:", ruta_item)
        return

    ITEM_W, ITEM_H = 30, 45
    img = pygame.transform.scale(img, (ITEM_W, ITEM_H))
    screen.blit(img, (x, y))

    Teclas={
        "Minipocion":"Q",
        "Pocion":"W",
        "Superpocion":"E",
        "Hiperpocion":"R"}
    

    draw_text(screen,Teclas.get(pocion),font_ui_mini, (255, 255, 255),(0, 0, 0), (x + 5 , y + ITEM_H + 10 ))
    draw_text(screen,f"x{cantidad}",font_stat, (255, 255, 255),(0, 0, 0), (x + 28 , y + ITEM_H - 20 ))


    