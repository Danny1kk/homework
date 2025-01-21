list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(list):
    if list[a] < 0:
        break
    elif list[a] > 0:
        print(list[a])
    a += 1