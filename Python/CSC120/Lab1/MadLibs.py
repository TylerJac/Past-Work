# ===============================================================

# Name: Tyler Jackson

# Date: 1//31/2024

# Course: CSC 120 NLE01

# Algorithm: 1. ask for input filename 2.ask for output filename 3. open filename re prompt if fileNotFound
# 4. create list of lines from input 5.open output filename 6. process each line 7. search line for token/placeholder
# 8. get new word from user for token 9. replace token with new word 10. write lines to output filename
# 11. ask if user want to see result 12. ask if user want to do again, exit if no

# References: in class

# ===============================================================

def open_file(file_name):
    """
     opens the mad libs file
    param: file_name = name of the file
    return: line_list = list of lines from the file
    """

    line_list = []
    # open the file using the file_name argument
    with open(file_name, "r") as file:
        for line in file:
            line_list.append(line)

        return line_list


def find_delims(line_list):

    """
    finds the delimiters and stores the indexes, and string in lists
    param: line_list = list of lines from the file
    return: delim_id_list = list of delimiter identification, delim_idx_list = list of delimiter indexes,
     line_list = list of lines from file
    """

    # list variables
    delim_idx_list = []
    delim_id_list = []
    start = 0

    for line in line_list:
        for char in line:
            if char == "<":
                # start var = index of "<"
                start = line.index(char)
            if char == '>':
                # end var = index of ">"
                end = line.index(char)
                delim_idx_list.append((start, end))
                # append delim index to idx list, and id to id list
                delim_id_list.append(line[start:end + 1])

    return delim_id_list, delim_idx_list, line_list


def gather_input(delim_id_list, delim_idx_list, line_list):
    """
    gathers input for each delimiter in the text file
    params: delim_id_list = list of delimiter identification, delim_idx_list = list of delimiter indexes,
     line_list = list of lines from file
    return: word_list = list of words to replace delimiters with, line_list = list of lines from file
    """
    word_list = []
    # zipping lists together
    for delim in zip(delim_id_list, delim_idx_list):
        # append new word
        word_list.append(input(f"Please type a {delim[0][1:-1]}:  "))

    return word_list, line_list


def replace_delim_w_word(word_list, line_list):
    """
    replaces the delimiters with the new words
    params: word_list = list of words to replace delimiters with, line_list = list of lines from file
    return: new_string = The updated string to be written to the new file
    """
    # controls whether it adds characters or not
    exempt = False
    count = 0
    # controls what word it adds to the new string
    new_string = ""
    for line in line_list:
        for char in line:
            if char == "<":
                # add new word to new_string
                new_string += word_list[count]
                # next word
                count += 1
                # don't add characters to new_line
                exempt = True
            elif char == ">":
                # being adding characters to new_line again
                exempt = False

            elif not exempt:
                # add the character to the new_line
                new_string += char
        # add a new line to the end of each line
        new_string += "\n"

    return new_string


def view_result(yesno, file_name):
    """
    takes a yes or a no to viewing file, if yes, displays file
    params: yesno = a string response to the question "Would you like to see the result [y/n]",
     file_name = name of the new file
    return: N/A
    """
    # if yes print each line
    if yesno == "y":
        with open(file_name, "r") as file:
            for line in file:
                print(line)


def main():
    # open_file then find delimiters then gather input then replace delimiters with words
    # then store result in new_string var
    new_string = replace_delim_w_word(*gather_input(*find_delims(open_file(input("Enter the file name: ")))))
    # name of the new file
    new_file_name = input("Output filename: ")
    # open new file
    new_file = open(new_file_name, "w")
    # write string to new file
    new_file.write(new_string)
    new_file.close()
    # view or not
    view = input("Would you like to see the result [y/n]:  ")

    # handle view results
    view_result(view, new_file_name)


if __name__ == "__main__":
    main()
