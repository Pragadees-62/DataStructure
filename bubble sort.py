def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

user_input=input("Enter a List In Numbers:")
arr = list(map(int,user_input.split()))

bubble_sort(arr)
print("Sorted array:", arr)






