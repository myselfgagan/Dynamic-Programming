#to check if we can get targetSum by using given numbers
# numbers can be used multiple times 

def canSum(targetSum, numbers, memo = {}):
    print(memo)
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return True

    if targetSum < 0:
        return False
    
    for num in numbers:
        remainder = targetSum - num
        #print(remainder)
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

print(canSum(7, [2, 3], {}))
# print(canSum(7, [2, 3, 5, 7]))
# print(canSum(6, [2, 3]))
print(canSum(7, [2, 4], {}))  # added the 3rd parameter because in python
# print(canSum(8, [2, 3, 5])) # it's keep iterating through the key, pairs
# print(canSum(300, [7, 21])) # from the last function call