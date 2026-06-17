def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    for n in range(1, 11):
        print(f"factorial({n}) = {factorial(n)}")
