def is_balanced(expr):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in expr:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    tests = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for t in tests:
        print(f"{t}: {is_balanced(t)}")
