import random

# generate a list of 10 random numbers between 1 and 100
nums = []
for i in range(10):
    num = random.randint(1, 100)
    nums.append(num)
    
print(f'Before sorting: {nums}')

# traverse the list starting at index 1
for i in range(1, len(nums)):
    
    # get the number at index i
    num = nums[i]
    
    # traverse the left partition of the list (index 0 to i)
    # and find the index where num will be inserted
    new_i = i
    for j in range(i):
        if num < nums[j]:
            new_i = j
            break
            
    # on the left partition, shift numbers greater than num once to the right
    for j in range(i - 1, new_i - 1, -1):
        nums[j + 1] = nums[j]
        
    # insert num in its correct position on the left partition
    nums[new_i] = num
    
print(f'After sorting: {nums}')