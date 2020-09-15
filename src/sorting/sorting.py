# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = arrA.extend(arrB)
    
    merge_sort(merged_arr)
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # find the midpoint 
        left = arr[:mid] # divide the elements into 2 halves
        right = arr[mid:]
        
        merge_sort(left) #sort the first half
        merge_sort(right) #sort the second half
        
        #two iterators for transversing the two halves
        i = 0
        j = 0
        
        #iterartor for the main list
        k = 0
        
        #copy data temp arrays left and right 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                #the value from the left has been used
                arr[k] = left[i]
                #move the iterator foreward
                i += 1
            else:
                # else use the value from the right
                arr[k] = right[j]
                j += 1
            #move to the next spot 
            k += 1
            
            #checking if any element was left
        while i < len(left): 
            arr[k] = left[i] 
            i+= 1
            k+= 1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+= 1
            k+= 1
  
            
    return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input

# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

