# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    # Indexes to keep track of next elements to compare in respective input arrays
    a_index = 0
    b_index = 0

    # Index to keep track of the next place in the merged output array
    merged_index = 0

    # While the current index of each respective array is less than it's length
    # compare to figure out which one is smaller and add that to the merged array first
    # then increment the index on each input array and the output array

    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            merged_arr[merged_index] = arrA[a_index]
            a_index += 1
            merged_index += 1
        else:
            merged_arr[merged_index] = arrB[b_index]
            b_index += 1
            merged_index += 1

    # If there are any remaining items in the left or right arrays, first add the left then the right items
    while a_index < len(arrA):
        merged_arr[merged_index] = arrA[a_index]
        a_index += 1
        merged_index += 1
    while b_index < len(arrB):
        merged_arr[merged_index] = arrB[b_index]
        b_index += 1
        merged_index += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

    # If the array is less than or equal to one in length then it has reached the recursive base case and can't be split any further

    if len(arr) <= 1:
        return arr

    # The middle point helps us split the array into two
    middle = int(len(arr)//2)

    # Call the split on the left half and the right half, which will return single item arrays if at the bottom of the recursive tree
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    # The two arrays are then compared, and merged in proper order going back up the recursion tree
    return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
