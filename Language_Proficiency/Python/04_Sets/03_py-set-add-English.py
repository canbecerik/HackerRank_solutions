import string

N = int(input())
countries = set()
for i in range(N):
    country = input()
    countries.add(country)

print(len(countries))