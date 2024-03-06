import random
import time

rang=10000
numbers_amount = 20000
list_of_numbers = [random.randint(0, rang) for _ in range(numbers_amount)]
target_number   = 3728

count = 0
start_time = time.time()

# a list size target_number of 0s
occurrences = [x-x for x in range(0,target_number+1)]

# counting repetitions  for every number in list of number 
for num in list_of_numbers:
   if (num < target_number): # no need to count numbers bigger thatn target_number
        occurrences[num] = occurrences[num] + 1


# since list of ints there are (target_number-1)/2 possibilties of couples withut repetition
# iterating on all of them.
# summing everything to 'count'
 

i=0
count=0
while i < int((target_number-1)/2):#iterating untill half of taget_nmer not including half
    count = count + occurrences[i] * occurrences[target_number-i]
    i = i + 1

print(count)


end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")
