import pgzrun
import random

# Game settings 
WIDTH = 480
HEIGHT = 352
TITLE = "A Fuga de Lorien"
game_state = 'menu'
score = 0
game_time = 0
sound_enabled = True
game_over_sound_played = False 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
STORY_BG_COLOR = (70, 40, 0)

# Background 
menu_background = Actor('bg_menu')
game_play_background = Actor('bg_game_play')

menu_background.pos = WIDTH // 2, HEIGHT // 2  
game_play_background.pos = WIDTH // 2, HEIGHT // 2


# Character 
HERO_IDLE_FRAMES = ['elf_m_idle_anim_f0', 'elf_m_idle_anim_f1', 'elf_m_idle_anim_f2', 'elf_m_idle_anim_f3']
HERO_RUN_FRAMES = ['elf_m_run_anim_f0', 'elf_m_run_anim_f1', 'elf_m_run_anim_f2', 'elf_m_run_anim_f3']

ENEMY_IDLE_FRAMES = ['big_demon_idle_anim_f0', 'big_demon_idle_anim_f1', 'big_demon_idle_anim_f2', 'big_demon_idle_anim_f3']
ENEMY_RUN_FRAMES = ['big_demon_run_anim_f0', 'big_demon_run_anim_f1', 'big_demon_run_anim_f2', 'big_demon_run_anim_f3']


#  Music and sound 
MUSIC_AMBIENT = 'ambient_music' 
SOUND_GAME_OVER = 'game_over' 

# Enemy 
enemies = []
ENEMY_SPEED_START = 80
ENEMY_SPAWN_COOLDOWN = 2.0
last_enemy_spawn_time = 0


class Hero(Actor):
    def __init__(self):
        super().__init__(HERO_IDLE_FRAMES[0])
        self.speed = 130
        self.x = self.width // 2 
        self.y = HEIGHT // 2

        self.animation_data = {
            'idle': HERO_IDLE_FRAMES,
            'run': HERO_RUN_FRAMES,
        }
        self.current_anim = 'idle'
        self.frame_index = 0
        self.anim_timer = 0.0
        self.anim_speed = 0.15
        self.is_moving = False

    def update(self, dt):
        self.is_moving = False

        if keyboard.up:
            self.y -= self.speed * dt
            self.is_moving = True
        elif keyboard.down:
            self.y += self.speed * dt
            self.is_moving = True

        if self.y < self.height // 2:
            self.y = self.height // 2
        if self.y > HEIGHT - self.height // 2:
            self.y = HEIGHT - self.height // 2

        if not self.is_moving:
            self.current_anim = 'idle'
            self.image = self.animation_data['idle'][0]
            self.frame_index = 0
            self.anim_timer = 0.0
        else:
            self.current_anim = 'run'
            self.anim_timer += dt
            if self.anim_timer >= self.anim_speed:
                self.anim_timer = 0.0
                frames_to_use = self.animation_data[self.current_anim]
                self.frame_index = (self.frame_index + 1) % len(frames_to_use)
                self.image = frames_to_use[self.frame_index]


