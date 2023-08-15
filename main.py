import pygame
from player import Player
from objects import Block, Fire
from enemy import Enemy
from utilities import get_background, handle_move, draw, HEIGHT, WIDTH, FPS

pygame.init()
pygame.display.set_caption("Platfromer")

##Main 
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    block_size = 96

    player = Player(100,100,50,50)
    fire =Fire(100, HEIGHT - block_size - 64, 16, 32)
    fire.on()
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]
    objects = [*floor, Block(0,HEIGHT - block_size * 2, block_size), Block(block_size * 3,HEIGHT - block_size * 4, block_size), fire]

    enemy_height = 50
    enemy_y = HEIGHT - block_size - enemy_height
    enemy = Enemy(300, enemy_y, 50, enemy_height, [(300, enemy_y), (500, enemy_y)])
    objects.append(enemy)



    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
            
        player.loop(FPS)
        fire.loop()
        enemy.patrol()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x)
        for obj in objects:
            if player.rect.colliderect(obj.rect) and isinstance(obj, Enemy):
                if player.y_vel > 0 and player.rect.bottom <= obj.rect.top + 10:
                    print("Enemy defeated!")
                    objects.remove(obj) # Remove the enemy from the objects list
                else:
                    print("Game Over!") # You can replace this with any other action
                    run = True


        if((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0 ) or ((player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()

if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
