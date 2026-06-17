def remove_duplicates_sorted(arr):
    if not arr:
        return 0
    write_idx = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_idx] = arr[i]
            write_idx += 1
    return write_idx

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 4, 4, 5]
    print("Original:", arr)
    k = remove_duplicates_sorted(arr)
    print("After removing duplicates:", arr[:k])
