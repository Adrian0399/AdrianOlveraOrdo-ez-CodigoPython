
N=int(input("Mayor nivel a alcanzar: "))

for i in range(1, N + 1):
    for j in range(i):
        print('* ', end='')
    print()

for i in range(N -1, 0, - 1):
    for j in range(i):
        print('* ', end='')
    print()
