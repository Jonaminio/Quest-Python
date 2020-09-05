c1: float = 80000
c2: float = 200000
i = 0
while c1 < c2:
    c1 = c1 + (c1 * 3 // 100)
    c2 = c2 + round((c2 * 1.5 // 100))
    i += 1
    if c1 > c2:
        print(f'Em {i} anos o país 1 vai ultrapassar a população do país 2 com  {c1} e {c2} respectivamente')
