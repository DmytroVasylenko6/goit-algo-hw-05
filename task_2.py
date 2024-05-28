def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    counter = 0

    while left <= right:
        mid = left + (right - left) // 2
        counter += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return counter, arr[mid]

    if left < len(arr):
        upper_bound = arr[left]
    else:
        upper_bound = None

    return counter, upper_bound


sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
target_value = 1.1

iterations, upper_bound = binary_search(sorted_array, target_value)

print(f"Number of iterations: {iterations}")
print(f"Upper limit: {upper_bound}")
