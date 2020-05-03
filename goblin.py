import pygame
from pygame.time import Clock
import math
pygame.init()

width, height = 800,500
screen = pygame.display.set_mode((width, height))
clock = Clock()
fps = 60

centre = (width // 2, height // 2)
pool_radius = 150
px, py = centre
gx, gy =  width // 2, pool_radius + height // 2
gspeed = 2
step = 1

#colours
BLACK = (0,0,0)
BLUE = (0,200,255)
RED = (255,0,0)
YELLOW = (190,255,200)

def abs(num: int):
    return num if num > 0 else -num

def sign(number: int):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    elif number == 0:
        return 0
    else:
        return None

def draw():
    global px, py, gx, gy
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        #if event.type == pygame.MOUSEMOTION:pass #event.type == pygame.MOUSEBUTTONDOWN or 

    # move player according to mouse clicks
    mx, my = pygame.mouse.get_pos()
    
    newx = step * sign(mx - px) #* abs(mx - px - centre[0])
    newy = step * sign(my - py) #* abs(my - py - centre[1])
    
    # if swimmer is inside pool then mvoe swimmer
    if (px + newx - centre[0]) ** 2 + (py + newy - centre[1]) ** 2 <= pool_radius ** 2:
        px += newx
        py += newy

    angle = math.atan2(py - centre[1], px - centre[0])
    gx = centre[0] + int(pool_radius * math.cos(angle))
    gy = centre[1] + int(pool_radius * math.sin(angle))
    # if goblin catches swimmer
    if (px - gx) ** 2 + (py - gy) ** 2 < 25:
        print("You lose!\nGoblin caught you!")
        pygame.quit()
        exit()

            # move goblin
            
    # draw the pool
    pygame.draw.circle(screen, BLUE, (width // 2, height // 2), pool_radius)
    # draw goblin
    pygame.draw.circle(screen, RED, (gx, gy), 5)
    #draw swimmer
    pygame.draw.circle(screen, YELLOW, (px,py), 5)

    clock.tick(fps)
    pygame.display.update()

def start():
    while True:
        draw()

if __name__ == "__main__":
    start()