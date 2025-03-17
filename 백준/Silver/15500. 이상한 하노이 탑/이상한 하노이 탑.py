import sys
from collections import deque

input = sys.stdin.readline

def move_disk(source, destination, disk_positions, moves, pole_1, pole_2, pole_3):
    disk = source.pop()
    disk_positions[disk] = get_pole_number(destination, pole_1, pole_2, pole_3)
    destination.append(disk)
    moves.append((get_pole_number(source, pole_1, pole_2, pole_3), 
                  get_pole_number(destination, pole_1, pole_2, pole_3)))

def get_pole_number(pole, pole_1, pole_2, pole_3):
    if pole is pole_1:
        return 1
    elif pole is pole_2:
        return 2
    elif pole is pole_3:
        return 3
    return -1

def solve_hanoi(n, pole_1):
    pole_2, pole_3 = deque(), deque()
    moves = []
    disk_positions = {i: 1 for i in range(1, n + 1)}

    for target_disk in range(n, 0, -1):
        while True:
            if (disk_positions[target_disk] == 1 and pole_1[-1] == target_disk) or \
               (disk_positions[target_disk] == 2 and pole_2[-1] == target_disk):
                move_disk(pole_1 if disk_positions[target_disk] == 1 else pole_2, 
                          pole_3, disk_positions, moves, pole_1, pole_2, pole_3)
                break
            else:
                move_disk(pole_1 if disk_positions[target_disk] == 1 else pole_2, 
                          pole_2 if disk_positions[target_disk] == 1 else pole_1, 
                          disk_positions, moves, pole_1, pole_2, pole_3)

    print(len(moves))
    for move in moves:
        print(*move)

if __name__ == "__main__":
    n = int(input().strip())
    pole_1 = deque(map(int, input().split()))
    solve_hanoi(n, pole_1)
