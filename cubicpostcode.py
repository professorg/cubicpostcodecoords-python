#!/bin/python3
from math import sqrt, floor
from numpy import array, clip

EDGE = 21000000
CUBESPERLAYER = EDGE * EDGE
DEBUG = False

n = 0


def debug_print(*args):
    if DEBUG:
        print(*args)

def loop(n):
    # Bail out on non-postive numbers
    if n < 1:
        return
    # Integer division to find layer
    layer = n // CUBESPERLAYER
    # Mod to find remainder
    remainder = n % CUBESPERLAYER
    # Largest even square less than remainder
    last_sqrt = int(floor(sqrt(remainder - 1)))
    last_even_sqrt_index = last_sqrt // 2       # The "n"th even square (0=0th, 4=1st)
    last_even_sqrt = last_even_sqrt_index * 2   # The sqrt of the even square
    last_even_sqr = last_even_sqrt ** 2         # The even square itself
    # Coords vector
    coords = array([-last_even_sqrt_index, last_even_sqrt_index])   # nth loop top left coords
    # Edge length for this loop, not including last
    local_edge = last_even_sqrt + 1
    # Index within this loop (0th=top left, last=below top left)
    loop_index = remainder - last_even_sqr - 1
    debug_print("loop index: ", loop_index)
    # Index at each corner, clockwise from top left
    weights = array(range(4)) * local_edge
    debug_print("weights: ", weights)
    # Subtract each from index to find distance traveled on each edge
    distances = loop_index - weights
    debug_print("distances: ", distances)
    # Clamp to [0, local_edge]
    clamped_distances = clip(distances, 0, local_edge)
    debug_print("clamped distances: ", clamped_distances)
    directions = array([[1,0], [0,-1], [-1,0], [0,1]])
    # Generate steps to add
    steps = array([a * b for a, b in list(zip(clamped_distances, directions))])
    debug_print("steps: ", steps)
    # Find displacement by summing steps
    displacement = sum(steps)
    # Add to coords
    coords += displacement

    x = layer
    y = coords[0]
    z = coords[1]

    print((x, y, z))

while (n != -1):
    n = int(input("N: "))
    loop(n)

