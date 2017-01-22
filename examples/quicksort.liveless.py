from sys import stdin

def main():
    print("start qs", stdin.readline())  # Ignore first line with number of inputs on it
    array_in = stdin.readline()
    print(array_in)
    presort = list(map(int, array_in.split(' ')))
    sort = quickSort(presort)
    print(sort)

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

if __name__ == '__main__':
    main()
