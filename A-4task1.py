def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':\n")
            for line in file:
                print(line, end='')  # end='' prevents extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Run the function
read_file('sample.txt')
