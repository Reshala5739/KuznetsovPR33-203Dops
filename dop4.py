# MOD = 10**9 + 7

# # Функция для нахождения модульного обратного числа
# def mod_inverse(a, m):
#     t, new_t = 0, 1
#     r, new_r = m, a
#     while new_r != 0:
#         quotient = r // new_r
#         t, new_t = new_t, t - quotient * new_t
#         r, new_r = new_r, r - quotient * new_r
#     if r > 1:  # Нет обратного числа
#         return -1
#     if t < 0:  # Приводим к положительному значению
#         t += m
#     return t

# # Функция для решения линейного уравнения
# def solve_equation(a, b):
#     a_inv = mod_inverse(a, MOD)
#     if a_inv == -1:  # Нет решений
#         return -1
#     return (-b * a_inv) % MOD

# # Основная функция
# def main():
#     # Считываем количество функций
#     n = int(input().strip())
    
#     # Считываем коэффициенты функций
#     functions = []
#     for _ in range(n):
#         ai, bi = map(int, input().split())
#         functions.append((ai, bi))
    
#     # Считываем порядок удаления
#     c = list(map(int, input().split()))
    
#     # Начальная композиция
#     a, b = 1, 0
#     results = []
    
#     # Обрабатываем в обратном порядке
#     for i in range(n - 1, -1, -1):
#         ai, bi = functions[i]
        
#         # Вычисляем корень для текущей композиции
#         res = solve_equation(a, b)
#         results.append(res)
        
#         # Если удаляем текущую функцию, пересчитываем a и b
#         if i > 0:  # Последняя функция не требует обновления
#             a = (a * ai) % MOD
#             b = (a * bi + b) % MOD
    
#     # Выводим результаты в обратном порядке
#     print("\n".join(map(str, results[::-1])))

# if __name__ == "__main__":
#     main()
