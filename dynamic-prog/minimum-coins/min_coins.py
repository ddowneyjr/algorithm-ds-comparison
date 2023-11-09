def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)
    
def minimum_coins(m, coins):
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0:
                # Skip solutions that are negative
                continue
            answer = min_ignore_none(answer, minimum_coins(subproblem, coins) + 1)
    return answer


print(minimum_coins(12, [1, 4, 5]))