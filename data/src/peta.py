""" Util file for global functions """
import pygame
import data.src.config as cfg
import mazelib
from mazelib.generate.AldousBroder import AldousBroder
from mazelib.solve.Collision import Collision


def buat_peta():
    maze = mazelib.Maze()
    maze.generator = AldousBroder(8, 8)
    maze.generate()
    maze.solver = Collision()
    cfg.maze = maze
    cfg.maze_list = [list(row) for row in cfg.maze.tostring().strip().split('\n')]

    buat_droid()
    berhenti()


def gambar_peta(screen):
    x_offset = 32
    y_offset = 32

    for i, row in enumerate(cfg.maze_list):
        for j, block in enumerate(row):
            if block == "#":
                pygame.draw.rect(screen, cfg.PURPLE, pygame.Rect(x_offset + j * 32, y_offset + i * 32, 32, 32))
            if block == " " or block == "+":
                pygame.draw.rect(screen, cfg.CREAM, pygame.Rect(x_offset + j * 32, y_offset + i * 32, 32, 32))
            if block == "E":
                pygame.draw.rect(screen, cfg.CREAM, pygame.Rect(x_offset + j * 32, y_offset + i * 32, 32, 32))
                pygame.draw.circle(screen, cfg.GREEN, (x_offset + j * 32 + 16, y_offset + i * 32 + 16), 16)
            if block == "S":
                pygame.draw.rect(screen, cfg.CREAM, pygame.Rect(x_offset + j * 32, y_offset + i * 32, 32, 32))
                pygame.draw.circle(screen, cfg.RED, (x_offset + j * 32 + 16, y_offset + i * 32 + 16), 16)
            if block == "h":
                pygame.draw.rect(screen, cfg.CREAM, pygame.Rect(x_offset + j * 32, y_offset + i * 32, 32, 32))
                if cfg.pandangan_hijau_on:
                    pygame.draw.circle(screen, cfg.GREEN, (x_offset + j * 32 + 16, y_offset + i * 32 + 16), 8)
            if block == "m":
                pygame.draw.rect(screen, cfg.CREAM, pygame.Rect(x_offset + j * 32, y_offset + i * 32, 32, 32))
                if cfg.pandangan_merah_on:
                    s = pygame.Surface((32, 32))
                    s.set_alpha(128)
                    s.fill(cfg.RED)
                    screen.blit(s, (x_offset + j * 32, y_offset + i * 32))
            if block == "h":
                pygame.draw.rect(screen, cfg.CREAM, pygame.Rect(x_offset + j * 32, y_offset + i * 32, 32, 32))
                if cfg.pandangan_hijau_on:
                    s = pygame.Surface((32, 32))
                    s.set_alpha(128)
                    s.fill(cfg.GREEN)
                    screen.blit(s, (x_offset + j * 32, y_offset + i * 32))


def acak_droid_merah():
    cfg.maze.generate_entrances(False, False)
    cfg.maze.end = cfg.hijau_coord
    cfg.merah_coord = cfg.maze.start
    print("acak merah", cfg.maze.start, cfg.maze.end)

    cfg.maze.solve()
    update_maze_list()
    berhenti()


def acak_droid_hijau():
    cfg.maze.generate_entrances(False, False)
    cfg.maze.start = cfg.merah_coord
    cfg.hijau_coord = cfg.maze.end
    print("acak hijau", cfg.maze.start, cfg.maze.end)

    cfg.maze.solve()
    update_maze_list()
    berhenti()


def buat_droid():
    cfg.maze.generate_entrances(False, False)
    cfg.merah_coord = cfg.maze.start
    cfg.hijau_coord = cfg.maze.end

    cfg.maze.solve()
    update_maze_list()


def mulai():
    cfg.is_running = True


def berhenti():
    cfg.is_running = False


def gerakkan_merah():
    maze_list = cfg.maze_list
    i, j = cfg.merah_coord

    if maze_list[i][j - 1] == "+":
        cfg.merah_coord = (i, j - 1)
    if maze_list[i][j + 1] == "+":
        cfg.merah_coord = (i, j + 1)
    if maze_list[i - 1][j] == "+":
        cfg.merah_coord = (i - 1, j)
    if maze_list[i + 1][j] == "+":
        cfg.merah_coord = (i + 1, j)

    x, y = cfg.merah_coord
    cfg.maze_list[i][j] = " "
    cfg.maze_list[x][y] = "S"


def update_maze_list():
    cfg.maze_list = [list(row) for row in cfg.maze.tostring(entrances=True, solutions=True).strip().split('\n')]
