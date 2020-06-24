sample = [6,5,4,3,2,10]
def bubble_sort(list):
    """this moves through the list, if a value is more than the value after it, they swap places"""
    sorting = True
    
    while sorting:
        sorting = False
        for i in range(len(list)-1):
            
            if list[i]>list[i+1]:
                
                list[i], list[i+1] = list[i+1], list[i]
                sorting = True
            
    return list


def selection_sort(list):
    """This creates two lists, sorted and unsorted. In practice, you treat the leftomost section as the sorted list"""
    for i in range(len(list)):

        min_index = i # Assume the first value is the smallest

        for j in range(i+1, len(list)): # go through the unsorted part of the list
            
            if list[min_index] > list[j]: # if the smallest value isn't the smallest value in the list:
                min_index = j # Identify the next smallest value in the list
        
        list[i], list[min_index] = list[min_index], list[i] # swap the smallest value with 

    return list


def insertion_sort(list):
    """First assume the first value in the list i ssorted, then take the second value(x), and move through the list until you find where x fits"""
    print("kaesih")


def counting_sort(list):
    """"""
