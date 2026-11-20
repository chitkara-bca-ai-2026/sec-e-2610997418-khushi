def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def box(title):
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

box("MATHEMATICS LEARNING TOOL")

while True:
    print("Select an operation:\n1. Calculate Factorial\n2. Generate Fibonacci Series\n3. Exit")
    choice = int(input("Enter choice (1-3): "))
    if choice == 3:
        break
    if choice == 1:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print('That is not a positive integer.')
        else:
            print(f'[RESULT] Factorial of {n} ({n}!) = {factorial(n)}\n')
    if choice == 2:
        n_terms = int(input("Enter the number of terms: "))

        numbers = ", ".join(str(fibonacci(i)) for i in range(n_terms))
        print(f"[RESULT] Fibonacci series ({n_terms} terms): [{numbers}]\n")