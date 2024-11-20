from collections import Counter

def findBeautyDegree(n, sequence):
    # Проверяем, содержатся ли все числа от 1 до max(sequence)
    maxColor = max(sequence)
    requiredColors = set(range(1, maxColor + 1))
    if requiredColors - set(sequence):
        return 0

    # Подсчет частот чисел в последовательности
    frequency = Counter(sequence).values()
    
    # Упорядоченные частоты
    sortedFrequencies = sorted(frequency, reverse=True)
    
    # Инициализация степени красоты
    beautyDegree = 0
    
    for freq in sortedFrequencies:
        if freq > beautyDegree:
            beautyDegree += 1
        else:
            break
    
    return beautyDegree


n = int(input())
sequence = list(map(int, input().split()))
print(findBeautyDegree(n, sequence))