from collections import Counter

def frequency_count(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print("Array:", arr)
    freq = frequency_count(arr)
    print("Frequency:", freq)
    print("Most common:", Counter(arr).most_common(2))
