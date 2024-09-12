
def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        next_value = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_value)
    return fib_seq


def is_in_fibonacci(n):
    fib_seq = fibonacci_sequence(n)
    if n in fib_seq:
        return f"O número {n} pertence a sequencia de Fibonacci."
    else:
        return f"O número {n} NÃO pertence a sequencia de Fibonacci."


number = int(input("Informe o número para verificar se pertence a sequencia de Fibonacci: "))


print(is_in_fibonacci(number))
