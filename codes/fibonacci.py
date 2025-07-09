def fibonacci(n):
    suite = [0, 1]
    for i in range(2, n):
        suite.append(suite[-1] + suite[-2])
    return suite[:n]


# Exemple d'utilisation
n = 10
print(f"Les {n} premiers termes de la suite de Fibonacci :", fibonacci(n))
