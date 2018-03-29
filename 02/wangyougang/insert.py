nums = [23, 4, 87, 9, 32, 45, 6, 76, 88]
count = len(nums)
for i in range(count):
    for j in range(i+1):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)
