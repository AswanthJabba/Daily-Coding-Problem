'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
def arrproduct(arr):
    product=[0]*len(arr)
    l=[0]*len(arr)
    r=[0]*len(arr)
    l[0]=1
    r[len(arr)-1]=1
    for i in range(1,len(arr)):
        l[i]=arr[i-1]*l[i-1]
    for i in range(len(arr)-2,-1,-1):
        r[i]=arr[i+1]*r[i+1]
    for i in range(len(arr)):
        product[i]=l[i]*r[i]
    return product
    
if __name__=='__main__':
    arr=[1, 2, 3, 4, 5]
    print(arrproduct(arr))
