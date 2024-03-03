def remove_duplicates(array):
    if not array:
        return 0

    non_duplicate_index = 1

    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            array[non_duplicate_index] = array[i]
            non_duplicate_index += 1

    return non_duplicate_index

if __name__ == '__main__':
    # Test cases
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # Output: 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9]))  # Output: 6
    print(remove_duplicates([2, 2, 2, 11]))           # Output: 2
    print(remove_duplicates([2, 2, 2, 11]))           # Output: 2
    print(remove_duplicates([1, 2, 3, 11, 11]))       # Output: 4
