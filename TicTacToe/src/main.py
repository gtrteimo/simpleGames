import pygame

from button import Button 

screen = None
clock = None

buttons = None

def createBoard(size: int):
    global buttons
    buttons = [
        [
            Button(0, 0, size/3 - 10, size/3 - 10), 
            Button(size/3 + 5, 0, size/3 - 10, size/3 - 10), 
            Button(size*2/3 + 10, 0, size/3 - 10, size/3 - 10)
        ],
        [
            Button(0, size/3 + 5, size/3 - 10, size/3 - 10), 
            Button(size/3 + 5, size/3 + 5, size/3 - 10, size/3 - 10), 
            Button(size*2/3 + 10, size/3 + 5, size/3 - 10, size/3 - 10)
        ],
        [
            Button(0, size*2/3 + 10, size/3 - 10, size/3 - 10), 
            Button(size/3 + 5, size*2/3 + 10, size/3 - 10, size/3 - 10), 
            Button(size*2/3 + 10, size*2/3 + 10, size/3 - 10, size/3 - 10)
        ],
    ]

def display():
    screen.fill((175, 175, 175))
    for row in buttons:
        for button in row:
            button.draw(screen)

def input():
    mousePos = pygame.mouse.get_pos()
    for row in buttons:
        for button in row:
            button.clicked(mousePos)

def loop():
    running: bool = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        input()
        display()

        pygame.display.flip()

        clock.tick(60)

def main(size: int = 720):
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((size, size))

    createBoard(size)

    clock = pygame.time.Clock()

    loop()

    pygame.quit()

main()