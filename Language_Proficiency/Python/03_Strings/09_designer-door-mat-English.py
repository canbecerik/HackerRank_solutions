# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    # Get input
    N, M = map(int,input().split())
    # Create pattern using list comprehension
    # .|. for 2 * i + 1 times, centered and filled with - for M chars total in range N // 2 for the top part of the pattern
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    # Join top part with the WELCOME text and reverse of the top part
    print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))

main()
