import pygame
import sys


buttons = []


class Button:
    def __init__(self, text, width, height, pos, elevation):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = 'Yellow'

        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = 'Green'

        self.text = text
        self.text_surf = font_size.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        buttons.append(self)

    def change_text(self, newtext):
        self.text_surf = font_size.render(newtext, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = 'Blue'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed:
                    print('Доделать')
                    self.pressed = False
                    self.change_text(self.text)
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = 'Brown'


pygame.init()
bg_fon = pygame.image.load("./img/background_img_reg.jpg")
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()

font_size = pygame.font.Font('./g_fonts/ZenDots-Regular.ttf', 40)
start_text = font_size.render('REGISTRATION', True, 'Blue')

button1 = Button('Start', 200, 40, (215, 300), 5)


def buttons_draw():
    for b in buttons:
        b.draw()


while True:
    screen.blit(bg_fon, (0, 0))
    buttons_draw()
    screen.blit(start_text, (110, 40))

    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

