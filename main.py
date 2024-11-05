import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f'''
          Starting asteroids!
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}
          ''')
    pygame.init()
    fpsClock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    pygame.display.set_caption('Asteroids')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updateable,drawable)
    Asteroid.containers = (updateable,drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateable:
            obj.update(dt)
        screen.fill('black')
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.collosionCheck(player):
                print('Game over!')
                sys.exit()
            for bullet in shots:
                if bullet.collosionCheck(obj):
                    bullet.kill()
                    obj.split()

        dt = fpsClock.tick(60) / 1000
        pygame.display.flip()
        
    
if __name__ == '__main__':
    main()