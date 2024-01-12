# def ficonacci_of(n):
#      if n in {0,1}:
#          return n
#      else:
#          return ficonacci_of(n-1) + ficonacci_of(n-2)

# n = 9 
# print(ficonacci_of(n))


# #fibonacci sequence

def fibonacci(n):
    sequence = [0,1]

    while len(sequence) < n :
        next_item = sequence[-1] + sequence[-2]
        sequence.append(next_item)

    return sequence

# Example usage:
num_terms = int(input("Enter the number of Fibonacci terms to calculate: "))

fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence:")
print(fib_sequence)