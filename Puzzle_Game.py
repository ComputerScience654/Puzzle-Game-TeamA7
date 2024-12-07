#นายนันทวุฒิ กองโภค CSS465415241024
#นายพีรพัฒน์ สอนน้อย CSS465415241008
import pygame
import random
import os

WIDTH, HEIGHT = 400, 400
ROWS, COLS = 4, 4 #จำนวนแถวและคอลัมที่ต้องการแบ่ง
TILE_SIZE = WIDTH // COLS
FPS = 60
WHITE = (255, 255, 255) 

def load_and_split_image(image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))

    tiles = []
    for y in range(ROWS):
        row = []
        for x in range(COLS):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            tile = image.subsurface(rect).copy()
            row.append(tile)
        tiles.append(row)
    
    tiles[-1][-1] = None
    return tiles

def swap(tiles, empty_tile, direction):
    x, y = empty_tile
    if direction == 'up' and y > 0:
        tiles[y][x], tiles[y - 1][x] = tiles[y - 1][x], tiles[y][x]
        return x, y - 1
    elif direction == 'down' and y < ROWS - 1:
        tiles[y][x], tiles[y + 1][x] = tiles[y + 1][x], tiles[y][x]
        return x, y + 1
    elif direction == 'left' and x > 0:
        tiles[y][x], tiles[y][x - 1] = tiles[y][x - 1], tiles[y][x]
        return x - 1, y
    elif direction == 'right' and x < COLS - 1:
        tiles[y][x], tiles[y][x + 1] = tiles[y][x + 1], tiles[y][x]
        return x + 1, y
    return empty_tile

def shuffle(tiles):
    empty_tile = COLS - 1, ROWS - 1
    for _ in range(1000):
        direction = random.choice(['up', 'down', 'left', 'right'])
        empty_tile = swap(tiles, empty_tile, direction)
    return empty_tile

def draw_tiles(win, tiles):
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if tile:
                win.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))

def is_solved(tiles, original_tiles):
    for y in range(ROWS):
        for x in range(COLS):
            if tiles[y][x] != original_tiles[y][x]:
                return False
    return True

def main(image_path):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PUZZLE GAME")
    clock = pygame.time.Clock()

    original_tiles = load_and_split_image(image_path)
    tiles = [row[:] for row in original_tiles] 
    empty_tile = shuffle(tiles)

    running = True
    while running:
        clock.tick(FPS)
        win.fill((0, 0, 0))

        draw_tiles(win, tiles)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    empty_tile = swap(tiles, empty_tile, 'up')
                elif event.key == pygame.K_DOWN:
                    empty_tile = swap(tiles, empty_tile, 'down')
                elif event.key == pygame.K_LEFT:
                    empty_tile = swap(tiles, empty_tile, 'left')
                elif event.key == pygame.K_RIGHT:
                    empty_tile = swap(tiles, empty_tile, 'right')

        if is_solved(tiles, original_tiles):
            print("you solved the puzzle!")
            running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    image_path = os.path.join(os.getcwd(),"D:/Users/MSI/Downloads/picture1.jpeg") #image_path = os.path.join(os.getcwd(),"ใส่pathของรูปที่ต้องการ")
    main(image_path)

