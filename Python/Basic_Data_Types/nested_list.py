if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
    
    grade = sorted(set([b for a,b in python_students]))[1]
    result = sorted([x for x,y in python_students if y==grade])
    print('\n'.join(result))
