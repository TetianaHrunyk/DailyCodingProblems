"""
On our special chessboard, two bishops attack each other if they share the same 
diagonal. This includes bishops that have another bishop located between them, 
i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M 
chessboard. Write a function to count the number of pairs of bishops that 
attack each other. The ordering of the pair doesn't matter:
    (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:
    (0, 0),(1, 2), (2, 2), (4, 0)
The board would look like this:
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other,
 as well as bishops 3 and 4.
"""

def add_new_bishop(location, attack_positions, board_size):
    # count how many times existing bishops can attack
    count = 0
    if location in attack_positions:
        count += 1

    # add new attack positions for future bishops
    new_attack_positions = list()

    i, j = location
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        new_attack_positions.append((i, j))
    i, j = location
    while i > 0 and j < board_size - 1:
        i -= 1
        j += 1
        new_attack_positions.append((i, j))
    i, j = location
    while i < board_size - 1 and j > 0:
        i += 1
        j -= 1
        new_attack_positions.append((i, j))
    i, j = location
    while i < board_size - 1 and j < board_size - 1:
        i += 1
        j += 1
        new_attack_positions.append((i, j))

    attack_positions.extend(new_attack_positions)

    return count, attack_positions


def get_attack_vectors(bishop_locations, board_size):
    attack_positions = list()
    total_count = 0
    for location in bishop_locations:
        count, attack_positions = add_new_bishop(
            location, attack_positions, board_size)
        total_count += count

    return total_count


assert get_attack_vectors([(0, 0), (1, 2), (2, 2), (4, 0)], 5) == 2
assert get_attack_vectors([(0, 0), (1, 2), (2, 2)], 5) == 1