#放弃

def coinChange(coins,  amount: int) -> int:
    max = coins[-1]
    nMax = 0
    i = 0
    while nMax <= amount:
        if nMax == amount:
            return i
        nMax += max
        i += 1
    n = max (0, i-2)
    amount = amount - n* max
    coins = coins[:, -1]
    coinChange(coins, amount)

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount  = 11
    a = coinChange(coins, amount)

    print(a)