# Selection Sort

# O(n^2) time | O(1) space
def selection_sort(array):
    current_index = 0
    while current_index < len(array):
        small_num_index = current_index
        for potential_match_index in range(current_index + 1, len(array)):
            if array[potential_match_index] < array[small_num_index]:
                small_num_index = potential_match_index
        swap(current_index, small_num_index, array)
        current_index += 1
    return array


def swap(large_num_index, small_num_index, array):
    array[large_num_index], array[small_num_index] = array[small_num_index], array[large_num_index]


print(selection_sort([4, 8, -1, 0, 2, 6, 3]))