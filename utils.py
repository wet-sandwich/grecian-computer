def get_radial(disks, index, rotations):
    """Return a list of the visible numbers in a radial for a given configuration."""
    # get a list of the radials for each disk for the given index and rotation set
    radials = []
    for disk in range(5):
        # inserting at zero allows us to flip the order of the disk radials (we
        # put the top most disk first), making it easier to determine which numbers
        # are visible in the next step
        radials.insert(0, _get_disk_radial(disks[disk], index, rotations[disk]))

    # determine which numbers are visible for this radial
    radial = []
    for ring in range(4):
        disk = 0
        while radials[disk][ring] == 0:
            disk += 1
        radial.append(radials[disk][ring])
    return radial

def _get_disk_radial(disk, index, rotation):
    """Return a list of numbers for a given disk radial."""
    radial = []
    for ring in range(4):
        radial.append(disk[ring][(index + rotation) % 12])
    return radial

def radial_sum(rad):
    """Return the sum of the visible numbers in a radial."""
    return rad[0] + rad[1] + rad[2] + rad[3]
