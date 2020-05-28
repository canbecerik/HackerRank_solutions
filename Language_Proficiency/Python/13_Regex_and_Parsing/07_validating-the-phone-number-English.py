import re

N = int(input())
[print("YES" if re.match(r"[7-9]\d{9}$", input()) else "NO") for _ in range(N)]