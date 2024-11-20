MOD = 10**9 + 7

def calculateMixSum(n):
    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += i & j
            result %= MOD
    return result

# Число наборов
t = int(input().strip())
results = []
for i in range(t):
# Количество красок
    n = int(input().strip())
    results.append(calculateMixSum(n))
    
for res in results:
    print(res)
