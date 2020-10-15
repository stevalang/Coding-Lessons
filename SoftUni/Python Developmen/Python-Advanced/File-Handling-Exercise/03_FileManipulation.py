import os


def create_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'x'):
        pass


def append_line_to_file(fine_name, line):

    with open(file_name, 'a') as file:
        file.write(f"{line}\n")


def replace_string_in_file(file_name, old_string, new_string):
    try:
        new_lines = []
        with open(file_name, 'r') as file:
            file.readlines()

            for line in file:
                new_lines.append(line.replace(old_string, new_string))

        with open(file_name, 'w') as file:
            for line in new_lines:
                file.write(line)

    except FileNotFoundError:
        print("An error occurred")


def remove_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command_line = input()
    tokens = command_line.split('-')
    command = tokens[0]

    if command_line == 'End':
        break

    if command == "Create":
        command, file_name = tokens
        create_file(file_name)

    elif command == "Add":
        command, file_name, old_string = tokens
        append_line_to_file(file_name, old_string)

    elif command == "Replace":
        command, file_name, old_string, new_string = tokens
        replace_string_in_file(file_name, old_string, new_string)

    elif command == "Delete":
        command, file_name = tokens
        remove_file(file_name)
