from time import time
def parse_input(file_adress):
    return [int(line.strip()) for line in open(file_adress, 'r')]

def merge(left_ar, right_ar):
    newAr = []
    i, j = 0, 0
    for k in xrange(len(left_ar) + len(right_ar)):
        if i >= len(left_ar):
            newAr[k:] = right_ar[j:]
            return newAr     
        if j >= len(right_ar):
            newAr[k:] = left_ar[i:]
            return newAr
        if left_ar[i] < right_ar[j]:
            newAr.append(left_ar[i])
            i += 1
        else:
            newAr.append(right_ar[j])
            j += 1
    return newAr

def mergeSort(array):
    length = len(array)
    if length == 1:
        return array
    elif length == 2:
        return array if array[0] < array[1] else array[::-1]
    else:
        left, right = array[: length / 2], array[length / 2 :]
        leftSorted = mergeSort(left)
        rightSorted = mergeSort(right)
        newArray = merge(leftSorted, rightSorted)
        return newArray

init_time = time()    
mergeSort(parse_input('IntegerArray.txt'))
print 'time:', round((time() - init_time),2)
init_time = time()    
parse_input('IntegerArray.txt').sort()
print 'time:', round((time() - init_time),2)