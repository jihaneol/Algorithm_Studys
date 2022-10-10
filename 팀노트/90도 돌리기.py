def rotation(a):
    r= len(a)
    c= len(a[0])
    arr = [[0]*r for _ in range(c)]
    for x in range(r):
        for y in range(c):
            arr[y][r-1-x] = a[x][y]
    return arr 