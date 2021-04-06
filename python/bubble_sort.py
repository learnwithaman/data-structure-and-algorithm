# Bubble Sort  

# O(n^2) time | O(1) space
def bubbleSort(array):
    i = 0;
    j = 1;
    
    counter = 1;
    
    isSwapping = True;
    
    while isSwapping:
        if counter == len(array):
            isSwapping = False
            
        if i == len(array) - counter:
            i = 0
            j = 1
            counter += 1
        
        if array[i] <= array[j]:
            i += 1 
            j += 1 
        else:
            swap(i, j, array)
            i += 1 
            j += 1
    
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i] 
    
print(bubbleSort([8, 12, 9, 10, 4, -1, 0, 6]));