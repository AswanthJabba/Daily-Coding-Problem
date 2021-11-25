'''
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, r eturn true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''
def twosum(arr,target):
    hashmap={}
    for i in arr:
        if target-i in hashmap:
            return [target-i,i]
        else:
            hashmap[i]=1
    return -1
    
if __name__=='__main__':
	arr=[10,15,3,7]
	print(twosum(arr,17))
