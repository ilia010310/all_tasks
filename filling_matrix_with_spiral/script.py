n, m = [int(i) for i in input().split()]
matrix = []
number = -1
turn = 0
for _ in range(n):
    matrix.append([0] * m)
directions = ['right', 'down', 'left', 'up']
chek_directions = 0
i = 0
j = 0
for k in range(1, n * m + 1):
    while directions[chek_directions] == 'right':
        matrix[i][j] = k
        j += 1
        if j == m:
            j -= 1
            chek_directions += 1

        break
    if matrix[i][j] == k:
        i += 1
        continue
    while directions[chek_directions] == 'down':
        matrix[i][j] = k
        i += 1
        if i == n:
            chek_directions += 1

            i -= 1
        break
    if matrix[i][j] == k:
        j -= 1
        continue

    while directions[chek_directions] == 'left':
        matrix[i][j] = k
        j -= 1
        if j == number:
            chek_directions += 1
            j += 1
            number += 1

        break
    if matrix[i][j] == k:
        i -= 1
        continue

    while directions[chek_directions] == 'up':
        matrix[i][j] = k
        i -= 1
        if i == turn:
            chek_directions = 0
            i += 1
            n -= 1
            m -= 1
        break
    if matrix[i][j] == k:
        turn += 1
        j += 1
        continue

for l in range(len(matrix)):
    print(*matrix[l])



