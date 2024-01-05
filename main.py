from data import disks
from utils import get_radial, radial_sum

def solve_puzzle(disks):
    """Find the set of counter-clockwise rotations for each disk, such that each radial sums to 42."""
    for i in range(12):
        for j in range(12):
            for k in range(12):
                for l in range(12):
                    rotations = [0, i, j, k, l]
                    solved_radials = 0
                    for index in range(12):
                        radial = get_radial(disks, index, rotations)
                        if radial_sum(radial) != 42:
                            break
                        solved_radials += 1
                    if solved_radials == 12:
                        return rotations

solution = solve_puzzle(disks)
print("Solution: ", solution)
