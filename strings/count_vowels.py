def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)

def count_consonants(s):
    return sum(1 for ch in s if ch.isalpha() and ch.lower() not in "aeiou")

if __name__ == "__main__":
    s = "Hello World! Python is fun."
    print(f"String: '{s}'")
    print(f"Vowels: {count_vowels(s)}")
    print(f"Consonants: {count_consonants(s)}")
