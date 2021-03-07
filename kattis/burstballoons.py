def maxCoinRight(nums) -> int:
    print("R:",nums)
    if len(nums) <= 2:
    	return 0
        
    ret = 0
    i = nums.index(max(nums[1:-1]))
    if i != 1:
        ret = maxCoinLeft(nums[:i+1])
        nums = nums[0:1] + nums[i:]

    while len(nums) > 2:
        ret += nums[0]*nums[2]*nums.pop(1)
    
    return ret
    
def maxCoinLeft(nums) -> int:
    print("L:",nums)
    if len(nums) <= 2:
        return 0
    if len(nums) == 3:
       return nums[0]*nums[2]*nums.pop(1)
    i = nums.index(max(nums))
    L = nums[:i+1]
    R = nums[i:]
    return 0
    
def maxCoins(nums) -> int:
    temp = [1] + nums + [1]
    while 0 in temp:
        temp.remove(0)
    print("begin:",temp)
    i = temp.index(max(temp))
    L = temp[:i+1]
    R = temp[i:]
    return maxCoinLeft(L) + maxCoinRight(R) + max(temp)
    

print(maxCoins([9,2,6,4,3]))