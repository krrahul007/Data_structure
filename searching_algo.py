
# coding: utf-8

# Linear search

# In[1]:


def LinearSearch(arr, n, x):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

arr = [89, 56, 87, 51, 46, 25, 52, 44, 10, 32]
n = len(arr)
x= int(input("Enter the number: "))
out = LinearSearch(arr,n,x)
print(out)


# Binary search

# In[7]:


#Def BinarySearch(arr,low,high,x):
def BinarySearch(arr,low,high,x):
    if low==high:
        return arr[low]
    else:
        mid = low + (high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return BinarySearch(arr,low,mid-1,x)
        else:
            return BinarySearch(arr,mid+1,high,x)
    return -1

arr = [89, 56, 87, 51, 46, 25, 52, 44, 10, 32]
n = len(arr)
low = 0
high = n
x= int(input("Enter the number: "))
out = BinarySearch(arr,low,high,x)
print(out)

