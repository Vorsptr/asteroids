import pygame
from constants import *
from player import Player

def main():
    print(f'''
          Starting asteroids!
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}
          ''')
    pygame.init()
    fpsClock = pygame.time.Clock()
    dt = 0
    
    pygame.display.set_caption('Asteroids')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()
        time = fpsClock.tick(60)
        dt = time / 1000
        print(dt)
        
    
if __name__ == '__main__':
    main()