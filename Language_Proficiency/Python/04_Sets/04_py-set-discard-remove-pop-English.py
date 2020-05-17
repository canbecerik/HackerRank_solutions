def main():
    n = int(input())
    s = set(map(int, input().split())) 
    for i in range(int(input())):
        command = input()
        if command == "pop":
            try:
                s.pop()
            except KeyError:
                print ("Key error")
                return
        else:
            eval('s.{0}({1})'.format(*command.split()+['']))
    print(sum(s))
main()