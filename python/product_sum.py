# O(n) time | O(d) space
def product_sum(array, multiplier=1):
    total_sum = 0
    for element in array:
        if type(element) is list:
            total_sum += product_sum(element, multiplier + 1)
        else:
            total_sum += element
    return total_sum * multiplier


print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
