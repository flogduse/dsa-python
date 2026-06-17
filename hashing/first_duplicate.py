def first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None

if __name__ == "__main__":
    arr = [2, 5, 1, 2, 3, 5, 1, 2, 4]
    print(f"Array: {arr}")
    print(f"First duplicate: {first_duplicate(arr)}")
