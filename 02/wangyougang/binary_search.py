nums = [5, 13, 19, 21, 37, 56, 64, 75, 80, 88, 92]
low = 0
high = len(nums) - 1
num = int(input('请输入你一个数字:'))
if num in nums:
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > num:
            high = mid - 1
        elif nums[mid] < num:
            low = mid + 1 
        elif nums[mid] == num:
            print("输入的数字在列表的第" + str(mid) + "位置")
            break
else:
    print('输入的数字不在列表中!')
