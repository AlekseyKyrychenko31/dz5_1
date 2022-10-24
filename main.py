


height = int(input('введите число'))
weight = 0
for h in range(height):
    for w in range(h):
        print('*', end=' ')
    print()
for h in range(height,0,-1):
    for w in range(0,h):
        print('*', end=' ')
    print()


