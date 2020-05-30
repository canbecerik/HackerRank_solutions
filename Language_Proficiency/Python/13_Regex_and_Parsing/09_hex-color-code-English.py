import re

N = int(input())
regex = r"(?<!^)(#(?:[\da-f]{3}){1,2})"

for _ in range(N):
    matches = re.findall(regex, input(), flags=re.I)
    print(*matches, sep='\n') if matches else next