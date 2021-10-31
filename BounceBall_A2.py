import pygame

pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Activity Window Bouncing Ball")
x=100
y=100
c=0
blue=(0,0,255)
white = (255,255,255)
color=blue

while True :
 
     
 if(x>=470):
  x=10
 else:
  x=x+1
 if(y>=470):
  y=10
 else:
  y=y+1
    
    
 window.fill(white)
 pygame.draw.circle(window,color,(x,y),35)
 pygame.display.update()
    
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()

    


       
     