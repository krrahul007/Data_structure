
# coding: utf-8

# In[11]:


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                arr[k] = R[j]
                k += 1
                j += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1
            
        
        
        
arr = [50, 20, 40, 90, 88, 11, 13]
mergesort(arr)
print(arr)
    

