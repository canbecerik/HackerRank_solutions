def print_formatted(number):
    
    # Calculate padding
    total_length = len("{0:b}".format(number))

    # Iterate for each number
    for curr_num in range(1, (number + 1)):
        
        # Print each value with fixed total_length using format
        print("{0:{1}} {0:{1}o} {0:{1}X} {0:{1}b}".format(curr_num, total_length))



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)