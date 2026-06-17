def two_sum_brute(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

def two_sum_hash(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    print(f"Array: {arr}, Target: {target}")
    print("Two sum (brute):", two_sum_brute(arr, target))
    print("Two sum (hash):", two_sum_hash(arr, target))
