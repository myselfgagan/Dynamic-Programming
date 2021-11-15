def howSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        # print("targetSum = ", targetSum, "Remainder = ", remainder)
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult != None:
            ans = []
            # return [...remainderResult, num] 
            # Javascript syntex
            # print(ans)
            ans.extend(remainderResult)
            ans.append(num)    
            memo[targetSum] = ans
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(howSum(7, [2, 3], {}))
# print(howSum(7, [5, 3, 4, 7], {}))
# print(howSum(8, [2, 3, 5], {}))
# print(howSum(7, [2, 4], {}))
# print(howSum(300, [7, 14], {}))