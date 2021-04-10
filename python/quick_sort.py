# Quick Sort
# Avg: O(nlog(n)) time | O(log(n)) space
def quick_sort(array):
    array_length = len(array)
    if array_length <= 1:
        return array
    # Select the first element as pivot.
    quick_sort_helper(array, 0, 1, array_length - 1)
    return array


def quick_sort_helper(array, pivot_index, left_bound_index, right_bound_index):
    if right_bound_index > pivot_index:
        sorted_num_index = sort_elements(array, pivot_index, left_bound_index, right_bound_index)
        quick_sort_helper(array, pivot_index, left_bound_index, sorted_num_index - 1)
        quick_sort_helper(array, sorted_num_index + 1, sorted_num_index + 2, right_bound_index)


def sort_elements(array, pivot_index, left_bound_index, right_bound_index):
    while left_bound_index <= right_bound_index:
        if array[left_bound_index] > array[pivot_index] > array[right_bound_index]:
            swap(left_bound_index, right_bound_index, array)
        if array[left_bound_index] <= array[pivot_index]:
            left_bound_index += 1
        if array[right_bound_index] >= array[pivot_index]:
            right_bound_index -= 1

    if array[right_bound_index] < array[pivot_index]:
        swap(pivot_index, right_bound_index, array)

    return right_bound_index


def swap(large_num_index, small_num_index, array):
    array[large_num_index], array[small_num_index] = array[small_num_index], array[large_num_index]


numbers_array = [1, 0, 12, 7, 0, 8, -1, 10, 21, 13, 14]

print("Output: ", quick_sort(numbers_array))
