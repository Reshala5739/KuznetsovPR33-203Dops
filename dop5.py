def main():
    n, m = map(int, input().split())
    
    # Считываем предпочтения
    pereferences = []
    for i in range(m):
        first, last, operator, summ = input().split()
        pereferences.append((int(first) - 1, int(last) - 1, operator, int(summ)))
    
    # Переменные, изначально все нули
    variables = [0] * n
    
    # Применяем ограничения
    for first, last, operator, summ in pereferences:
        currentSumm = sum(variables[first:last + 1])
        
        if operator == ">=" and currentSumm < summ:
            # Нужно увеличить сумму
            diff = summ - currentSumm
            increment = diff // (last - first + 1) + (1 if diff % (last - first + 1) else 0)
            for i in range(first, last + 1):
                variables[i] += increment
        elif operator == "<=" and currentSumm > summ:
            # Нужно уменьшить сумму
            diff = currentSumm - summ
            decrement = diff // (last - first + 1) + (1 if diff % (last - first + 1) else 0)
            for i in range(first, last + 1):
                variables[i] -= decrement

    # Проверяем, выполнены ли все ограничения
    for first, last, operator, summ in pereferences:
        currentSumm = sum(variables[first:last + 1])
        if operator == ">=" and currentSumm < summ:
            print("NO")
            return
        elif operator == "<=" and currentSumm > summ:
            print("NO")
            return

    print("YES")


