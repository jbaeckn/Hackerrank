phoneNumber = {}
x = int(input())
for i in range(x):
    name, number = input().split()
    phoneNumber[name] = number
    
for i in range(x):
    query_name = input()
    if query_name in phoneNumber.keys():
        print(query_name + "=" + phoneNumber[query_name])
    else:
        print("Not found")
