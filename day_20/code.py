import re
import numpy as np


with open("input.txt") as file:
    tiles_with_tile_numbers = file.read().split('\n\n')

tiles = {}
for tile in tiles_with_tile_numbers:
    tile_number = int(tile.splitlines()[0][5:9])
    tile_contents = np.array([list(map(lambda x: 1 if x == '#' else 0, line.strip())) for line in tile.splitlines()[1:]])
    # print(tile_number)
    # print(tile_contents)
    tiles[tile_number] = tile_contents


[print(number, value, "\n", sep='\n') for number,value in tiles.items()]