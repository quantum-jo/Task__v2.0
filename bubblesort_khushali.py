def bubbleSort(arr,n): 
   for i in range(n): 
        swapped = False
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
        if swapped == False: 
            break
           

n = input("Enter the length of list:")
arr=[x for x in range(n)]
for i in range(0,n):
    arr[i]=input("Enter the element:")
bubbleSort(arr,n) 
   
print ("Sorted array :") 
for i in range(n): 
    print ( arr[i]) ,
  
