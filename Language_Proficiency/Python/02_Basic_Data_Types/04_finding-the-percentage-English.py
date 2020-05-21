if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Calculate average
    number = float(sum(student_marks[query_name])/len(student_marks[query_name]))
    # Print output with 2 dec place
    print(f'{number:.2f}')
