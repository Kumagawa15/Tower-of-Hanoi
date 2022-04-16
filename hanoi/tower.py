import pygame

from hanoi.container import screen, make_text, clock,TEXT_COLORW,POLE_COLOR, POINTER_COLOR, TEXT_COLORBL, TEXT_COLORY, TOWER_COLOR, BG_COLOR, TEXT_COLORB

class Tower:
    def draw_towers(self, towers_psnx, steps):
        screen.fill(BG_COLOR)      # pemberian warna background display
        for xpos in range(40, 660+1, 200):
            pygame.draw.rect(screen, TOWER_COLOR, pygame.Rect(xpos, 400, 160 , 20))
            pygame.draw.rect(screen, POLE_COLOR, pygame.Rect(xpos+75, 200, 10, 200))
        make_text(screen, 'Start', (towers_psnx[0], 403), font_name='mono', size=14, color = TEXT_COLORW)
        make_text(screen, 'Finish', (towers_psnx[3], 403), font_name='mono', size=14, color = TEXT_COLORW)
        #Menampilkan langkah jalan pemain
        make_text(screen, 'Steps: '+str(steps), (420, 20), font_name='mono', size=30, color = TEXT_COLORB)

    def draw_blok(self, bloks):
        for blok in bloks:
            pygame.draw.rect(screen, TEXT_COLORBL, blok['rect'])
        return

    def draw_ptr(self, towers_psnx, pointing_at):
        ptr_points = [(towers_psnx[pointing_at]-7 ,440), (towers_psnx[pointing_at]+7, 440), (towers_psnx[pointing_at], 433)]
        pygame.draw.polygon(screen, POINTER_COLOR, ptr_points)
        return
    
    def stopwach(self):
        ticks = pygame.time.get_ticks()
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)
        make_text(screen, out, (50, 20), font_name='sans serif', size=50, color = TEXT_COLORY)
        clock.tick(60)

    


