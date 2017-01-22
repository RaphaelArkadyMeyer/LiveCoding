from sys import stdin


def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
@@ begin question base case
@@ description: Find the base case
@@ points: 100

@@ end question
    else:
        pivot = arr[0]
@@ begin question recursion
@@ points: 500







@@ end question
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

