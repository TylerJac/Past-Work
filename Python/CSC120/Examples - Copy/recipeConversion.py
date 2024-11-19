# ============================================================
# PROGRAMMER:..... Tyler Jackson
# COURSE:......... CSC 120
# TERM:........... Spring 2024
# PROJECT:........ Recipe Conversion Program
# FILENAME:....... recipeConversion.py, fraction.py
# ============================================================
from fraction import *


def get_file():
    """
    Gets filename from user and attempts to open file up to three times.
    If the file exceeds three attempts of opening successfully,
    an IO exception is raised
    :return: Tuple of the filename entered by the user and the open file object
    """
   # Initialize attempts counter
    attempts = 0
    
    # Try to open the file up to three times
    while attempts < 3:
        try:
            # Prompt user to enter filename
            filename = input("Enter the filename: ")
            # Attempt to open the file in read mode
            input_file = open(filename, 'r')
            # Return the filename and the open file object if successful
            return filename, input_file
        except IOError:
            # Print error message if file not found
            print("Error: File not found.")
            # Increment attempts counter
            attempts += 1
    
    # If file cannot be opened after three attempts, raise IOError
    raise IOError("Exceeded maximum attempts to open file.")

# DO NOT CHANGE THE CODE, ONLY COMMENT
def remove_measure(line):
    """
    Returns the given line with any initial digits and fractions (and
    any surrounding blanks) removed
    :param line: str line to be processed
    :return: str line with measurements removed
    """
    # Initialize index to 0
    k = 0
    # Define the blank character
    blank_char = ' '

    # Iterate through the characters in the line
    # Continue until the end of the line or until a non-digit, '/', or blank character is encountered
    while k < len(line) and (line[k].isdigit() or line[k] in ('/', blank_char)):
        # Increment index
        k = k + 1

    # Return the line from the index 'k' onwards, effectively removing any initial digits and fractions along with surrounding blanks
    return line[k:]


# DO NOT CHANGE THE CODE, ONLY COMMENT
def scan_as_fraction(line):
    """
    Scans all digits, including fractions, and returns as a Fraction object
    For example, '1/2' would return as a Fraction value 1/2, '2' would return
    as Fraction 2/1, and '2 1/2' would return as Fraction value 3/2
    :param line: str line to be processed
    :return: Fraction object of the given line's measurement
    """
    # Initialize variables
    completed_scan = False
    value_as_fraction = Fraction(0, 1)

    # Continue scanning until completed
    while not completed_scan:
        k = 0
        # Scan for digits
        while k < len(line) and line[k].isdigit():
            k = k + 1

        # Extract numerator
        numerator = int(line[:k])

        if k < len(line) and line[k] == '/':
            k = k + 1
            start = k
            # Scan for denominator
            while k < len(line) and line[k].isdigit():
                k = k + 1

            denominator = int(line[start:k])
        else:
            denominator = 1

        # Add the scanned fraction to the accumulated value
        value_as_fraction = value_as_fraction + Fraction(numerator, denominator)

        # Check if the end of the line is reached
        if k == len(line):
            completed_scan = True
        else:
            # Continue scanning from the next position
            line = line[k:].strip()

            # Check if the next character is a digit, if not, scanning is completed
            if not line[0].isdigit():
                completed_scan = True

    return value_as_fraction


def convert_line(line, factor):
    """
    If the line begins with a digit, then returns the line with the value
    incremented by factor, otherwise returns line unaltered
    For example, for a factor of 2, '1/4 cup sugar' returns as '1/2 cup sugar'
    and '2 cups sugar' returns as '4 cups sugar'
    :param line: str line to be processed
    :param factor: int | Fraction factor to change line measurement by
    :return: str processed line
    """
    # Check if the line starts with a digit
    if line[0].isdigit():  
        # Convert the line's measurement into a Fraction object
        measurement = scan_as_fraction(line)  
        # Multiply the measurement by the provided factor
        new_measurement = measurement * factor  
        # Remove the original measurement from the line
        new_line = remove_measure(line)  
        # Concatenate the new measurement with the rest of the line
        return str(new_measurement) + new_line 
    else:
        # If the line does not start with a digit, return the original line unchanged
        return line  

# DO NOT CHANGE ANYTHING BELOW THIS LINE!
# You are responsible for writing the 2 empty functions above and
# adding comments to the other two functions
def main():
    # display welcome
    print("This program will convert a given recipe to a different\n"
          "quantity based on a specified conversion factor. Enter a\n"
          "factor of 1/2 to halve, 2 to double, 3 to triple, etc.\n")

    try:
        # get filename and open file
        filename, input_file = get_file()  # you need to write this function

        # get conversion factor
        factor = input("Enter a conversion factor: ")
        factor = scan_as_fraction(factor)

        # open output file named "conv_" + filename
        output_filename = "conv_" + filename
        output_file = open(output_filename, 'w')

        # convert recipe
        empty_str = ''
        line = input_file.readline()  # you are converting the recipe line by line

        while line != empty_str:  # while we haven't reached the end of the file
            new_line = convert_line(line, factor)  # you need to write this function
            output_file.write(new_line)  # write the new line to the output file
            line = input_file.readline()  # get the next line of the original recipe

        # close files
        input_file.close()
        output_file.close()

        # display completion message
        print(f"Converted recipe in file: {output_filename}")

    except IOError as err_mess:  # catch IOError
        print(err_mess)


if __name__ == '__main__':
    main()
