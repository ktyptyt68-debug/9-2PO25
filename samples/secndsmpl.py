
while True:
    if int(input("нажмите 1 чтобы выйти")) == 1:
        break
    else:
        print("продолжаем...")
list1 = []
for i in range(1, 21):
    print(i)
    list1.insert(i, i)

print("-"*20)
print(list1)