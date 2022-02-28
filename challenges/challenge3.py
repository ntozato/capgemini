def anagrams(string):
    result = {}
    pares = []
    res = [string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1)]

    res.sort()

    for substr in res:
        sorted_substr = "".join(sorted(substr))
        if sorted_substr not in result:
            result[sorted_substr] = 1
        else:
            result[sorted_substr] += 1
    
    for key, value in result.items():
        if value >= 2:
            pares.append(key)
    
    return len(pares)


print(anagrams('ifailuhkqq'))
