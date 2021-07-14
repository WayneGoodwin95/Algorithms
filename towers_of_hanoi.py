"""
Towers of Hanoi
    Only one peg can be moved at one time
    Cant place larger peg on top of smaller peg
"""


# loop through items in each tower --> if disc present print disc else print nothing
def towers_print(towers, discs):
    print('Move Next Disc')
    output = ""
    for disc in range(discs, -1, -1):
        for tower in range(len(towers)):
            if len(towers[tower]) > disc:
                output += " " + str(towers[tower][disc])
            else:
                output += " "
        output += '\n '
    return output


def move_disc(towers, from_tower, dest_tower):
    # remove last disc from tower, retain it in placeholder
    disc = towers[from_tower].pop()
    # add disc to top of destination tower
    towers[dest_tower].append(disc)


def solve_tower_of_hanoi(towers, disc, start_tower, dest_tower, aux_tower):
    # Base-case if disc = 0 then stop recursion
    if disc == 0:
        return

    # Recursive case
    # Move disc to auxilary tower
    solve_tower_of_hanoi(towers, disc - 1, start_tower, aux_tower, dest_tower)
    move_disc(towers, start_tower, dest_tower)
    print(towers_print(towers, discs))
    # move disc from aux to destination
    solve_tower_of_hanoi(towers, disc - 1, aux_tower, dest_tower, start_tower)


# Setting up the discs and towers. Discs all placed on first tower
discs = 5
num_towers = 3
towers = [[]]*num_towers
towers[0] = [i for i in range(discs, 0, -1)]
towers[1] = []
towers[2] = []

# Naming the towers for readability and moving them
start_tower, dest_tower, aux_tower = 0, 2, 1

# show the starting towers before any move
print(towers_print(towers, discs))

# Start Recursive Algorithm
solve_tower_of_hanoi(towers, discs, start_tower, dest_tower, aux_tower)

