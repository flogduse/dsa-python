def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    target = 70
    idx = linear_search(arr, target)
    print(f"Array: {arr}")
    print(f"Search for {target}: found at index {idx}" if idx != -1 else f"Search for {target}: not found")
