import pygame
from player import Player
from objects import Block, Fire
from enemy import Enemy
from utilities import get_background, handle_move, draw, HEIGHT, WIDTH, FPS
from load_level import *
from win_condition import Checkpoint, check_win_condition

pygame.init()
pygame.display.set_caption("Platfromer")

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    checkpoint_positions = [WIDTH - block_size, WIDTH - block_size * 2, WIDTH - block_size * 3]
    checkpoints = [Checkpoint(x, HEIGHT - block_size, block_size) for x in checkpoint_positions]

    current_level = 0
    total_levels = len(levels)
    running = True
    previous_level = current_level


    player = Player(100,100,50,50)
    fire = Fire(100, HEIGHT - 96 - 64, 16, 32)
    fire.on()

    # Load the desired level (e.g., level 0)
    level_index = 0
    objects = load_level(level_index)

    offset_x = 0
    scroll_area_width = 200

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
            
        player.loop(FPS)
        fire.loop()
        for obj in objects:
            if isinstance(obj, Enemy):
                obj.patrol()


        checkpoint = levels[current_level]['checkpoint']
        game_over, current_level = check_win_condition(player, checkpoint, current_level, total_levels)

        if game_over:
            print("Congratulations! You have completed the game!")
            running = False
            break  # Exit the loop immediately
        else:
            if current_level != previous_level:
                objects = load_level(current_level)
                previous_level = current_level



        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x)
        for obj in objects:
            if player.rect.colliderect(obj.rect) and isinstance(obj, Enemy):
                if player.y_vel > 0 and player.rect.bottom <= obj.rect.top + 10:
                    print("Enemy defeated!")
                    objects.remove(obj) # Remove the enemy from the objects list
                else:
                    print("Game Over!") # You can replace this with any other action
                    running = True


        if((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0 ) or ((player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()

if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
