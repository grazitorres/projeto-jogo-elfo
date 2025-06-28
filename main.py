import pgzrun 
from pygame.Rect import Rect
import random

# Tamanho da tela do jogo
WIDTH = 480
HEIGHT = 352
TITLE = "A fuga de Lorien" 

TILE_SIZE = 16

#Cores
WHITE = (255, 255, 255) #Para as letras
BLACK = (0, 0, 0)
MENU_BG_COLOR = (144, 238, 144) # Verde claro
STORY_BG_COLOR = (70, 40, 0) # Marrom
GAME_BG_COLOR = (0, 0, 0)
WALL_COLOR = (139, 69, 19) 



HERO_INITIAL_IMAGE = "elf_m_idle_anim_f0"
DEMON_INITIAL_IMAGE = "big_demon_idle_anim_f0"
OGRE_INITIAL_IMAGE = "ogre_idle_anim_f0"

# Variáveis
game_state ='menu'
sound_enable = True

elf = Actor(HERO_INITIAL_IMAGE)
elf.x = WIDTH / 2 
elf.y = HEIGHT / 2 
elf_speed = 130

def draw():
    screen.clear()

    if game_state == 'menu':
        screen.fill(MENU_BG_COLOR)
        screen.draw.text(TITLE, center=(WIDTH/2, 60), color=BLACK, fontsize=50)

        star_button_rect = Rect((WIDTH // 2 - 100, 150), (200, 50))




def draw():
    screen.clear()
    screen.fill(STORY_BG_COLOR)
    elf.draw()
 
def update(dt):
    
    if keyboard.right:
        elf.x = elf.x + elf_speed * dt 
    elif keyboard.left:
        elf.x = elf.x - elf_speed * dt 
    elif keyboard.up:
        elf.y = elf.y - elf_speed * dt 
    elif keyboard.down:
        elf.y = elf.y + elf_speed * dt 

    elf.x = max(elf.width / 2, min(elf.x, WIDTH - elf.width / 2))
    elf.y = max(elf.height / 2, min(elf.y, HEIGHT - elf.height / 2))
    



    

