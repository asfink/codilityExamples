# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    postSum = 0
    preSum = 0
    for n in A:
        postSum+=n
    arr = list()
    for i in range(len(A)):
        postSum -=A[i]
        preSum +=A[i]
        diff = abs(preSum-postSum)
        arr.append(diff)
    minVal = min(arr)
    return minVal
