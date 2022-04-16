import pygame, time, sys

from hanoi.container import screen, make_text, ticks, TEXT_COLORR, TEXT_COLORY, BG_COLOR, TEXT_COLORB, TEXT_COLORG

class Game:
    def __init__(self):
        self.towers_psnx = [120, 320, 520, 720]
        self.bloks = []
        self.n_bloks = 4        #Mengatur banyaknya jumlah bloks                 
        self.pointing_at = 0
        self.floating = False   
        self.floater = 0
        self.steps = 0

    def make_blok(self):
        self.bloks = []
        height = 20
        ypos = 397 - height
        width = self.n_bloks * 23
        for i in range(self.n_bloks):
            #meng-Implementasi metode maps ADT (Abstact Data Type) 
            blok = {}
            blok['rect'] = pygame.Rect(0, 0, width, height)
            blok['rect'].midtop = (120, ypos)
            blok['val'] = self.n_bloks-i
            blok['tower'] = 0
            #meng-Implementasi metode Unsorted Map
            self.bloks.append(blok)
            ypos -= height+3
            width -= 23

    #Mereset game dengan mengembalikan seluruh nilai objek menjadi 0 dan false
    #Lalu melemparkan atau memanggil fungsi make_bloks
    def reset(self):
        self.steps = 0
        self.pointing_at = 0
        self.floating = False
        self.floater = 0
        self.make_blok()
        
    def check_win(self):
        over = True
        for blok in self.bloks:
            #Jika tidak diposisi array 3 nilai variable over menjadi false dan kondisi perulanggan terjadi
            if blok['tower'] != 3:
                over = False
        #Jika variable over True 
        if over:
            time.sleep(0.2)     # pouse
            self.game_over()    # setelah 0.2 detik melempar ke variable game_over

    def game_over(self): # display dari game over
        screen.fill(BG_COLOR)  #Background game_over
        min_steps = 2**self.n_bloks/2+1 #perhitungan minimum step 4 tower
        make_text(screen, 'You Won!', (420, 100), font_name='sans serif', size=72, color = TEXT_COLORY)
        make_text(screen, 'You Won!', (422, 102), font_name='sans serif', size=72, color = TEXT_COLORY)
        make_text(screen, 'Your Steps: '+str(self.steps), (420, 260), font_name='mono', size=30, color = TEXT_COLORB)
        #minimum step yang terjadi
        make_text(screen, 'Minimum Steps: '+str(min_steps), (420, 290), font_name='mono', size=30, color = TEXT_COLORR)
        #step yang dilakukan
        if min_steps == self.steps:
            make_text(screen, 'You finished in minumum steps!', (420, 200), font_name='mono', size=26, color = TEXT_COLORG)
        #hasil waktu yang didapatkan 
        end_stopwach = (pygame.time.get_ticks() - ticks) // 1000
        make_text(screen, 'Time to finish: '+ str(end_stopwach)+ ' S', (420, 320), font_name='mono', size=26, color = TEXT_COLORR)
        pygame.display.flip()
        time.sleep(3)   #menunggu selama 3 s
        pygame.quit()   #pygame exit
        sys.exit()      #console exit
    