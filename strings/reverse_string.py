def reverse_string(s):
    return s[::-1]

def reverse_string_loop(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

def reverse_words(s):
    return " ".join(s.split()[::-1])

if __name__ == "__main__":
    s = "hello world"
    print(f"Original: '{s}'")
    print(f"Reversed: '{reverse_string(s)}'")
    print(f"Reversed words: '{reverse_words(s)}'")
