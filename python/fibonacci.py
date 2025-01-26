def fibonacci(n):
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
    return fib[:n]

# Input: number of terms
n = int(input("Enter the number of Fibonacci terms: "))

# Output: Fibonacci sequence
print("Fibonacci Sequence:", fibonacci(n))
