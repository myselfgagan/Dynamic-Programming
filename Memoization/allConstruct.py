def allConstruct(target, wordbank, memo = {}):
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []

    for word in wordbank:
        if word in target:
            if target.index(word) == 0:
                suffix = target[len(word):]
                suffixWays = allConstruct(suffix, wordbank, memo)
                def add_word(x):
                    y =[word]
                    y.extend(x)
                    return y
                targetWays = map(add_word, suffixWays)
                result.extend(targetWays)
    memo[target] = result
    return result

#print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
#print(allConstruct("abcdef", ["ab", "abc", 'cd', 'def', 'abcd', 'ef', 'c']))
print(allConstruct('aaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaaa']))