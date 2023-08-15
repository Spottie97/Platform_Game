import pygame
from objects import Block
from enemy import Enemy
from utilities import load_sprite_sheets
from objects import Object

WIDTH = 1000
HEIGHT = 800
block_size = 96
enemy_y = HEIGHT - block_size - 50
enemy_height = 50
last_block_x = (143 + 5) * block_size

class Checkpoint(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "checkpoint")
        self.image_path = "assets/Items/Checkpoints/End_Idle.png"
        self.image = pygame.image.load(self.image_path)
        if self.image:
            self.image = pygame.transform.scale(self.image, (size, size))  # Scale to the desired size
            self.mask = pygame.mask.from_surface(self.image)
        else:
            print("Checkpoint image not found!")

    def draw(self, win, offset_x):
        if self.image:
            win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


# Define levels
levels =[{
    'terrain': [
        *([Block(i * block_size, HEIGHT - block_size, block_size) for i in range(20)]),  # Flat ground
        *([Block((23 + i) * block_size, HEIGHT - block_size, block_size) for i in range(10)]),  # Pitfall of 3 blocks
        *([Block((36 + i) * block_size, HEIGHT - block_size, block_size) for i in range(15)]),  # Flat ground
        *([Block((54 + i) * block_size, HEIGHT - block_size, block_size) for i in range(20)]),  # Pitfall of 3 blocks
        *([Block((78 + i) * block_size, HEIGHT - block_size, block_size) for i in range(25)]),  # Flat ground
        *([Block((108 + i) * block_size, HEIGHT - block_size, block_size) for i in range(30)]),  # Pitfall of 3 blocks
        *([Block((143 + i) * block_size, HEIGHT - block_size * (i + 1), block_size) for i in range(5)]),  # Staircase
    ],
    'enemies': [
        Enemy(block_size * 1, HEIGHT - block_size - enemy_height, 50, enemy_height, [(block_size * 1, enemy_y), (block_size * 3, enemy_y)]),
        Enemy(block_size * 13, HEIGHT - block_size - enemy_height, 50, enemy_height, [(block_size * 13, enemy_y), (block_size * 15, enemy_y)]),
        # Add more enemies as needed
    ],
    'checkpoint': Checkpoint(last_block_x, HEIGHT - block_size, block_size),
    },
    {
        'terrain': [
            *([Block(i * block_size, HEIGHT - block_size, block_size) for i in range(20)]),  # Flat ground
            *([Block((23 + i) * block_size, HEIGHT - block_size, block_size) for i in range(10)]),  # Pitfall of 3 blocks
            *([Block((36 + i) * block_size, HEIGHT - block_size, block_size) for i in range(15)]),  # Flat ground
            *([Block((54 + i) * block_size, HEIGHT - block_size, block_size) for i in range(20)]),  # Pitfall of 3 blocks
            *([Block((78 + i) * block_size, HEIGHT - block_size, block_size) for i in range(25)]),  # Flat ground
            *([Block((108 + i) * block_size, HEIGHT - block_size, block_size) for i in range(30)]),  # Pitfall of 3 blocks
            *([Block((143 + i) * block_size, HEIGHT - block_size * (i + 1), block_size) for i in range(5)]),  # Staircase
        ],
        'enemies': [
            Enemy(400, enemy_y, 50, enemy_height, [(400, enemy_y), (600, enemy_y)]),
        ],
        'checkpoint': Checkpoint(last_block_x, HEIGHT - block_size, block_size),
    },
    {
        'terrain': [
            *([Block(i * block_size, HEIGHT - block_size, block_size) for i in range(20)]),
            *([Block((22 + i) * block_size, HEIGHT - block_size, block_size) for i in range(10)]),
            *([Block((35 + i) * block_size, HEIGHT - block_size, block_size) for i in range(15)]),
            *([Block((55 + i) * block_size, HEIGHT - block_size, block_size) for i in range(20)]),
            *([Block((80 + i) * block_size, HEIGHT - block_size, block_size) for i in range(25)]),
            *([Block((110 + i) * block_size, HEIGHT - block_size, block_size) for i in range(30)]),
            *([Block((140 + i) * block_size, HEIGHT - block_size * (i + 1), block_size) for i in range(5)]),
        ],
        'enemies': [
            Enemy(500, enemy_y, 50, enemy_height, [(500, enemy_y), (700, enemy_y)]),
        ],
        'checkpoint': Checkpoint(last_block_x, HEIGHT - block_size, block_size),
    },
]

# Function to load a level
def load_level(level_index):
    level = levels[level_index]
    objects = level['terrain'] + level['enemies'] + [level['checkpoint']]
    return objects
