from code import Fraction


def main():
    spacing = 44
    print("Creating fractions: (1,2), (-1,4), (0,2), (4,1), (2,4), and (1, -8)")
    frac1 = Fraction(1, 2)
    frac2 = Fraction(-1, 4)
    frac3 = Fraction(0, 2)
    frac4 = Fraction(4, 1)
    frac5 = Fraction(2, 4)
    frac6 = Fraction(1, -8)
    # print(frac1)
    # print(frac2)
    # print(frac3)
    # print(frac4)
    # print(frac5)
    # print(frac6)
    print("\n __str__ and getter methods:")
    print(f"{'Fraction 1 should read 1/2':{spacing}} {frac1}")
    print(f"{'Fraction 1 should read -1/4':{spacing}} {frac2}")
    print(f"{'Fraction 1 should read 0':{spacing}} {frac3}")
    print(f"{'Fraction 1 should read 4':{spacing}} {frac4}")
    print(f"{'Fraction 1 should read 1/2':{spacing}} {frac5}")
    print(f"{'Fraction 1 should read -1/8':{spacing}} {frac6}")

    print("\nSetting fraction 2's numerator to 2 and denominator to 8")
    frac2.set_numerator(2)
    frac2.set_denominator(8)
    print(f"{'the num of it should be 2':{spacing}} {frac2.get_numerator()}")
    print(f"{'the num of it should be 8':{spacing}} {frac2.get_denominator()}")

    print("\nException handling tests:")
    passed = False
    try:
        print("create frac with dem of 0")
        Fraction(10, 0)
    except ValueError:
        passed = True
        print("\tZero dem test pass")
        if not passed:
            print("\tTest failed")
    passed = False

    try:
        print("\nCreate frac with str in num")
        Fraction("10", 1)
    except TypeError:
        passed = True
        print("\tZero dem test pass")
    if not passed:
        print("\tTest failed")
    passed = False

    try:
        print("\nCreate frac with str in num")
        frac6.set_denominator(0)
    except ValueError:
        passed = True
        print("\tZero dem test pass")
    if not passed:
        print("\tTest failed")
    passed = False

    try:
        print("\nCreate frac with str in num")
        frac6.set_numerator("10")
    except TypeError:
        passed = True
        print("\tZero dem test pass")
    if not passed:
        print("\tTest failed")
    passed = False

    try:
        print("\nCreate frac with str in num")
        frac6.set_denominator("10")
    except TypeError:
        passed = True
        print("\tZero dem test pass")
    if not passed:
        print("\tTest failed")

    print("\nMath methods:")
    print(f"{frac1} + {frac2} should be {frac1 + frac2}")
    print(f"{frac1} + {frac6} should be {frac1 + frac6}")
    print(f"{frac6} + {frac1} should be {frac6 + frac1}")
    print(f"{frac1} - {frac2} should be {frac1 - frac2}")
    print(f"{frac1} - {frac6} should be {frac1 - frac6}")
    print(f"{frac6} - {frac1} should be {frac6 - frac1}")
    print(f"{frac1} * {frac2} should be {frac1 * frac2}")
    print(f"{frac1} * {frac6} should be {frac1 * frac6}")
    print(f"{frac6} * {frac1} should be {frac6 * frac1}")
    print(f"{frac1} / {frac2} should be {frac1 / frac2}")
    print(f"{frac1} / {frac6} should be {frac1 / frac6}")
    print(f"{frac6} / {frac1} should be {frac6 / frac1}")


if __name__ == '__main__':
    main()
