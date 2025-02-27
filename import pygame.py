import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Player Settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 80
player_speed = 5

# Bullet Settings
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Enemy Settings
enemy_size = 50
enemy_speed = 3
enemies = []
enemy_spawn_rate = 30  # Lower is faster spawning

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game Loop Variables
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit number of bullets on screen
            bullets.append(pygame.Rect(player_x + player_size//2 - bullet_width//2, player_y, bullet_width, bullet_height))
    
    # Bullet Movement
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
    
    # Enemy Spawning
    if random.randint(1, enemy_spawn_rate) == 1:
        enemies.append(pygame.Rect(random.randint(0, WIDTH - enemy_size), 0, enemy_size, enemy_size))
    
    # Enemy Movement
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
    
    # Collision Detection
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
                break
    
    # Draw Player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    # Draw Bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    
    # Draw Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, GREEN, enemy)
    
    # Draw Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)  # Limit FPS to 30

pygame.quit()
