import pygame
import data.src.config as cfg
import data.src.peta as peta


class Slider:
    def __init__(self, pos, length, line_color, handle_color, starting_percentage=.5, line_width=2, handle_radius=8):
        # Core attributes
        self.start_pos = pos
        self.length = length
        self.line_color = line_color
        self.HANDLE_COLOR = handle_color
        self.handle_color = handle_color
        self.line_width = line_width
        self.handle_radius = handle_radius
        self.pressed = False
        self.chary = pygame.font.Font(cfg.chary_font, 20)

        # Handle attributes
        x, y = self.start_pos
        self.handle_obj = pygame.Rect(self.start_pos, (self.handle_radius, self.handle_radius))
        self.end_pos = (x + self.length, y)
        self.handle_pos = (x + self.length * starting_percentage, y)

    def draw(self, screen, text):
        self.check_click()
        self.run_logic()
        self.draw_text(screen, text)
        pygame.draw.line(screen, self.line_color, self.start_pos, self.end_pos, self.line_width)
        self.handle_obj = pygame.draw.circle(screen, self.handle_color, self.handle_pos, self.handle_radius)

    def check_click(self):
        mouse = pygame.mouse.get_pressed(num_buttons=3)
        mouse_pos = pygame.mouse.get_pos()
        mouse_x, mouse_y = mouse_pos

        if self.handle_obj.collidepoint(mouse_pos):
            self.handle_color = cfg.WHITE
            if mouse[0]:
                self.pressed = True
            else:
                self.pressed = False
        elif not mouse[0]:
            self.pressed = False
            self.handle_color = self.HANDLE_COLOR

        if self.pressed:
            x, y = self.handle_pos
            if mouse_x < self.start_pos[0]:
                x = self.start_pos[0]
                self.handle_pos = (x, y)
            elif mouse_x > self.end_pos[0]:
                x = self.end_pos[0]
                self.handle_pos = (x, y)
            else:
                self.handle_pos = (mouse_x, y)

    def run_logic(self):
        """
        Performs slider logic
        :return:
        """

    def draw_text(self, screen, text):
        color = cfg.CREAM
        displaced_y_pos = -30
        text_obj = self.chary.render(text, True, color)
        x, y = self.start_pos
        text_start_pos = (x, y + displaced_y_pos)
        screen.blit(text_obj, text_start_pos)

    def slider_logic(self, min_value, max_value):
        relative_pos = self.handle_pos[0] - self.start_pos[0]
        dis_value = max_value - min_value
        return min_value + int(dis_value * relative_pos / self.length)


class PandanganMerahSlider(Slider):
    def run_logic(self):
        cfg.jarak_pandangan_merah = self.slider_logic(cfg.MIN_PANDANGAN_MERAH, cfg.MAX_PANDANGAN_MERAH)
        # peta.cek_pandangan_merah()

class PandanganHijauSlider(Slider):
    def run_logic(self):
        cfg.jarak_pandangan_hijau = self.slider_logic(cfg.MIN_PANDANGAN_HIJAU, cfg.MAX_PANDANGAN_HIJAU)
        # peta.cek_pandangan_hijau()
