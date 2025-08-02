import pygame

class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.click = False

    def draw(self, screen):
        pygame.draw.rect(screen, (125, 125, 125), self.rect)
        if self.click:
            center_x, center_y = self.rect.center
            pygame.draw.line(screen, (50, 50, 50), (self.rect.topleft), (self.rect.bottomright), 20)
            pygame.draw.line(screen, (50, 50, 50), (self.rect.topright), (self.rect.bottomleft), 20)

    def clicked(self, mousePos):
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0]:
                if not self.click:
                    self.click = True