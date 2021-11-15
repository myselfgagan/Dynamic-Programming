import sys

def canConstruct(target, wordbank, memo = {}):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in wordbank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct(suffix, wordbank, memo) == True:
                    memo[target] = True
                    return True
        except ValueError:
            pass
    memo[target] = False
    return False
        

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeeee", "eeeee"]))
