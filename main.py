# this allows us  to use code from 
# the open-source pygame library 
# thoughout this file 
import pygame 
# import the connect_database function and the database_version variable from database.py 
# from database import connect_database, database_version 
from constants import *


def main():
    pygame.init()        
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return

            
            screen.fill("black")
            pygame.display.flip()







if __name__ == "__main__": 
        main()
