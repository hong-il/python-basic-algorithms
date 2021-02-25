def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 3
    cache = ["Jeju", "Pangyo", "Seoul"]
    answer = 0
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.pop(cache.index(c))
            cache.append(c)
            pass
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(c)
                cache = cache[-cacheSize: ]
                answer += 5
            else:
                cache = cache[1:] + [c]
    return answer
