n = int(input("enter n:"))
posloupnost = [0, 1]
for i in range(n-2):
    posloupnost.append(posloupnost [-1]+posloupnost [-2])
print(posloupnost)