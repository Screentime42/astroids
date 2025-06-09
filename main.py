import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
   pygame.init()
   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()
   
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()

   Asteroid.containers = (asteroids, updatable, drawable)
   AsteroidField.containers = updatable
   asteroid_field = AsteroidField()


   Player.containers = (updatable, drawable)

   # player object in middle of screen
   player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

   dt = 0

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
         
      pygame.Surface.fill(screen, (0, 0, 0))
      
      # update all updatable objects
      updatable.update(dt)

      for asteroid in asteroids:
         if asteroid.collisionCheck(player):
            print("Game over!")
            sys.exit()

      # update all drawable objects
      for obj in drawable:
         obj.draw(screen)
      
      pygame.display.flip()

      # limit frame rate to 60fps
      dt = clock.tick(60) / 1000

if __name__ == "__main__":
   main()
