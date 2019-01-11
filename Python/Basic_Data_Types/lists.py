if __name__ == '__main__':
    N = int(input())
    result = []

    for i in range(N):
        user_input = input().split()
        if len(user_input)==3:
            user_command, place, value = user_input
            result.insert(int(place), int(value))
        elif len(user_input)==2:
            user_command, value = user_input
            if user_command=="remove":
                result.remove(int(value))
            elif user_command=="append":
                result.append(int(value))
        elif len(user_input)==1:
            user_command = user_input[0]
            if user_command=="print":
                print(result)
            elif user_command=="reverse":
                result.reverse()
            elif user_command=="pop":
                result.pop()
            elif user_command=="sort":
                result.sort()
