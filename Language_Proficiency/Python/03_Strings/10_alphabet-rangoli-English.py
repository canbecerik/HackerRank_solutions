def print_rangoli(size):

    import string
    # Get the letters to be used
    letters = string.ascii_lowercase[0:size]

    # Iterate 2 * size - 1 times
    for i in range(size - 1, -size, -1):
        # Variable to determine line format
        x = abs(i)
        # Combine the required letters in correct sequence
        line = letters[size:x:-1] + letters[x:size]
        # Print the pattern
        print ("--" * x + '-'.join(line) + "--" * x)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)