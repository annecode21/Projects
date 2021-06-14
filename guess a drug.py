import pygame

#initialize python
pygame.init()

#create the window
winWidth = 800
winHeight = 600
window = pygame.display.set_mode((winWidth,winHeight))

#title and icon
pygame.display.set_caption('Guess a drug!')
icon = pygame.image.load('medicine.png')
pygame.display.set_icon(icon)

#game loop
running = True
while running:
    window.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.update()