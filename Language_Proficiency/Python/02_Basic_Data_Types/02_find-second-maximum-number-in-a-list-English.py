if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Copy original array
    new_arr = set(arr)

    # Remove max values
    new_arr.remove(max(new_arr))

    # Print new max (2nd max)
    print(max(new_arr))
