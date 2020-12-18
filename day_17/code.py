# Inspired by https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/gg6wehc/ with modifications by me
import numpy as np
from scipy.signal import convolve

with open('input.txt') as f: # Get input data and change active to 1 and inactive to 0. Put data to numpy array
    data = np.array([list(map(lambda x: 1 if x == '#' else 0, line.strip())) for line in f], dtype=np.uint8)

def cycle(init, dim, gen=6): 
    grid = init.reshape([1] * (dim - len(init.shape)) + list(init.shape)) # Reshape data to 1 dimension higher than before: 8x8 -> 1x8x8
    kernel = np.ones([3] * dim, dtype=np.uint8) # make kernel 3x3x3 or 3x3x3x3 etc depending on the dimesion
    for i in range(gen): # run simulation for gen number of cycles
        nb = convolve(grid, kernel) # count neighbors+itself. Basically multiplies every item in grid-array with a array of ones. 
        grid = np.pad(grid, 1) & (nb == 4) | (nb == 3)  # Do Conway GoL rules using bitwise operators for every item in array. 
                                                        # If active in padded grid AND has 4 neighbors (3+itself) then STAY ACTIVE
                                                        # If active in padded grid but does NOT have 4 neighbors then INACTIVE but if has 3 neighbors (2+itself) then STAY ACTIVE 
                                                        # If inactive in padded grid then STAY INACTIVE but if 3 neighbors (3+0 [itself is inactive = 0]) then become ACTIVE
    return np.sum(grid) # Count active. Because actives are 1 then counting them is the same as adding everything in the array together.

""" If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive."""


# Part 1
print("Part1:", cycle(data, 3)) # run simulation with 3D

# Part 2
print("Part2:", cycle(data, 4)) # run simulation with 4D