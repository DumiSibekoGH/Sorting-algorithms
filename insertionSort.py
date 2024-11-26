def sort(list):
    for i in range(1, len(list)):  # iterate through the array
        index = i
        val = list.pop(i)
        for j in range(i - 1, -1, -1):  # iterate through the array
            if list[j] > val:
                index = j
        list.insert(index, val)

    return list