for num in range(100, 1000):
    b = str(num)
    s = int(b[0])**3 + int(b[1])**3 + int(b[2])**3
    if s == num:
        print(num)