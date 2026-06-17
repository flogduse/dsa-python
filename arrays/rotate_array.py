def rotate_left(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]

def rotate_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original:", arr)
    print("Left rotate by 2:", rotate_left(arr, 2))
    print("Right rotate by 2:", rotate_right(arr, 2))
