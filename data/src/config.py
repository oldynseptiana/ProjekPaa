""" Config file to store global variables """
import pygame

# Screen dimension
screen_width = 832
screen_height = 608

# Font
chary_font = 'data/font/charybdis.ttf'

# RETROCAL-8 Palette
RED = pygame.Color("#c6505a")
GREEN = pygame.Color("#74a33f")
PURPLE = pygame.Color("#2f142f")
CREAM = pygame.Color("#fcffc0")
BROWN = pygame.Color("#774448")
WHITE = pygame.Color("#ffffff")
BLUE = pygame.Color("#6eb8a8")

# Peta
maze = None
maze_list = []

# Koordinat droid
merah_coord = []
pandangan_merah_coords = []
hijau_coord = []
pandangan_hijau_coords = []

# Pandangan droid
pandangan_merah_on = False
pandangan_hijau_on = False

# Slider
MIN_PANDANGAN_HIJAU = 2
MAX_PANDANGAN_HIJAU = 6
jarak_pandangan_hijau = 2

MIN_PANDANGAN_MERAH = 3
MAX_PANDANGAN_MERAH = 6
jarak_pandangan_merah = 3

# Gerakkan hijau
is_running = False
