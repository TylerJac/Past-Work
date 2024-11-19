# ===============================================================

# Name: Tyler Jackson

# Date: 2/26/2024

# Course: CSC 120 NLE01

# Algorithm: n/a

# References: in class

# ===============================================================

def problem_one(n):
    """
    Recursively prints numbers from 1 to n.

    Params: n: The upper limit of the numbers to be printed.
    """
    if n > 0:
        # Recursively call print_numbers with n-1 until n becomes 0
        problem_one(n - 1)
        # Print the current number
        print(n)


def problem_two(x, y):
    """
    Recursively calculates the product of x and y using repeated addition.

    Params:  x: The first number.  y: The second number.

    Returns: The product of x and y.
    """
    if y == 1:
        return x
    else:
        # Recursively add x y times
        return x + problem_two(x, y - 1)


def problem_three(n):
    """
    Recursively displays lines of asterisks.

    Params: The number of lines of asterisks to be displayed.
    """
    if n > 0:
        # Recursively call asterisks with n-1 until n becomes 0
        problem_three(n - 1)
        # Print n asterisks
        print('*' * n)


def problem_four(num):
    """
    Recursively finds the largest value in a list.

    Params: The list of numbers.

    Returns: The largest value in the list.
    """
    if len(num) == 1:
        return num[0]
    else:
        # Recursively find the largest value in the rest of the list
        max_num = problem_four(num[1:])
        # Compare the first element with the max of the rest
        return num[0] if num[0] > max_num else max_num


def problem_five(num):
    """
    Recursively calculates the sum of all numbers in a list.

    Params: The list of numbers.

    Returns: The sum of all numbers in the list.
    """
    if len(num) == 1:
        return num[0]
    else:
        # Recursively sum the first element with the sum of the rest
        return num[0] + problem_five(num[1:])


def problem_six(n):
    """
    Recursively calculates the sum of integers from 1 to n.

    Params: n : The upper limit of the range of integers.

    Returns: The sum of integers from 1 to n.
    """
    if n == 1:
        return 1
    else:
        # Recursively add n with the sum of integers from 1 to n-1
        return n + problem_six(n - 1)


def problem_seven(base, exponent):
    """
    Recursively raises a number to a power.

    Params: base : The base number.  exponent : The exponent.

    Returns: The result of raising the base to the exponent.
    """
    if exponent == 0:
        return 1
    else:
        # Recursively multiply base with itself exponent times
        return base * problem_seven(base, exponent - 1)


def main():
    """
    The main function to demonstrate the usage of the implemented recursive functions.
    """
    problem_one(5)
    print(problem_two(5, 5))
    problem_three(10)
    print(problem_four([4, 8, 6, 35, 21]))
    print(problem_five([6, 8, 9, 10, 15]))
    print(problem_six(55))
    print(problem_seven(2, 18))


if __name__ == "__main__":
    main()
