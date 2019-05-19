def selection_sort(a):
    for i in range(len(a)):
        min=i
        for j in range (i+1,len(a)):
            if a[min]>a[j]:
                min = j
        a[i],a[min]=a[min],a[i]
    return a
print(selection_sort([5,4,3,9,1]))
