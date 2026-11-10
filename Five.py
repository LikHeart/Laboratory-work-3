const = ("Медный", "ул. Максима Горького 24", "инвентаризация 21.12.2027")
supplies = sorted(["P-1", "P-2","P-4", "P-3","P-6", "P-5","P-8", "P-7"])
articuli = {"A-101", "A-102", "A-103", "A-104", "A-105", "A-106", "A-107", "A-108"}
items = {
    "A-101": "Болт М8x40",
    "A-102": "Гайка М8",
    "A-103": "Шайба 8",
    "A-104": "Винт М6x30",
    "A-105": "Гайка М6",
    "A-106": "Шайба 6",
}
print(f'Склад {const}')
print(f'Поставки {supplies}')
print(f'Артикулы {articuli}')
print(f'Товары {items}')

supplies.append("P-8")
supplies.append("P-9")

print(f'Поставки с добавлением {supplies}')

print("Наличие А-105:", "Да" if "A-105" in articuli else "нет")

print("Названия товара A-107: ", items.get("A-107"))