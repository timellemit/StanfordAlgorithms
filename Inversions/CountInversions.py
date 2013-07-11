def parse_input(file_adress):
    return [int(line.strip()) for line in open(file_adress, 'r')]

def countSplitInv(left_ar, right_ar):
    newAr = []
    i, j, countInv = 0, 0, 0
    for k in xrange(len(left_ar) + len(right_ar)):
        if i >= len(left_ar):
            newAr[k:] = right_ar[j:]
            return newAr, countInv     
        if j >= len(right_ar):
            newAr[k:] = left_ar[i:]
            return newAr, countInv
        if left_ar[i] < right_ar[j]:
            newAr.append(left_ar[i])
            i += 1
        else:
            newAr.append(right_ar[j])
            j += 1
            countInv += len(left_ar) - i
    return newAr, countInv

def CountInv(array):
    length = len(array)
    if length == 1:
        return array,0
    elif length == 2:
        return [array, 0] if array[0] < array[1] else [array[::-1], 1]
    else:
        left, right = array[: length / 2], array[length / 2 :]
        leftSorted, leftInvCount = CountInv(left)
        rightSorted, rightInvCount = CountInv(right)
        newArray, countInv = countSplitInv(leftSorted, rightSorted)
        return newArray, leftInvCount + countInv + rightInvCount
     
def brutalInvCount(array): # for debugging
    count = 0
    for i in xrange(len(array)):
        for j in xrange(i,len(array)):
            if array[i] > array[j]:
                count += 1
    return count

def brutalSplitCount(left_ar, right_ar): # for debugging
    count = 0
    for i in left_ar:
        for j in right_ar:
            if i > j:
                count += 1
    return count   
      
print CountInv(parse_input('IntegerArray.txt'))[1]