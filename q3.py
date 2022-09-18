def median2arr(m,n):
    small = m
    big = n
    if len(m)>len(n):
        small =n
        big = m
    sbig = len(big)
    ssmall = len(small)
    start = 0
    end = ssmall
    realmidinmergedarray = (ssmall + sbig + 1) // 2

    while (start <= end):
        mid = (start + end) // 2
        leftAsize = mid
        leftBsize = realmidinmergedarray - mid
         
        # checking overflow of indices
        leftA = small[leftAsize - 1] if (leftAsize > 0) else float('-inf')
        leftB = big[leftBsize - 1] if (leftBsize > 0) else float('-inf')
        rightA = small[leftAsize] if (leftAsize < ssmall) else float('inf')
        rightB = big[leftBsize] if (leftBsize < sbig) else float('inf')

        # if correct partition is done
        if leftA <= rightB and leftB <= rightA:
            if ((sbig + ssmall) % 2 == 0):
                return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
            return max(leftA, leftB)

        elif (leftA > rightB):
            end = mid - 1
        else:
            start = mid + 1
a= [1,4,5,9,12]
b= [4,5,7,9]
arr = a+b
print(arr)
arr.sort()
print(arr)

print(median2arr(a,b))
            
    
         

    



