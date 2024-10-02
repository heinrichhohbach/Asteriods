# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()




    #print("Starting asteroids!")
    #print("Screen width: " + str(SCREEN_WIDTH))
    #print("Screen height: " + str(SCREEN_HEIGHT))

# Call the main function
if __name__ == "__main__":
    main()
