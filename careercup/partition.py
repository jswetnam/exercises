# http://www.careercup.com/question?id=21037663

# Given an array of numbers, arrange it such that all the numbers less
# than a given key should come before the key and all the numbers greater
# than the key should come after it.
# For example: arr = { 0, -1, -2, 2, 0, 3, 5}, given key = 0
# answer should be {-1, -2, 0, 0, 2, 3, 5}
# Order of elements that are smaller or greater than key does not matter i.e. sorting
# is not expected. So, {-1,-2, 0, 0, 5, 2, 3} is also a correct answer.

# Time complexity should not be more than O(n).

def partition(A, pivot):
    j = -1
    for i in range(len(A)):
        if A[i] <= pivot:
            j += 1
            A[i], A[j] = A[j], A[i]
