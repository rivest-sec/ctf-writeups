maxu = 0xFFFFFFFF + 1

for i in range(1, 10**10):
    if (1000 * i) % maxu <= 50:
        print(i)
        break
