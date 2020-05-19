def action(A, set_in, comm_in):
    eval('A.{0}(set_in)'.format(comm_in))
    return

def main():
    number_A = int(input())
    A = set([int(i) for i in input().split(' ')])
    number_N = int(input())

    for i in range(number_N):
        comm_in = input().split(' ')
        set_in =  set([int(j) for j in input().split(' ')])
        action(A, set_in, comm_in[0])
    
    print(sum(A))

main()