from objects import Block


class Checkpoint(Block):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        # You can customize the appearance of the checkpoint here

def check_win_condition(player, checkpoint, current_level, total_levels):
    if player.rect.colliderect(checkpoint.rect):
        current_level += 1
        if current_level >= total_levels:
            print("Congratulations! You have completed the game!")
            return True, current_level
        else:
            print(f"Level {current_level} completed! Moving to next level...")
            return False, current_level
    return False, current_level

