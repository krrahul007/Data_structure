
# coding: utf-8

# In[32]:


def Quicksort(a,low,high):
    if low == high:
        return a
    if low < high:
        m = partition(a, low, high)
        Quicksort(a, low, m-1)
        Quicksort(a, m+1, high)
    return a

def partition(a, low, high):
    x = a[low]
    i = low
    for j in range(low+1,high):
        if a[j] <= x :
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i], a[low] = a[low], a[i]
    return i + 1

def prints(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()
    
a= [50, 80, 27, 20, 9, 30,3, 444,2, 1000, 40, 88, 27, 69, 19]
print("Array before sorting" )
prints(a)

Quicksort(a, 0, len(a))
print("Array afer sorting" )
prints(a)
            
        
    

