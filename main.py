import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (drawable, updatable, shots)
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    AsteroidField()
    print("Starting Asteroids with pygame version: 3.13")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
   
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for floating_thing in asteroids:
            if floating_thing.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for aste in asteroids:
            for bullet in shots:
                if aste.collides_with(bullet) == True:
                    log_event("asteroid_shot")
                    aste.kill()
                    bullet.kill()
                    

        pygame.display.flip()
        dt = clock.tick(60)/1000
        

        
if __name__ == "__main__":
    main()
