import pygame
import sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH
from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    font = pygame.font.SysFont(None, 36)
    score_rect = pygame.Rect(10, 10, 150, 50)

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
    score = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        pygame.draw.rect(screen, "white", score_rect, LINE_WIDTH)
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (score_rect.x + 10, score_rect.y + 10))

        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(p1):
                log_event("player_hit")
                print("Game over!")
                print(f"Your score was {score}")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    log_event(score)
                    score += 1
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
