# ===============================================================

# Name: Tyler Jackson

# Date: 2/12/2024

# Course: CSC 120 NLE01

# Algorithm: -

# References: Starting out with Python 5E, W3Schools

# ===============================================================

# Python libraries imported
import random


def problem_1():
    """
    this function asks for a course number and returns you the data
    params: course_room, course_instructor, course_meeting_time
    returns: nothing
    """
    # Dictionary
    course_meeting_time = {
        "CS101": "8:00 a.m.",
        "CS102": "9:00 a.m.",
        "CS103": "10:00 a.m.",
        "NT110": "11:00 a.m.",
        "CM241": "1:00 p.m."
    }
    # Dictionary
    course_instructor = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }
    # Dictionary
    course_room = {
        "CS101": "3004",
        "CS102": "4501",
        "CS103": "6755",
        "NT110": "1244",
        "CM241": "1411"
    }

    print("--------Problem 1: Course Information--------")

    while True:
        course_number = input("Enter a course number (CS101) : ")
        # getting all the information
        room = course_room.get(course_number)
        instructor = course_instructor.get(course_number)
        meeting_time = course_meeting_time.get(course_number)
        # if user inputs correct course number
        if room and instructor and meeting_time:
            # prints all the information
            print(f"Information for {course_number}:")
            print(f"Room number: {room}")
            print(f"Instructor: {instructor}")
            print(f"Meeting time: {meeting_time}")
            break
            # User input an incorrect course number
        else:
            print("Course not listed, please try again.")


def problem_2():
    """
    conducts a U.S. State quiz.
    the functions randomly quizzes the user by displaying the name of a state and asks the user to input its capital

    params: user_input = incorrect or correct
    returns: nothing
    """
    # Dictionary of U.S. states
    states_capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
    }
    # Variables for right and wrong
    correct = 0
    incorrect = 0
    # Asks the user 10 times
    for quest in range(10):
        # randomly select state
        state = random.choice(list(states_capitals.keys()))
        capital = states_capitals[state]
        # Asks for user input
        user_input = input(f"What is the capital of {state}? ").strip()
        # If you're correct
        if user_input.lower() == capital.lower():
            print("Correct")
            correct += 1
        # If you're wrong
        else:
            print(f"The correct capital of {state} is {capital}.")
            incorrect += 1
    # Results of how many you got right and wrong
    print("-------- Results --------")
    print(f"Number of correct: {correct}")
    print(f"Number of incorrect: {incorrect}")


def encrypt_file(filename):
    """
    creates an encrypted file of the data with a given dictionary

    params: codes (dict): A dictionary where keys are characters in the text and values are their respective codes.

    returns: none
    """

    # Dictionary
    code = {
        'W': '?', 'a': '9', 'b': '8', 'c': '7', 'd': '6',
        'e': '5', 'f': '4', 'g': '3', 'h': '2', 'i': '1',
        'j': '0', 'l': '`', 'm': '_', 'n': '.', 'o': ',',
        'p': ' ', 'r': '^', 's': '&', 't': "'", 'v': '!',
        'w': '@', 'y': '#', ' ': '%'
    }
    # name of the output file
    output_filename = "encrypted_" + filename
    # opens Kennedy.txt file
    with open(filename, 'r') as file:
        content = file.read()

        encrypted_content = ''
        for char in content:
            if char in code:
                encrypted_content += code[char]
            else:
                encrypted_content += char
        # creates file with coded message
    with open(output_filename, 'w') as output_file:
        output_file.write(encrypted_content)
    print(f"File '{filename}' has been encrypted and saved as '{output_filename}'.")


