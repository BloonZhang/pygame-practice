# Tutorial 2, dealing with images

import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Create display
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("A bit Racey")


# Values for black and white
black = (0, 0, 0)
white = (255, 255, 255)

# Create the clock
clock = pygame.time.Clock()
# Crashed flag
crashed = False

# Create the car LOL
carImg = pygame.image.load("racecar.png")


# Create a function to draw the car
def car(x, y):
  # Draws a Surface onto the gameDisplay Surfact
  gameDisplay.blit(carImg, (x, y))


# initial x and y positions
x = (DISPLAY_WIDTH * 0.45)
y = (DISPLAY_HEIGHT * 0.8)


# Game loop
while not crashed:
  for event in pygame.event.get():
    # Testing if game has closed
    if event.type == pygame.QUIT:
      crashed = True

  # Fills the Suface with white
  gameDisplay.fill(white)
  # Draws the car on the x and y coordinates
  car(x, y)

  # Updates the display
  pygame.display.update()
  # Stalls the clock
  clock.tick(60)


# At this point, the game is done
pygame.quit()
quit()
