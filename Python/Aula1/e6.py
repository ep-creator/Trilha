num = int(input())

if num % 2 == 0:
    num += 1
    print(num)
    for i in range(5):
        num += 2
        print(num)
else:
    for i in range(6):
        print(num)
        num += 2
