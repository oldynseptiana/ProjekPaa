""" Button class file """
import pygame
import sys
import data.src.config as cfg
import data.src.peta as peta


class Button:
    """ Button abstract class """

    def __init__(self, text, width, height, pos, color, font_size=20, text_color=cfg.PURPLE):
        # Core attributes
        self.pressed = False
        self.disabled = False
        self.elevation = 4
        self.dynamic_elevation = self.elevation
        self.original_y_pos = pos[1]
        self.text = text
        self.text_color = text_color
        self.pos = pos
        self.font_size = font_size

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.TOP_COLOR = color
        self.top_color = color

        # Bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = cfg.PURPLE

        # Hitbox rectangle
        self.hitbox_rect = pygame.Rect(pos, (width, height))

        # Text
        self.gui_font = pygame.font.Font(cfg.chary_font, self.font_size)
        self.text_surf = self.gui_font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        """
        Draws the button
        :param screen:
        :return:
        """
        self.check_click()
        self.update()

        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.hitbox_rect.y = self.original_y_pos - self.elevation

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=5)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=5)

        screen.blit(self.text_surf, self.text_rect)

    def check_click(self):
        """
        Check if the button is clicked
        :return:
        """
        mouse_pos = pygame.mouse.get_pos()

        if self.hitbox_rect.collidepoint(mouse_pos):
            self.top_color = cfg.WHITE
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.button_action()
                    self.pressed = False
        else:
            self.pressed = False
            self.dynamic_elevation = self.elevation
            self.top_color = self.TOP_COLOR

    def button_action(self):
        """
        Performs default button actions
        :return:
        """

    def update(self):
        """
        Optional updates for subclasses
        :return:
        """


class MulaiButton(Button):
    def button_action(self):
        peta.mulai()


class BerhentiButton(Button):
    def button_action(self):
        peta.berhenti()


class AcakPetaButton(Button):
    def button_action(self):
        peta.buat_peta()


class AcakDroidMerahButton(Button):
    def button_action(self):
        peta.acak_droid_merah()


class AcakDroidHijauButton(Button):
    def button_action(self):
        peta.acak_droid_hijau()


class TambahDroidMerahButton(Button):
    def button_action(self):
        print("Tambah Merah")


class PandanganDroidMerahButton(Button):
    def button_action(self):
        cfg.pandangan_merah_on = not cfg.pandangan_merah_on


class PandanganDroidHijauButton(Button):
    def button_action(self):
        cfg.pandangan_hijau_on = not cfg.pandangan_hijau_on


class KeluarButton(Button):
    def button_action(self):
        pygame.quit()
        sys.exit()
