import pygame, sys

from hanoi.game import Game
from hanoi.tower import Tower

pygame.init()
pygame.display.set_caption("Towers of Hanoi")

game = Game()
tower = Tower()
game_done = False

game.make_blok()
while not game_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and not game_done:
            if event.key == pygame.K_r:
                game.reset()
            if event.key == pygame.K_q:
                game_done = True
            #arah gerak kekana jika menekan panah kana di keyboard
            if event.key == pygame.K_RIGHT:
                game.pointing_at = (game.pointing_at+1)%4
                if game.floating:
                    game.bloks[game.floater]['rect'].midtop = (game.towers_psnx[game.pointing_at], 100)
                    game.bloks[game.floater]['tower'] = game.pointing_at
            #arah gerak kekiri jika menekan panah kiri di keyboard
            if event.key == pygame.K_LEFT:
                game.pointing_at = (game.pointing_at-1)%4
                if game.floating:
                    game.bloks[game.floater]['rect'].midtop = (game.towers_psnx[game.pointing_at], 100)
                    game.bloks[game.floater]['tower'] = game.pointing_at
            #arah gerak keatas jika menekan panah atas di keyboard
            if event.key == pygame.K_UP and not game.floating:
                for blok in game.bloks[::-1]:
                    if blok['tower'] == game.pointing_at:
                        game.floating = True
                        game.floater = game.bloks.index(blok)
                        blok['rect'].midtop = (game.towers_psnx[game.pointing_at], 100)
                        break
            #arah gerak kebawah jika menekan panah bawah di keyboard
            if event.key == pygame.K_DOWN and game.floating:
                for blok in game.bloks[::-1]:
                    if blok['tower'] == game.pointing_at and game.bloks.index(blok) != game.floater:
                        if blok['val'] > game.bloks[game.floater]['val']:
                            game.floating = False
                            game.bloks[game.floater]['rect'].midtop = (game.towers_psnx[game.pointing_at], blok['rect'].top-23)
                            game.steps += 1
                        break
                else: 
                    game.floating = False
                    game.bloks[game.floater]['rect'].midtop = (game.towers_psnx[game.pointing_at], 400-23)
                    game.steps += 1

    tower.draw_towers(game.towers_psnx, game.steps)
    tower.draw_blok(game.bloks)
    tower.draw_ptr(game.towers_psnx, game.pointing_at)
    tower.stopwach()
    #sama seperti update game 
    pygame.display.flip()
    #kondisi juka tidak ada yamg mengambang method check_win dijalankan
    if not game.floating:game.check_win()