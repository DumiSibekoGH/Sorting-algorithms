# choose pivot
# partition
# recursively call sort(arg)
# base case

def sort(list):
    if len(list) <= 1:
        # base case
        return list
    else:
        # recursive case
        pivot = list[0]
        sub_left = []
        sub_right = []

        #partition
        for i in list[1:]:
            if i <= pivot:
                sub_left.append(i)
            else:
                sub_right.append(i)

        # recursive call
        return sort(sub_left) + [pivot] + sort(sub_right)