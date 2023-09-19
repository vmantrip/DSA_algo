# Maximum subarray problem to determine maximum stock price

import random
import math
randomlist = []
for i in range(0,10):#Constraint: Input array has only 5 elements
    n = random.randint(-10,10)
    randomlist.append(n)
print(f'Input array is {randomlist}')
def max_cross_sub(a,low,mid,high):
    left_sum=-1*(math.inf)
    sum=0
    for i in range(mid,low-1,-1):
        sum=sum+a[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i
    right_sum=-1*(math.inf)
    sum=0
    for j in range(mid+1, high+1):
        sum+=a[j]
        if sum>right_sum:
            right_sum=sum
            max_right=j
    return (max_left, max_right, left_sum+right_sum)
def max_sub(a, low, high):
    if high==low:
        return (low, high, a[low])
    else:
        mid=(low+high)//2
        (left_low, left_high, left_sum)=max_sub(a, low, mid)
        (right_low, right_high, right_sum)=max_sub(a, mid+1, high+1)
        (cross_low, cross_high, cross_sum)=max_cross_sub(a,low, mid+1, high+1)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low,cross_high, cross_sum)
print(max_sub(randomlist,0,len(randomlist)))



