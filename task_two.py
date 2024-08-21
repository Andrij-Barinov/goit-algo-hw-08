import heapq

def merge_k_lists(lists):
    # Створюємо мінімальну купу
    min_heap = []
    
    # Ініціалізуємо купу першими елементами з кожного списку
    for i, sorted_list in enumerate(lists):
        if sorted_list:  # Якщо список не порожній
            heapq.heappush(min_heap, (sorted_list[0], i, 0))
    
    merged_list = []
    
    # Поки купа не порожня, витягуємо мінімальні елементи і додаємо в результуючий список
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Якщо є ще елементи в тому ж списку, додаємо наступний елемент до купи
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
