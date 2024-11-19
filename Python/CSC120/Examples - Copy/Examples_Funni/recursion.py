def recursion_depth(times):
    if times > 0:
        print("this is a recursive function that will break")
    recursion_depth(times)


def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n - 1)


def factorial2(n):
    if n > 1:
        return n * factorial2(n - 1)
    return 1


def hanoi(n, source, destination, temp):
    if n == 1:
        print(f"moving disc {n} from peg {source} to peg {destination}")
    else:
        hanoi(n - 1, source, temp, destination)
        print(f"moving disc {n} from peg {source} to peg {destination}")
        hanoi(n - 1, temp, destination, source)


def move_discs(n, source, destination, temp):
    if n > 0:
        move_discs(n - 1, source, temp, destination)
        print(f"moving disc {n} from peg {source} to peg {destination}")
        move_discs(n - 1, temp, destination, source)


def main():
    # print(factorial2(6))
    # recursion_depth(6)
    move_discs(4, 'A', 'B', 'C')
    hanoi(4, 'A', 'B', 'C')


if __name__ == '__main__':
    main()
