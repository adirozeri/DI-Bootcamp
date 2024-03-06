import random
import time
[9184, 1450, 7299, 3328, 9872, 313, 4696, 8516, 42, 9612, 5967, 2426, 9626, 2513, 5471, 3299,
  9099, 273, 7156, 4644, 5123, 3379, 7944, 171, 5239, 9711, 3323, 5981, 5109, 864, 9790, 3518,
    6863, 446, 9775, 4803, 4881, 7225, 1697, 4133, 1547, 1473, 6599, 2371, 8805, 995, 4843, 114,
      6278, 9549, 4251, 1429, 2411, 9435, 8915, 9967, 2350, 8439, 6151, 9530, 3039, 9703, 1455, 
      7751, 7507, 9847, 8726, 2799, 6647, 5264, 5412, 6658, 653, 1597, 3044, 604, 3946, 8169, 9442,
        7152, 227, 5896, 9397, 1675, 32, 5272, 7326, 9140, 1296, 8772, 6985, 1407, 4578, 4626, 828, 5635, 
        5341, 6953, 1835, 5750, 6411, 5306, 5786, 5254, 5335, 9204, 2498, 5358, 5549, 8891, 7873, 3417, 6561, 6954,
          6553, 521, 2740, 4522, 4320, 8605, 3896, 935, 1478, 7261, 7635, 6479, 7474, 1908, 4803, 9571, 7578, 3722,
            689, 1425, 600, 2885, 1642, 4210, 3933, 5645, 132, 9448, 3950, 67, 867, 6053, 1534, 7500, 1103, 1762, 4869,
              6873, 3431, 5036, 7782, 6601, 3517, 1626, 9075, 5434, 3874, 7814, 1961, 6210, 5196, 5420, 142, 6862, 8919,
                1806, 8732, 6787, 8285, 1481, 8692, 481, 7630, 2988, 6478, 8055, 5330, 4447, 1246, 4577, 1641, 8799, 7894,
                  9094, 7098, 4118, 
9867, 2214, 6256, 3277, 9238, 34, 5565, 848, 6107, 6548]



rang=100
numbers_amount = 200
list_of_numbers = [random.randint(0, rang) for _ in range(numbers_amount)]
target_number   = 2
# list_of_numbers = [random.randint(0, rang-2) for _ in range(20000)]
# list_of_numbers = list_of_numbers 
print(list_of_numbers)

count = 0
start_time = time.time()

# a list size 10000 of 0s
occurrences = [x-x for x in range(0,target_number+1)]
# print(occurrences)
# occurrences1 = occurrences.copy()
# occurrences2 = occurrences.copy()

# occurrences1 = map(lambda x: list_of_numbers.count(x[1]) , enumerate(occurrences)) 
# counting repetitions  for every number in list of number 


# for num in list_of_numbers:
#    occurrences2[num] = occurrences2[num] + 1

# print(occurrences1 == occurrences2)


for num in list_of_numbers:
   if (num < len(occurrences)):
        occurrences[num] = occurrences[num] + 1

print(occurrences)

# since list of ints there are target_number possibilties of couples
# iterating on all of them.
# for each couple counting their pairs with no repetition (23,45) and (45,23) count as one
# summint everything to 'count'
 
# print(occurrences[1])
# print(occurrences[target_number-1])

i=0
count=0
while i < target_number:
    count = count + occurrences[i] * occurrences[target_number-i]
    if occurrences[i]*occurrences[target_number-i] != 0:
        print(f'i(number)={i} - occ= {occurrences[i]},    target_number-i(number) = {target_number-i}  occ={occurrences[target_number-i]}')
    i = i + 1
# print(occurrences)
remove_middle_pair = 0
if target_number % 2 == 0:
    remove_middle_pair = occurrences[int(target_number/2)]**2
print(count-remove_middle_pair)

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")
