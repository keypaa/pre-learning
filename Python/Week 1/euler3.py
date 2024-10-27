def fibonacci(n):
    if n <= 1:
        return(n)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(33))

def fibonacci_even_sum(limit):
    a, b = 0, 1
    even_sum = 0
    while b <= limit:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    return even_sum

limit = 4000000
result = fibonacci_even_sum(limit)
print(result)