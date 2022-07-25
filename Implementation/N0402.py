position = input()
x, y = (ord(position[0]) - 96), int(position[1])

move_types = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0

for move in move_types:
    dx = x + move[0]
    dy = y + move[1]

    if (dx < 1) or (dy < 1) or (dx > 8) or (dy > 8):
        continue

    count += 1

print(count)