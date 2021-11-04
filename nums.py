# Вводим функцию
num = input()
nums = num.split()
nums = list(map(int, nums))
nums.sort()
f = len(nums)

#Используем след. синтаксис 
def find_missing_nums(nums):
    o = 1
    list1 = list()
    for o in range(1,f+1):
        if o not in nums:
            list1.append(i)
    return list1

print(find_missing_nums(nums))
