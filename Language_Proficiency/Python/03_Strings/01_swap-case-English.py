def swap_case(s):
    # New string to hold converted value
    new_s = ""
    # Iterate each character
    for i in s:
        # Convert case, if not a letter, keep it
        if i.islower():
            new_s += i.upper()
        elif i.isupper():
            new_s += i.lower()
        else:
            new_s += i
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)