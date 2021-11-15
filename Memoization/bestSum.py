def bestSum(targetSum, numbers, memo = {}):

    shortestCombination = None

    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination != None:
            ans = []
            ans.extend(remainderCombination)
            ans.append(num)
            if shortestCombination == None or len(ans) < len(shortestCombination):
                shortestCombination = ans

    memo[targetSum] = shortestCombination
    return shortestCombination
              

# print(bestSum(7, [5, 3, 4, 7]))
# print(bestSum(8, [2, 3, 5]))
# print(bestSum(8, [1, 4, 5]))
print(bestSum(100, [1, 2, 5, 25]))