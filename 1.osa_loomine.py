import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480)) 
ekraani_pind.fill((0,0,130)) 
pygame.display.set_caption("Esimene aken")
ristkulik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0,255,0),ristkulik)
kuu=pygame.Rect(20,15,70,70)
pygame.draw.ellipse(ekraani_pind,(255,255,0), kuu)
taht=pygame.Rect(150,65,5,5)
pygame.draw.ellipse(ekraani_pind,(255,255,0), taht)
taht2=pygame.Rect(250,25,5,5)
pygame.draw.ellipse(ekraani_pind,(255,255,0), taht2)
taht3=pygame.Rect(400,40,5,5)
pygame.draw.ellipse(ekraani_pind,(255,255,0), taht3)
taht4=pygame.Rect(550,65,5,5)
pygame.draw.ellipse(ekraani_pind,(255,255,0), taht4)
taht5=pygame.Rect(200,150,5,5)
pygame.draw.ellipse(ekraani_pind,(255,255,0), taht5)
taht6=pygame.Rect(475,130,5,5)
pygame.draw.ellipse(ekraani_pind,(255,255,0), taht6)
taht7=pygame.Rect(300,120,5,5)
pygame.draw.ellipse(ekraani_pind,(255,255,0), taht7)


pilt=pygame.image.load("Liblikas.png")
ekraani_pind.blit(pilt,(150,200))
font=pygame.font.SysFont("Broadway",40)
sonad="Tere tulemast!"
varv=[0,0,0]
teksti_lisamine=font.render(sonad,False,varv)
ekraani_pind.blit(teksti_lisamine,(250,150))

pygame.display.flip() #отображает поэтому должна находиться в конце рисунков
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
