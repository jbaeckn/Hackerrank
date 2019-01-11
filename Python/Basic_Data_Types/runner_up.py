if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    #use 'set' to remove duplicates
    print(sorted(list(set(arr)))[-2])
