
def insertion_sort(list_to_sort):
    """
    To sortowanie jest stabilne
    """
    for index in range(len(list_to_sort)):
        while index > 0:
            if list_to_sort[index] < list_to_sort[index - 1]:
                list_to_sort[index], list_to_sort[index - 1] = list_to_sort[index - 1], list_to_sort[index]
                index -= 1
            else:
                break

    return list_to_sort


def selection_sort(list_to_sort):
    """
    To sortowanie nie jest stabilne
    """
    for i in range(len(list_to_sort)):
        min_ind = i
        for index in range(i, len(list_to_sort)-1):
            if list_to_sort[index+1] < list_to_sort[min_ind]:
                min_ind = index+1
        list_to_sort[i], list_to_sort[min_ind] = list_to_sort[min_ind], list_to_sort[i]

    return list_to_sort


if __name__ == "__main__":
    list1 = [101, 2, 3, 4, 10, 6, 3, 2, 2, -3, 1, 2]
    print(insertion_sort(list1))
    list2 = [101, 2, 3, 4, 104, 65, 32, 2, 1]
    print(selection_sort(list2))
