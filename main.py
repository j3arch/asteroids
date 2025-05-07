import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:               # Check for player-asteroid collisions
            if player.collides_with(asteroid):
                print("Game over!")
                import sys
                sys.exit()

            for shot in shots:                   # Bullet-asteroid collision
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()


        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()