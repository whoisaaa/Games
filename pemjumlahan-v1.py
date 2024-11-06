import pygame
import random

pygame.init()

panjang_lebar = (800, 600)
screen = pygame.display.set_mode(panjang_lebar)
pygame.display.set_caption("Angka")

bg_color = pygame.Color('white')
tx_color = pygame.Color('black')
hijau = pygame.Color('green')
merah = pygame.Color('red')

font = pygame.font.Font(None, 72)
font_poin = pygame.font.Font(None, 35)


def in_text(text, x, y, color):
    render_text = font.render(text, True, color)
    text_center = render_text.get_rect(center=(x, y))
    screen.blit(render_text, text_center)

def in_quest ():
    r_nomor1 = random.randint(1, 10)
    r_nomor2 = random.randint(1, 10)
    return r_nomor1, r_nomor2, f"berapa {r_nomor1} + {r_nomor2}?"

def game_over():
    screen.fill(bg_color)
    in_text("Game over", 400, 200, merah)
    in_text("Tekan Spasi untuk Restart", 400, 300, tx_color)
    pygame.display.flip()
    pygame.time.wait(2000)
    
running = True
while running:
    r_nomor1, r_nomor2, quest = in_quest()
    text = ""
    jawaban = ""
    poin = 0
    nyawah = 3
    pertanyaan = False
    game_aktif = True

    while game_aktif:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_aktif =False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not pertanyaan:
                        if text.isdigit() and int(text) == (r_nomor1 + r_nomor2):
                            jawaban = "Kamu benar"
                            warna_jawaban = hijau
                            poin += 1
                        else:
                            jawaban = "kamu salah"
                            warna_jawaban = merah
                            nyawah -= 1
                        if nyawah == 0:
                            game_aktif = False
                        pertanyaan = True
                    else:
                        r_nomor1, r_nomor2, quest = in_quest()
                        text = ""
                        jawaban = ""
                        pertanyaan = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text [:-1]
                else:
                    text += event.unicode
            
            
        screen.fill (bg_color)
        in_text(quest, 400, 200, tx_color)
        in_text(text, 400, 300, tx_color)
        if pertanyaan:
            in_text(jawaban, 400, 400, warna_jawaban)
        skor_surface = font_poin.render(f"Skor: {poin}", True, merah)
        screen.blit(skor_surface, (10, 10))
        in_nyawa = font_poin.render(f"nyawa: {nyawah}", True, merah)
        screen.blit(in_nyawa, (690, 10))
        
        pygame.display.flip()
    
    game_over()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
    
pygame.quit()