import pygame

#INIT

pygame.init()
size = (852, 480)
win = pygame.display.set_mode(size)
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#CLASSES (player, projectile)

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.right = False
        self.left = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
     
    def draw(self, win):
        if not self.standing:
            if self.walkCount > 26:
                self.walkCount = 0
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x ,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x ,self.y))
                self.walkCount += 1
        else :
            if self.right:
                win.blit(walkRight[0],(self.x ,self.y))
            else :
                win.blit(walkLeft[0], (self.x ,self.y))
                
            
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)             

       

def redrawGameWindow():
    win.blit(bg, (0,0))      
    man.draw(win)   
    pygame.display.update()

#############################
############################
#main loop
man = player(50, 410, 64, 64)
bullets = []
run = True

while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.x < size[0] and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed() #hyper important, maintient l'etat de tout les boutons du clavier en mémoire.
    
    if keys[pygame.K_LEFT] and man.x >= man.vel:
        man.x -= man.vel
        man.right = False
        man.left = True
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < size[0]-man.width:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0       
    if man.isJump == False :    
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= 0 and man.jumpCount < 11: 
            man.y -= (man.jumpCount ** 2) * 0.5
            man.jumpCount -= 1
        elif man.jumpCount >= -10 and man.jumpCount < 0:
            man.y -= -(man.jumpCount ** 2) * 0.5
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()
    
pygame.quit()

################################################
#############################