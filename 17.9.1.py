spisok = '3 6 2 8 1 5 17 23 18 23 70 68'
lst = [int(i) for i in spisok.split()]
num = int(input('Enter a number from 0 to 70: '))

try:
    if 0 < num < 70:
        lst.append(num)
    else:
        num = int(input('Enter a valid number: '))
        lst.append(num)
except ValueError:
    print('Incorrect data')

for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)

def bi_search(num: int, lst: list, left, right) -> int:
    len(lst)
    while left < right:
        middle = (left + right) // 2
        if lst[middle] < num:
            left = middle + 1
        else:
            right = middle
    return left
print('Element number:', bi_search(num, lst, 0, len(lst) - 1))