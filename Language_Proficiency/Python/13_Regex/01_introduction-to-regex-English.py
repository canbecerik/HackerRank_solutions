import re

[print("True" if re.match(r"^(\+|\-)?\d*\.\d+$", input()) else "False") for _ in range(int(input()))]