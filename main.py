import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = [asteroids, updatable, drawable]
    Player.containers = [updatable, drawable]
    AsteroidField.containers = [updatable]
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over")
                sys.exit()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
        dt = pygame.time.Clock().tick(60) / 1000


if __name__ == "__main__":
    main()
