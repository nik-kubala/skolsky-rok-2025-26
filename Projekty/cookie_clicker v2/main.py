from inspect import _void
import pygame
import random

SIRKA = 500
VYSKA = 500

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SIRKA, VYSKA))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# --- Load and Scale Image ---
# Load the image with transparency
ball_image = pygame.image.load("Projekty/cookie_clicker v2/assets/ball.png").convert_alpha()
# Scale the image to the desired size (60x60 pixels)
ball_image = pygame.transform.smoothscale(ball_image, (60, 60))
# Get the rect of the image to make positioning easier
ball_rect = ball_image.get_rect()
# --- End Image Load ---

# --- Obstacle Rectangle Setup ---
obstacle_color = "white"
obstacle_rect = pygame.Rect(100, 350, 300, 20)  # x, y, width, height
# --- End Obstacle Setup ---

# --- Motion Blur Setup ---
# Create a surface that will be used to fade the screen.
blur_surface = pygame.Surface(screen.get_size())
blur_surface.fill((0, 0, 0))  # Fill with black
# Set the alpha for the whole surface. A lower value means a longer trail.
blur_surface.set_alpha(60)  # Adjusted for better visibility with an image
# --- End Motion Blur Setup ---

# rec okrajov
screen_rect = screen.get_rect()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Instead of clearing the screen, draw the transparent surface
    # to create a motion blur/trail effect.
    screen.blit(blur_surface, (0, 0))

    # --- Draw Obstacle ---
    pygame.draw.rect(screen, obstacle_color, obstacle_rect)
    # --- End Draw Obstacle ---

    # --- Draw Image ---
    # Center the image's rect on the player's position vector
    ball_rect.center = player_pos
    # Draw the ball image onto the screen
    screen.blit(ball_image, ball_rect)
    # --- End Draw Image ---
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 600 * dt
    if keys[pygame.K_s]:
        player_pos.y += 600 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt

    # --- Screen Edge Collision ---
    # 1. Synchronize the rect's center with the player_pos vector.
    ball_rect.center = player_pos

    # 2. Clamp the rect to the screen boundaries. This modifies ball_rect in-place.
    ball_rect.clamp_ip(screen_rect)

    # 3. Synchronize the player_pos vector back to the (potentially altered) rect's center.
    player_pos.x = ball_rect.centerx
    player_pos.y = ball_rect.centery
    # --- End Screen Edge Collision ---
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
