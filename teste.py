#BOX = Rect((20, 20), (100, 100))
#draw.filled_rect( rect , (r , g , b) ) 
# screen.draw.rect(BOX, WHITE)

class Hero:
    def __init__(self, pos):
        self.x, self.y = pos

        self.sprites = {
            "idle":["elf_m_idle_anim_f0", "elf_m_idle_anim_f1", "elf_m_idle_anim_f2", "elf_m_idle_anim_f3"],
            "run":["elf_m_run_anim_f0", "elf_m_run_anim_f1", "elf_m_run_anim_f2","elf_m_run_anim_f3"]
        }
