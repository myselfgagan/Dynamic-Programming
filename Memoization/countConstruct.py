import sys

def countConstruct(target, wordbank, memo = {}):

    if target in memo:
        return memo[target]

    if target == "":
        return 1
    
    total = 0

    for word in wordbank:
        try:
            if target.index(word) == 0:
                # print(f"checking : {target}, {word} found")
                numWays = countConstruct(target[len(word):], wordbank, memo)
                
                total += numWays
                # print(f"total : {total}")
        except ValueError:
            pass

    memo[target] = total
    return total

        

print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeeee", "eeeee"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))