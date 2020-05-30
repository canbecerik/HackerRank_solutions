import re

N = int(input())
for _ in range(N):
    string = input().split()
    regex = r"^<[A-Za-z][\w|\_|\-|\.]+\@[A-Za-z]+\.[A-Za-z]{1,3}>$"
    if re.match(regex, string[1]):
        print(*string)