# First file using pygame!
import pygame

# Initialize pygame
pygame.init()

# Create main display for game. width, height
gameDisplay = pygame.display.set_mode((800, 600))
# Title of the window
pygame.display.set_caption("A bit Racey")

# Create the game clock
clock = pygame.time.Clock()

# Flag to see if there's an error in the game
crashed = False
# This is our game loop
while not crashed:
  for event in pygame.event.get():
    # If the user closes the window
    if event.type == pygame.QUIT:
      crashed = True
    # Print all the things we're doing! Wow
    print(event)

  # Update the entire surface
  pygame.display.update()
  clock.tick(60)

# This is what happens after crashed = True
# Ends our game
pygame.quit()
# Ends python
quit()
