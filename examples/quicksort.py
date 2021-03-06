from sys import stdin

@@ begin hide
def main():
    print("start qs", stdin.readline())  # Ignore first line with number of inputs on it
    array_in = stdin.readline()
    print(array_in)
    presort = list(map(int, array_in.split(' ')))
    sort = quickSort(presort)
    print(sort)
@@ end hide

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
@@ begin question base case
@@ description: Find the base case
@@ points: 100
        return arr
@@ end question
    else:
        pivot = arr[0]
@@ begin question recursion
@@ points: 500
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
@@ end question
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

@@ begin hide
if __name__ == '__main__':
    main()
@@ end hide
