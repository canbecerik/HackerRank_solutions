from cmath import phase

# Get input
z = complex(input())


phi = phase(z)
r = abs(complex(z))

print(f"{r}\n{phi}")