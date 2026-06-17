def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

def is_anagram_count(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    if len(s1) != len(s2):
        return False
    from collections import Counter
    return Counter(s1) == Counter(s2)

if __name__ == "__main__":
    pairs = [("listen", "silent"), ("hello", "world"), ("debit card", "bad credit")]
    for s1, s2 in pairs:
        print(f"'{s1}' vs '{s2}': {is_anagram(s1, s2)}")
