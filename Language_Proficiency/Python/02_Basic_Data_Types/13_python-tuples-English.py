if __name__ == '__main__':
    N = int(input())
    # List to hold input command
    commands = []
    # The actual list
    theList = []
    # Iterate over N
    for i in range(N):
        # Get current command
        commands = input().split()
        # Print if the command is print
        if commands[0] == "print":
            print(theList)
        # Process command
        else:
            # Get arguments
            args = commands[1:]
            # Construct command from arguments
            cmd = commands[0] + "(" + ",".join(args) + ")"
            # Eval the command
            eval("theList." + cmd)