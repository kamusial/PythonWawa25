"""
Fibonacci program
"""

def fibonacci(n: int) -> int:
    """n must be positive.
    NOTE: if result > 4300 digits, the result cannot be printed.
    """
    if n < 0:
        raise ValueError("Fibonacci sequence only supports positive numbers.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
