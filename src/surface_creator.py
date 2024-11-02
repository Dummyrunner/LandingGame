import pygame


def create_pg_surface_from_color_and_size(color, size):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf
