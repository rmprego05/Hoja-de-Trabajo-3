def bubble_sort(arr):


    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1): #termino hasta el penultimo indice para comparar con el de la derecha
            if arr[j] > arr[j+1]:
                #swap python: a, b = b, a
                arr[j], arr[j+1] = arr[j+1] , arr[j]
    
    return arr


unsorted_list = [-2,6,4,67,13]
print("Lista deordenada: " , unsorted_list)

sorted_list = bubble_sort(unsorted_list)
print("Lista ordenada: " , sorted_list)

