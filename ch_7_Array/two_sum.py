nums = [2,7,11,15]
target = 18

# my solve(brute-force)
def two_sum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            res = num[i] + num[j]
            if res == target:
                print(i,j)

two_sum(nums,target)


# optima solve
def two_sum_optim(nums,target):
    nums_map = {}
    for i,num in enumerate(nums):
        nums_map[num] = i
        if target - num in nums_map:
            return [nums_map[target-num],i]
        # nums_map[num] = i

two_sum_optim(nums,target)