class Enemy(Actor):
    def __init__(self, start_speed):
        super().__init__(ENEMY_RUN_FRAMES[0])
        self.speed = start_speed
        self.x = WIDTH + 50
        self.y = random.randint(self.height // 2, HEIGHT - self.height // 2)

        self.animation_data = {
            'idle': ENEMY_IDLE_FRAMES,
            'run': ENEMY_RUN_FRAMES,
        }
        self.current_anim = 'run'
        self.frame_index = 0
        self.anim_timer = 0.0
        self.anim_speed = 0.2

    def reset_position(self):
        self.x = WIDTH + random.randint(50, 150)
        self.y = random.randint(self.height // 2, HEIGHT - self.height // 2)
        self.speed += 5

    def update(self, dt):
        self.x -= self.speed * dt

        self.anim_timer += dt
        if self.anim_timer >= self.anim_speed:
            self.anim_timer = 0.0
            frames_to_use = self.animation_data[self.current_anim]
            self.frame_index = (self.frame_index + 1) % len(frames_to_use)
            self.image = frames_to_use[self.frame_index]

hero = Hero()

def spawn_enemy():
    new_enemy = Enemy(ENEMY_SPEED_START)
    enemies.append(new_enemy)

def draw():
    screen.clear()

    if game_state == 'menu':
        menu_background.draw()
        screen.draw.text(TITLE, center=(WIDTH/2, 60), color=WHITE, fontsize=50)

        start_button_rect = Rect((WIDTH // 2 - 100, 150), (200, 50))
        screen.draw.filled_rect(start_button_rect, (0, 0, 100))
        screen.draw.text("Iniciar Jogo", center=start_button_rect.center, color=WHITE, fontsize=30)

        sound_button_rect = Rect((WIDTH // 2 - 100, 220), (200, 50))
        screen.draw.filled_rect(sound_button_rect, (0, 0, 100))
        screen.draw.text(f"Sons {'ON' if sound_enabled else 'OFF'}", center=sound_button_rect.center, color=WHITE, fontsize=30)

        quit_button_rect = Rect((WIDTH // 2 - 100, 290), (200, 50))
        screen.draw.filled_rect(quit_button_rect, (0, 0, 100))
        screen.draw.text("Sair", center=quit_button_rect.center, color=WHITE, fontsize=30)

    elif game_state == 'story':
        screen.fill(STORY_BG_COLOR)
        screen.draw.text("O elfo Lorien precisa escapar dos monstros!", center=(WIDTH/2, 100), color=WHITE, fontsize=25)
        screen.draw.text("Ajude-o a sobreviver!", center=(WIDTH/2, 140), color=WHITE, fontsize=25)
        screen.draw.text("Pressione ENTER para iniciar...", center=(WIDTH/2, HEIGHT - 50), color=WHITE, fontsize=20)

    elif game_state == 'game_play':
        game_play_background.draw()
        hero.draw()
        for enemy_obj in enemies:
            enemy_obj.draw()
        screen.draw.text(f"Pontos: {int(score)}", (10, 10), color=WHITE, fontsize=25)

    elif game_state == 'game_over':
        screen.fill(BLACK)
        screen.draw.text("GAME OVER!", center=(WIDTH/2, 150), color=(255, 0, 0), fontsize=60)
        screen.draw.text(f"Seus Pontos: {int(score)}", center=(WIDTH/2, 200), color=WHITE, fontsize=30)
        screen.draw.text("Pressione ENTER para ir ao Menu", center=(WIDTH/2, HEIGHT - 50), color=WHITE, fontsize=25)


def update(dt):
    global game_state, game_time, score, sound_enabled, last_enemy_spawn_time, game_over_sound_played

    if game_state == 'menu':
        music.stop()
        game_over_sound_played = False
    elif game_state == 'game_play':
        hero.update(dt)

        if sound_enabled:
            if not music.is_playing(MUSIC_AMBIENT):
                music.play(MUSIC_AMBIENT) 
        else:
            music.stop()

        game_time += dt
        score += dt * 3

        if game_time - last_enemy_spawn_time >= ENEMY_SPAWN_COOLDOWN:
            spawn_enemy()
            last_enemy_spawn_time = game_time

        active_enemies = []
        for enemy_obj in enemies:
            enemy_obj.update(dt)

            if hero.colliderect(enemy_obj):
                music.stop()

                if sound_enabled and not game_over_sound_played:
                    sounds.game_over.play() 
                    game_over_sound_played = True
                
                game_state = 'game_over'
                score = int(score)
                game_time = 0
                enemies.clear()
                return

            if enemy_obj.x < -50:
                enemy_obj.reset_position()
            active_enemies.append(enemy_obj)

        enemies[:] = active_enemies


def on_mouse_down(pos, button):
    global game_state, sound_enabled

    if game_state == 'menu':
        start_button_rect = Rect((WIDTH // 2 - 100, 150), (200, 50))
        sound_button_rect = Rect((WIDTH // 2 - 100, 220), (200, 50))
        quit_button_rect = Rect((WIDTH // 2 - 100, 290), (200, 50))

        if start_button_rect.collidepoint(pos):
            game_state = 'story'
        elif sound_button_rect.collidepoint(pos):
            sound_enabled = not sound_enabled
        elif quit_button_rect.collidepoint(pos):
            exit()

def on_key_down(key):
    global game_state, score, game_time, last_enemy_spawn_time, game_over_sound_played

    if game_state == 'story' and key == keys.RETURN:
        game_state = 'game_play'
        game_time = 0
        score = 0
        last_enemy_spawn_time = 0
        enemies.clear()
        spawn_enemy()
        game_over_sound_played = False
        if sound_enabled:
            music.play(MUSIC_AMBIENT)

    elif game_state == 'game_over' and key == keys.RETURN:
        game_state = 'menu'
        score = 0
        game_time = 0
        hero.x = hero.width // 2
        hero.y = HEIGHT // 2
        hero.is_moving = False
        hero.current_anim = 'idle'
        hero.frame_index = 0
        hero.anim_timer = 0.0
        enemies.clear()
        last_enemy_spawn_time = 0