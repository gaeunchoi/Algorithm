list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = input()

for i in list:
    str = str.replace(i, '*')

print(len(str))