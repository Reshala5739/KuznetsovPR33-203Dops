def findMinDistance(m, costs):
# cost — значение элемента массива.
# idx — его исходный индекс
    indexedCosts = sorted((cost, idx) for idx, cost in enumerate(costs))
# Из первых m элементов отсортированного списка indexedCosts выбираются индексы idx
    selectedIndices = sorted(idx for _, idx in indexedCosts[:m])
    
    minDistance = selectedIndices[-1] - selectedIndices[0] + 1

    return minDistance

# n: общее количество элементов в массиве costs.
# m: количество минимальных элементов, которые нужно выбрать.
n, m = map(int, input().split())
# массив стоимости элементов
costs = list(map(int, input().split()))

print(findMinDistance(m, costs))
