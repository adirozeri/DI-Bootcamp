import random
import time


list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728

count = 0
start_time = time.time()

# a list size 10000 of 0s
occurrences = [x-x for x in range(0,10001)]

# counting repetitions  for every number in list of number 
for num in list_of_numbers:
    occurrences[num] = occurrences[num] + 1

# since list of ints there are target_number possibilties of couples
# iterating on all of them.
# for each couple counting their pairs with no repetition (23,45) and (45,23) count as one
# summint everything to 'count'
i=0
while i <= target_number:
    count = occurrences[i]*occurrences[target_number-i]
    i = i + 1
# print(occurrences)
print(count)

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")
