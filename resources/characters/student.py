# Importing the necessary modules for creating a simple pixel art character
import numpy as np

# Define the pixel art character
# 0: Empty, 1: Skin, 2: Clothes, 3: Eyes, 4: Shoes
character = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 3, 1, 3, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 2, 2, 1, 2, 2, 0, 0],
    [0, 0, 2, 1, 1, 1, 2, 0, 0],
    [0, 0, 2, 2, 2, 2, 2, 0, 0],
    [0, 0, 4, 4, 4, 4, 4, 0, 0],
])

# Define the color mapping
colors = {
    0: (255, 255, 255),  # White for empty space
    1: (255, 228, 196),  # Skin color
    2: (0, 128, 128),    # Clothes color (teal)
    3: (0, 0, 0),        # Eyes color (black)
    4: (139, 69, 19)     # Shoes color (brown)
}

# Create an RGB array to represent the character in color
character_rgb = np.zeros((character.shape[0], character.shape[1], 3), dtype=np.uint8)
for i in range(character.shape[0]):
    for j in range(character.shape[1]):
        character_rgb[i, j] = colors[character[i, j]]
