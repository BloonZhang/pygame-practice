# Tutorial 2, dealing with images

import pygame
import time

pygame.init()

display_width = 800
display_height = 600

# Create display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A bit Racey")


# Values for colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# Value for car width
car_width = 73

# Create the clock
clock = pygame.time.Clock()


# Create the car LOL
carImg = pygame.image.load("racecar.png")


# Create a function to draw the car
def car(x, y):
  # Draws a Surface onto the gameDisplay Surfact
  gameDisplay.blit(carImg, (x, y))


# Create a function for returning text objects
def text_objects(text, font):
  # Creates a surface with the text rendered on it
  textSurface = font.render(text, True, black)
  # Returns the surface itself, and also the rectangle
  return textSurface, textSurface.get_rect()


# Create a function for displaying a message
def message_display(text):
  # Define a font
  largeText = pygame.font.Font("freesansbold.ttf", 115)
  # Define the text and the rectange that surrounds the text
  TextSurf, TextRect = text_objects(text, largeText)
  # Center the text
  TextRect.center = ((display_width / 2), (display_height / 2))
  # Draws the text (in the background, we need to update the display)
  gameDisplay.blit(TextSurf, TextRect)

  # Updates the display
  pygame.display.update()
  time.sleep(2)


# Function that runs after you crash
def crash():
  # Displays a message
  message_display("You Crashed")


# ###### Game loop ########
def gameLoop():
  # initial x and y positions
  x = (display_width * 0.45)
  y = (display_height * 0.8)
  # initial x_change and car_speed
  x_change = 0
  # car_speed = 0
  # gameExit flag
  gameExit = False

  while not gameExit:
    for event in pygame.event.get():
      # Testing if game has closed
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      ##############
      # Getting user input: arrow keys
      # If the event was a key press
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x_change = -5
        elif event.key == pygame.K_RIGHT:
          x_change = 5
      # IF the event was a key coming back up
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          x_change = 0
      ##############
      x = x + x_change
      ##############

    # Fills the Suface with white
    gameDisplay.fill(white)
    # Draws the car on the x and y coordinates
    car(x, y)

    # If the car has gone too far
    if x > display_width - car_width or x < 0:
      crash()
      gameExit = True

    # Updates the display
    pygame.display.update()
    # Stalls the clock
    clock.tick(60)

 # ###### End game loop ########


while True:
  gameLoop()

pygame.quit()
quit()
