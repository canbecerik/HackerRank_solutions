#!/bin/python3

# Complete the minimumBribes function below.
def minimumBribes(q):
    min_bribes = 0
    # Reinitialize position stickers to match index
    q = [i - 1 for i in q]
    q_enum = enumerate(q)

    for init, curr in q_enum:
        # Check if anyone moved more than twice
        if curr - init > 2:
            print("Too chaotic")
            return
        # Check if current person received a bribe
        # Look at between one position in front of his current pos (curr -1 )
        # and one position in front of his init position
        bribe_check_range = range(max(curr - 1, 0), init)
        for j in bribe_check_range:
            # If anyone in the range has a larger number than the curr person,
            # He must have received a bribe
            if q[j] > curr:
                min_bribes += 1
    print(min_bribes)
    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
