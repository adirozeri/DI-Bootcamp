# 1
my_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
    # [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
    # [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
    # [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# 2a
print('list of numbers printed in a single line')
for a in my_list:
    print(a,  end=' ')
print('\n',my_list)

# 2b
print('list of numbers sorted desc')
sorted_list = sorted(my_list)
for a in sorted_list[::-1]:
    print(a,  end=' ')
print('\n',sorted_list)

#2c
print('the sum: ',sum(my_list))


