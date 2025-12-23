# Пример 1: Сумма элементов в списке - O(N)
def sum_list(nums):
    total = 0
    for num in nums:  # Один цикл по всем элементам
        total += num  # Каждая операция занимает постоянное время O(1)
    return total

# Пример 2: Поиск максимального элемента - O(N)


def find_max(nums):
    if not nums:
        return None

    max_num = nums[0]
    for num in nums:  # Проходим по всем элементам один раз
        if num > max_num:
            max_num = num
    return max_num

# Пример 3: Линейный поиск - O(N)


def linear_search(arr, target):
    for i in range(len(arr)):  # Один проход по массиву
        if arr[i] == target:
            return i
    return -1

# Пример 4: Печать элементов - O(N)


def print_elements(arr):
    for element in arr:  # Каждый элемент печатается один раз
        print(element)


# Демонстрация работы
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    print("Сумма элементов:", sum_list(numbers))
    print("Максимальный элемент:", find_max(numbers))
    print("Индекс числа 3:", linear_search(numbers, 3))
    print("Все элементы:")
    print_elements(numbers)

    # Визуализация зависимости времени выполнения от N
    print("\n--- Зависимость от размера входных данных ---")

    # Создаем списки разных размеров
    import time

    sizes = [1000, 10000, 100000]
    for size in sizes:
        test_list = list(range(size))

        start_time = time.time()
        sum_list(test_list)
        elapsed = time.time() - start_time

        print(f"Размер списка: {size}, время выполнения: {elapsed:.6f} сек")
