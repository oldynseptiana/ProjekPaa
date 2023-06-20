"""
Program Labirin
"""
import pygame
import sys

import data.src.config as cfg
import data.src.button as btn
import data.src.slider as sld
import data.src.peta as peta

# Inisiasi pygame
pygame.init()

# Timer
clock = pygame.time.Clock()
mulai_tick = pygame.USEREVENT + 1
pygame.time.set_timer(mulai_tick, 250)  # 250 milliseconds

# Inisiasi screen
screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))

# Set caption
icon = pygame.image.load('data/images/labirin-icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Labirin")


class Program:
    """ Program class """

    def __init__(self):
        # Initiate buttons
        self.mulai_button = btn.MulaiButton("Mulai", 192, 32, (608, 32), cfg.GREEN)
        self.berhenti_button = btn.BerhentiButton("Berhenti", 192, 32, (608, 80), cfg.RED)
        self.acak_peta_button = btn.AcakPetaButton("Acak Peta", 192, 32, (608, 128), cfg.CREAM)
        self.acak_droid_merah_button = btn.AcakDroidMerahButton("Acak Droid Merah", 192, 32, (608, 176), cfg.CREAM)
        self.acak_droid_hijau_button = btn.AcakDroidHijauButton("Acak Droid Hijau", 192, 32, (608, 224), cfg.CREAM)
        self.tambah_droid_merah_button = btn.TambahDroidMerahButton("Tambah Droid Merah", 192, 32, (608, 272), cfg.CREAM)
        self.pandangan_droid_merah_button = btn.PandanganDroidMerahButton("Pandangan Droid Merah", 192, 32, (608, 320), cfg.CREAM)
        self.pandangan_droid_hijau_button = btn.PandanganDroidHijauButton("Pandangan Droid Hijau", 192, 32, (608, 416), cfg.CREAM)
        self.keluar_button = btn.KeluarButton("Keluar", 192, 32, (608, 512), cfg.BLUE)

        # Initiate sliders
        self.pandangan_droid_merah_slider = sld.PandanganMerahSlider((608, 388), 192, cfg.RED, cfg.RED)
        self.pandangan_droid_hijau_slider = sld.PandanganHijauSlider((608, 484), 192, cfg.GREEN, cfg.GREEN)

        # Initiate peta
        peta.buat_peta()

    def run(self):
        """ Runs methods every frame """
        # Run buttons
        self.mulai_button.draw(screen)
        self.berhenti_button.draw(screen)
        self.acak_peta_button.draw(screen)
        self.acak_droid_merah_button.draw(screen)
        self.acak_droid_hijau_button.draw(screen)
        self.pandangan_droid_merah_button.draw(screen)
        self.pandangan_droid_hijau_button.draw(screen)
        self.tambah_droid_merah_button.draw(screen)
        self.keluar_button.draw(screen)

        # Run sliders
        self.pandangan_droid_merah_slider.draw(screen, f"Jarak: {cfg.jarak_pandangan_merah} Blok")
        self.pandangan_droid_hijau_slider.draw(screen, f"Jarak: {cfg.jarak_pandangan_hijau} Blok")

        # Run peta
        peta.gambar_peta(screen)


def main():
    """ === DRIVER CODE === """
    # Initiate instances
    program = Program()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == mulai_tick:
                if cfg.is_running:
                    peta.gerakkan_merah()

        # Run program
        program.run()

        # Updates
        pygame.display.flip()
        screen.fill(cfg.BROWN)
        clock.tick(60)


if __name__ == "__main__":
    main()
