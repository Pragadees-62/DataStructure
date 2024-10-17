def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


user_input=input("Enter a list of number :")
arr = list(map(int,user_input.split()))

target=int(input("Enter a Number:"))

result = binary_search(arr, target)
print(f'Target found at index: {result}' if result != -1 else 'Target not found')
