
# coding: utf-8
PROBLEM TARGET
# In[9]:


max= 10000000000
def SumDigit(arr,n,target):
    p1,p2=0, 0 
    low, high, diff=0, n-1, max
    
    while high > low:
        if abs(arr[low] + arr[high] - target) < diff:
            p1 = low
            p2 = high
            diff = abs(arr[low] + arr[high] - target)
        
        if (arr[low] + arr[high]) > target:
            high = high - 1
        else:
            low = low + 1
    print('the pair is {} and {}'.format(arr[p1],arr[p2]))

arr = [10,22,28,29,30,40]
target = 54
n = len(arr)
SumDigit(arr,n,target)

