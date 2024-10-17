def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

user_input=input("Enter a list of number :")
arr = list(map(int,user_input.split()))

target=int(input("Enter a Number:"))

result = linear_search(arr, target)
print(f'Target found at index: {result}' if result != -1 else 'Target not found')
