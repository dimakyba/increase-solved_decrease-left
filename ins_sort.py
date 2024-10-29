def insertion_sort(arr):
    moves = 0
    insertions = 0

    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        if current_value < arr[j]:
            insertions += 1

        while j >= 0 and current_value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            moves += 1

        arr[j + 1] = current_value

        print(f"Iteration {i}: {arr}")

    return arr, moves, insertions

# arr = [22, 66, 2, 6, 8, 55, 88, 77, 33, 44, 4, 99, 11, 0]
arr = [44, 77, 6, 0, 33, 66, 8, 88, 99, 11, 4, 22, 2, 55]
sorted_arr, total_moves, total_insertions = insertion_sort(arr)
print(f"Sorted array: {sorted_arr}")
print(f"Total moves: {total_moves}")
print(f"Total insertions: {total_insertions}")
