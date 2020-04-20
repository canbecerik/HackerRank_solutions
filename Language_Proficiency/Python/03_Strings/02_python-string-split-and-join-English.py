def split_and_join(line):
    str1 = line.split()
    str2 = "-".join(str1)
    return str2
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)