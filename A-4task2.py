def write_and_append_file():
    filename = 'output.txt'

    # Step 1: Take user input and write to the file
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')

    # Step 2: Append additional data to the same file
    additional_input = input("Enter additional text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')

    # Step 3: Read and display final content of the file
    print(f"\nFinal content of '{filename}':\n")
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')

# Call the function
write_and_append_file()
