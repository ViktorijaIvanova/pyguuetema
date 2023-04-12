import pygame 
import random 
import sys 

def maja(x,y,laius,kõrgus,pind,värv): 
    punktid=[(x,y-((3/4.0)*kõrgus)),(x,y),(x+laius,y),(x+laius,y-(3/4.0)*kõrgus),(x,y-((3/4.0)*kõrgus)),(x+laius/2.0,y-kõrgus),(x+laius,y-(3/4.0)*kõrgus)]
    suurus=random.randint(1,10) 
    pygame.draw.lines(pind,värv,False,punktid,suurus)


r=random.randint(0,255)
g=random.randint(0,255) 
b=random.randint(0,255) 
fon=[r,g,b] 

r=random.randint(0,255)
g=random.randint(0,255) 
b=random.randint(0,255)
majavarv=[r,g,b] 

r=random.randint(0,255)
g=random.randint(0,255) 
b=random.randint(0,255)
doorvarv=[r,g,b] 

r=random.randint(0,255)
g=random.randint(0,255) 
b=random.randint(0,255)
nuupvarv=[r,g,b]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("juhuslikud objektid") 
pind.fill(fon)  

maja(100,400,300,400,pind,majavarv)
for i in range(10): 
    #värv
    r=random.randint(0,255)
    g=random.randint(0,255) 
    b=random.randint(0,255) 
    varv=[r,g,b] 
    #suurus
    laius=random.randint(1,80) 
    kõrgus=random.randint(1,80)
    #asukoht
    x=random.randint(0,610-laius) 
    y=random.randint(0,450-kõrgus)
    pygame.draw.rect(pind,varv,[x,y,laius,kõrgus])


door=pygame.Rect(180,220,140,180)
pygame.draw.rect(pind,doorvarv,door) 

nuup=pygame.Rect(290,300,20,20)
pygame.draw.ellipse(pind,nuupvarv, nuup)

pygame.display.flip() 



while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
