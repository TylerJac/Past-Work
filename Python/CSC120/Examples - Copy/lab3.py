def print_numbers(n):
    """
    Recursively prints numbers from 1 to n.
    
    Params: n (int): The upper limit of the numbers to be printed.
    """
    if n > 0:
        # Recursively call print_numbers with n-1 until n becomes 0
        print_numbers(n - 1)
        # Print the current number
        print(n)

def multiply(x, y):
    """
    Recursively calculates the product of x and y using repeated addition.
    
    Params:  x (int): The first number.  y (int): The second number.
        
    Returns: The product of x and y.
    """
    if y == 1:
        return x
    else:
        # Recursively add x y times
        return x + multiply(x, y - 1)

def asterisks(n):
    """
    Recursively displays lines of asterisks.
    
    Params: The number of lines of asterisks to be displayed.
    """
    if n > 0:
        # Recursively call asterisks with n-1 until n becomes 0
        asterisks(n - 1)
        # Print n asterisks
        print('*' * n)

def find_largest(num):
    """
    Recursively finds the largest value in a list.
    
    Params: The list of numbers.
        
    Returns: The largest value in the list.
    """
    if len(num) == 1:
        return num[0]
    else:
        # Recursively find the largest value in the rest of the list
        max_rest = find_largest(num[1:])
        # Compare the first element with the max of the rest
        return num[0] if num[0] > max_rest else max_rest

def recursive_sum(num):
    """
    Recursively calculates the sum of all numbers in a list.
    
    Args: The list of numbers.
        
    Returns:  int: The sum of all numbers in the list.
    """
    if len(num) == 1:
        return num[0]
    else:
        # Recursively sum the first element with the sum of the rest
        return num[0] + recursive_sum(num[1:])

def sum_integers(n):
    """
    Recursively calculates the sum of integers from 1 to n.
    
    Params: n (int): The upper limit of the range of integers.
        
    Returns: int: The sum of integers from 1 to n.
    """
    if n == 1:
        return 1
    else:
        # Recursively add n with the sum of integers from 1 to n-1
        return n + sum_integers(n - 1)

def power(base, exponent):
    """
    Recursively raises a number to a power.
    
    Param: base (int): The base number.  exponent (int): The exponent.
        
    Returns: int: The result of raising the base to the exponent.
    """
    if exponent == 0:
        return 1
    else:
        # Recursively multiply base with itself exponent times
        return base * power(base, exponent - 1)

def main():
    """
    The main function to demonstrate the usage of the implemented recursive functions.
    """
    print_numbers(5)
    print(multiply(5, 5))
    asterisks(10)
    print(find_largest([4, 8, 6, 35, 21]))
    print(recursive_sum([6, 8, 9, 10, 15]))
    print(sum_integers(55))
    print(power(2, 18))

main()
