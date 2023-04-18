from math import factorial

n = float(input("Enter the value of n: \n"))
x = int(input("Enter the value of x: \n"))

series = lambda n, x: [n ** i / factorial(i) for i in range(x + 1)]
sum_series = lambda series: sum(series)

result = sum_series(series(n, x))

print("Result is: "f"e^{n} = {result:.3f}")


def sum(n):
    """
    Recursively calculate the sum of series (-1)^(k+1)/k from k = 1 to k = n.
    Global variable 'total'.

    :param n(int): The number of terms to sum
    :return: None
    """
    global total

    if n == 0:
        return
    term = (-1) ** (n + 1) / n
    total += term

    sum(n - 1)


total = 0
sum(6)
print(f"The sum is {total:.4f}")
