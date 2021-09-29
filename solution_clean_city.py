import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=600
height=350
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("city3.jpg").convert_alpha()
images["bin"] = pygame.image.load("bin.png").convert_alpha()
  

class Dustbin:
    def __init__(self,x):
        self.bin=pygame.Rect(x,210,10,10)
        
    def display(self):
        screen.blit(images["bin"],self.bin)
        
bin1=Dustbin(25)
bin2=Dustbin(335)
bin3=Dustbin(516)

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass        
    
    
    screen.blit(images["bg"],[0,0])
    bin1.display()
    bin2.display()
    bin3.display()
    

    pygame.display.update()
    clock.tick(30)
