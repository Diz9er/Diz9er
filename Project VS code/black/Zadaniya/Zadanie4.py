# 4ое задание с проколеджа
nums = [0]
sum = 0
while True:
    a = input('Введите число которое хотите добавить или "нет" чтобы закончить: ')
    if a == "нет":
        break
    nums.append(int(a))
    
for i in nums:
    if i > -1:
        sum += i
    else:
        break
print(sum)