if __name__ == '__main__':
    # Init empty list
    students = []
    # Get input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # Add to list
        students.append([name, score])
    # Sort list according to grades
    students.sort(key = lambda x: x[1])
    # Remove lowest score
    students = [i for i in students if i[1] != students[0][1]]
    # Remove other scores than second lowest
    students = [j for j in students if j[1] == students[0][1]]
    # Sort by name
    students.sort(key = lambda x: x[0])
    # Print names of second lowest grades sorted alphabetically
    for i in range(len(students)):
        print(students[i][0])
