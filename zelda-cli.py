# Import necessary libraries
import sys
import random

# BIOS Startup Sequence
print('Starting BIOS...')

# Main Game Class
class ZeldaAdventure:
    def __init__(self):
        # Initialize game variables
        self.running = True
        self.current_scene = 'start'
        self.scenes = {
            'start': self.start_scene,
            'forest': self.forest_scene,
            'castle': self.castle_scene
        }

    def start_scene(self):
        print("You are in a dark forest. Do you go left or right?")
        choice = input(" > ")
        if choice == 'left':
            self.current_scene = 'castle'
        elif choice == 'right':
            self.current_scene = 'forest'
        else:
            print("Invalid choice. Choose 'left' or 'right'.")

    def forest_scene(self):
        print("You encounter a wild beast. Do you fight or flee?")
        choice = input(" > ")
        if choice == 'fight':
            print("Fight mechanics not implemented yet.")
            # Implement fight mechanics
        elif choice == 'flee':
            print("Flee mechanics not implemented yet.")
            # Implement flee mechanics
        else:
            print("Invalid choice. Choose 'fight' or 'flee'.")

    def castle_scene(self):
        print("You arrive at a mysterious castle. Do you enter or explore around?")
        choice = input(" > ")
        if choice == 'enter':
            print("Enter mechanics not implemented yet.")
            # Implement enter mechanics
        elif choice == 'explore':
            print("Explore mechanics not implemented yet.")
            # Implement explore mechanics
        else:
            print("Invalid choice. Choose 'enter' or 'explore'.")

    def update(self):
        # Update game state based on current scene
        scene_function = self.scenes.get(self.current_scene)
        if scene_function:
            scene_function()
        else:
            print("Scene not found:", self.current_scene)
            self.running = False

    def main_loop(self):
        # Main game loop
        while self.running:
            self.update()

# Create game instance and start the game
if __name__ == '__main__':
    game = ZeldaAdventure()
    game.main_loop()
