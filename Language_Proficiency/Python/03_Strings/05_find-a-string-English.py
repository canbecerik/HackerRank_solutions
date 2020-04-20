def count_substring(string, sub_string):
    # Init counter
    counter = 0
    # Find first index
    ind = string.find(sub_string)
    # Iterate over string
    for i in string:
        # If not found, return counter
        if ind == -1:
            return counter
        else:
            # Increment counter
            counter += 1
            # Throw the beginning of string until position of next unmatched part
            string = string[ind + 1:]
            # Try to find the string again
            ind = string.find(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)