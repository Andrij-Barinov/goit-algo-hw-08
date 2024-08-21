import heapq

def minimize_cable_connection_cost(lengths):
    # Перетворюємо список довжин кабелів у мін-купу
    heapq.heapify(lengths)
    
    total_cost = 0
    
    # Виконуємо з'єднання, поки не залишиться один кабель
    while len(lengths) > 1:
        # Виймаємо два найменших кабелі
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        
        # Об'єднуємо їх і додаємо витрати
        combined = first + second
        total_cost += combined
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(lengths, combined)
    
    return total_cost

# Приклад використання
lengths = [8, 4, 6, 12]
result = minimize_cable_connection_cost(lengths)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")
