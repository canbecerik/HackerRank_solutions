if __name__ == '__main__':
    s = input()
    alphabet = False
    digit = False
    lower = False
    upper = False
    for i in s:
        if i.isalpha():
            alphabet = True
        if i.isdigit():
            digit = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
    print(alphabet or digit)
    print(alphabet)
    print(digit)
    print(lower)
    print(upper)
        
