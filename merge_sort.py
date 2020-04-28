"""
Practice for implementing the merge sort algorithm in Python:
Merge Sort recursively sorts two parts of a list and merges them together 

Jason Zhang April 2020
"""


def Merge(top: list, bottom: list):
    """
    Helper function that merges the top and bottom arrays together
    (your mistake was assuming it was going to be adding the arrays together)
    Args:
        top: top half of list being merged
        bottom: bottom half of list being merged
    Returns: 
        the merged list in python 
    """
    i = 0 # pointer for first array
    j = 0 # pointer for second array
    merged = []
    # while none of the array's have run out 
    while i < len(top) and j < len(bottom):
        if top[i] < bottom[j]:
            merged.append(top[i])
            i += 1
        else:
            merged.append(bottom[j])
            j += 1
    # check if any elements are left from top and bottom arrays
    if i < len(top):
        merged = merged + top[i:]
    if j < len(bottom):
        merged = merged + bottom[j:]
    
    return merged


def MergeSort(A: list):
    """ Recursive merge sort algorithm to sort an array
    Args:
        A: a list that needs to be sorted
    Returns:
        the sorted list (python passes by reference nicely though)
    """
    
    n = len(A)
    # base case
    if n <= 1:
        return A
    # recursively sort the two halves of A (cool thing to note is that python slicing A[x:] means A[x+1,...,n])
    half = n//2
    top = MergeSort(A[:half])
    bottom = MergeSort(A[half:])
    # returned the merged list of the two sorted halves 
    return Merge(top, bottom)

if __name__ == "__main__":
    # array to be sorted
    A = [5,2,3,1,6,4,7,9,8,10]
    # print the nicely sorted result 
    print(MergeSort(A))
    