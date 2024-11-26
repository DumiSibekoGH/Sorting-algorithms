def sort(list):
    length = len(list)
    for i in range(1, length):
        for j in range(i):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
    return list