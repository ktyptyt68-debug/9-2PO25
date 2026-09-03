
def function1(int1, int2, list1):
    for i in range(1, 21):
        print(i)
        list1.append(i)
    print("-"*20)
    print(list1)

while True:
    if int(input("нажмите 1 чтобы выйти")) == 1:
        break
    else:
        print("продолжаем...")

list1 = []
function1(1, 21, list1)