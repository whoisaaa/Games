import pygame
import sys
import random

pygame.init()

lebar_panjang = (800, 600)
screen = pygame.display.set_mode(lebar_panjang)
pygame.display.set_caption("MAIN ANGKA")

putih = pygame.Color('White')
hitam = pygame.Color('Black')
merah = pygame.Color('red')
hijau = pygame.Color('green')

font = pygame.font.Font(None, 50)
mini_font = pygame.font.Font(None, 25)

def ini_text (text, x, y, color):
    render_text = font.render(text, True, color)
    text_posisi = render_text.get_rect(center=(x,y))
    screen.blit(render_text,text_posisi)
    
def mini_text (text, x, y, color):
    render_text = mini_font.render(text, True, color)
    text_posisi = render_text.get_rect(center=(x,y))
    screen.blit(render_text,text_posisi)
    
levels = [
    {"target": 3, "min": 1, "max": 10},
    {"target": 5, "min": 10, "max": 20},
    {"target": 8, "min": 20, "max": 50}
]
    
operasi_ = ["+", "-", "*", "/"]

level = 0
start =  "TEKAN SPASI UNTUK MEMULAI"
soal = ""
hasil = ""
jawaban = ""
perintah = ""
poin = 0
jawab = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not jawab:
                if event.key == pygame.K_SPACE:
                    if poin < levels[level]["target"]:
                        start = ""
                        angka1 = random.randint(levels[level]["min"], levels[level]["max"])
                        angka2 = random.randint(levels[level]["min"], levels[level]["max"])
                        operasi = random.choice(operasi_)
                        if operasi == "+":
                            soal = f"BERAPA {angka1} + {angka2} ?"
                            benar = angka1 + angka2
                        elif operasi == "-":
                            if angka1 < angka2:
                                angka1 = angka1 + angka2
                                soal = f"BERAPA {angka1} - {angka2} ?"
                                benar = angka1 - angka2
                        elif operasi == "*":
                            soal = f"BERAPA {angka1} x {angka2} ?"
                            benar = angka1 * angka2
                        elif operasi == "/":
                            angka1 = angka1 * angka2
                            soal = f"BERAPA {angka1} / {angka2} ?"
                            benar = angka1 // angka2
                        jawaban = ""
                        hasil = ""
                        perintah = ""
                        jawab = True
                    else:
                        level += 1
            else:
                pass
            if jawab:
                jawaban = jawaban.strip()
                if event.key == pygame.K_RETURN:
                    if jawaban.isdigit() and int(jawaban) == benar:
                        hasil = "KAMU BENAR"
                        perintah = "TEKAN SPASI UNTUK SOAL BARU"
                        poin += 1
                    else:
                        hasil = f"KAMU SALAH, JAWABANNYA {benar}"
                        perintah = "TEKAN SPASI UNTUK SOAL BARU"
                    jawab = False
                elif event.key == pygame.K_BACKSPACE:
                    jawaban = jawaban[:-1]
                else:
                    jawaban += event.unicode
                
            
    screen.fill(putih)
    ini_text(start, 400, 200, merah)
    ini_text(soal, 400, 200, hitam)
    ini_text(jawaban, 400, 250, hitam)
    ini_text(hasil, 400, 300, merah)
    mini_text(perintah, 400, 330, hijau)
    mini_text(f"POIN {poin}", 35, 15, hitam)
    
    pygame.display.flip()
    


sys.exit()   
pygame.quit()