def decrypt_file(filename):
    """
    decrypts the file using the given dictionary
    params:codes = A dictionary containing encryption codes as keys and corresponding characters as values.
    returns: none, prints the decrypted contents of the file to the console
    """
    # Dictionary
    code = {
        '?': 'W', '9': 'a', '8': 'b', '7': 'c', '6': 'd',
        '5': 'e', '4': 'f', '3': 'g', '2': 'h', '1': 'i',
        '0': 'j', '`': 'l', '_': 'm', '.': 'n', ',': 'o',
        ' ': 'p', '^': 'r', '&': 's', "'": 't', '!': 'v',
        '@': 'w', '#': 'y', '%': ' '
    }
    # opens encrypted file
    with open(filename, 'r') as file:
        content = file.read()
        # decrypts content in file
        decrypted_content = ''
        for char in content:
            if char in code:
                decrypted_content += code[char]
            else:
                decrypted_content += char
    # prints decrypted content
    print(f"Decrypted contents of file '{filename}':")
    print(decrypted_content)


def problem_4(file_name):
    """
    This function reads the contents of a text file and finds all unique words in the file.

    Params: file_name: The name of the text file to be processed.

    Return: None
    """

    unique_words = set()
    try:
        # opens file
        with open(file_name, "r") as text:
            # finding unique words and adding them
            for line in text:
                words = line.split()
                for word in words:
                    unique_words.add(word.strip())
        print("Unique words found in the file:")
        for word in sorted(unique_words):
            print(word)
    except FileNotFoundError:
        print("File not found.")


def problem_5(file_name):
    """
    Counts the frequency of each word in a text file.
    params: file_name: The name of the text file to analyze.
    return: None
    """
    word_count = {}

    try:
        # opens file
        with open(file_name, 'r') as text:
            # finding each word
            for line in text:
                words = line.split()
                for word in words:
                    # Convert word to lowercase to ensure case-insensitive counting
                    word = word.lower()
                    # counts the words
                    word_count[word] = word_count.get(word, 0) + 1
        # prints the word frequency
        print("Word frequency in the file:")
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("file not found.")


def problem_6():
    """
    Analyzes two text files and performs set operations on their contents.
    params: none
    return: nothing
    """
    # files
    file1 = "fileAnalysis1.txt"
    file2 = "fileAnalysis2.txt"

    # sets and set methods
    set1 = set(open(file1, "r").read().split())
    set2 = set(open(file2, "r").read().split())
    set3 = set1 & set2
    set4 = set1 - set2
    set5 = set2 - set1
    set6 = set1 ^ set2

    # print statements
    print(f"All Unique words in {file1}:")
    print(set1, "\n")
    print(f"All Unique words in {file2}:")
    print(set2, "\n")

    print(f"All the words that appear in both files:")
    print(set3, "\n")

    print(f"All the words that appear in {file1} but not {file2}:")
    print(set4, "\n")

    print(f"All the words that appear in {file2} but not {file1}:")
    print(set5, "\n")

    print(f"all the words that appear in {file1} or {file2} but not both of them: ")
    print(set6, "\n")


def problem_7(file_name):
    """
    Reads the contents of a text file and creates a dictionary where the keys are individual words found in the file,
    and the values are lists containing the line numbers in the file where each word is found.

    Params: file_name (str): The name of the text file to be analyzed.

    Returns: nothing
    """
    word_line_dict = {}
    try:
        # opens file
        with open(file_name, "r") as text:
            # Enumerate lines, starting from 1
            for line_number, line in enumerate(text, 1):
                words = line.split()
                for word in words:
                    # Convert word to lowercase to ensure case-sensitivity doesn't happen
                    word = word.lower()
                    if word in word_line_dict:
                        word_line_dict[word].append(line_number)
                    else:
                        word_line_dict[word] = [line_number]
        # prints which word displays on which lines
        print("what lines the words are in, in the file:")
        for word, line_numbers in sorted(word_line_dict.items()):
            print(f"{word}: {line_numbers}")
    except FileNotFoundError:
        print("File not found")


def main():
    problem_1()
    problem_2()
    encrypt_file("Kennedy.txt")
    decrypt_file("encrypted_Kennedy.txt")
    prob4_file = input("Enter a filename(Kennedy.txt): ")
    problem_4(prob4_file)
    prob5_file = input("Enter a filename(Kennedy.txt): ")
    problem_5(prob5_file)
    problem_6()
    prob7_file = input("Enter a filename(Kennedy.txt): ")
    problem_7(prob7_file)


if __name__ == "__main__":
    main()
