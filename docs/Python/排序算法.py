def bubblesort(list):
    length = len(list)
    for i in range(1, length):
        flag = True
        for j in range(length - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = False
        if flag:
            return list
    return list


def selectionsort(list):
    length = len(list)
    for i in range(length):
        minindex = i
        for j in range(i + 1, length):
            if list[j] < list[minindex]:
                minindex = j
        if i != minindex:
            list[i], list[minindex] = list[minindex], list[i]
    return list


def insertsort(list):
    length = len(list)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
    return list


def quicksort(list, start, end):
    if start < end:
        mid = start
        left, right = start, end
        while left < right:
            while list[left] < list[mid] and left < right:
                left += 1
            while list[right] >= list[mid] and left < right:
                right -= 1
            if left < right:
                list[left], list[right] = list[right], list[left]
        list[mid], list[left] = list[left], list[mid]
        quicksort(list, start, mid - 1)
        quicksort(list, mid + 1, end)


def shellsort(list):
    pass