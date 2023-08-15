import pygame
from utilities import load_sprite_sheets
from objects import Object


class Enemy(Object):
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
    ANIMATION_DELAY = 6

    def __init__(self, x, y, width, height, patrol_points):
        super().__init__(x, y, width, height)
        self.rect = pygame.Rect(x, y, width, height)
        self.patrol_points = patrol_points
        self.current_point = 0
        self.speed = 2
        self.direction = "left"
        self.animation_count = 0
        self.animation_name = "run"
        self.update_sprite()
    
    def update_sprite(self):
        sprite_sheet_name = self.animation_name + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def patrol(self):
        target_x, _ = self.patrol_points[self.current_point]
        if self.rect.x < target_x:
            self.rect.x += self.speed
            self.direction = "right"
        elif self.rect.x > target_x:
            self.rect.x -= self.speed
            self.direction = "left"
        else:
            self.current_point = (self.current_point + 1) % len(self.patrol_points)

        self.update_sprite()
