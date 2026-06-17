def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70]
    target = 40
    print(f"Array: {arr}")
    print(f"Binary search for {target} (recursive): index {binary_search_recursive(arr, target, 0, len(arr) - 1)}")
    print(f"Binary search for {target} (iterative): index {binary_search_iterative(arr, target)}")
