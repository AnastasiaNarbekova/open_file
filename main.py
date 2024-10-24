def load_cook_book(filename):
    cook_book = {}
    with open(filename, encoding='utf-8') as f:
        for i in f:
            recepie_name = i.strip()
            ingredients_count = f.readline()
            ingredients = []
            for p in range(int(ingredients_count)):
                recepie = f.readline().strip().split(' | ')
                ingredient_name, quantity, measure = recepie
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            f.readline()
            cook_book[recepie_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(person_count, dishes, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге.")
            continue
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'quantity': quantity, 'measure': ingredient['measure']}
    return shop_list
cook_book = load_cook_book('recipes.txt')
shop_list = get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'], cook_book)
print(shop_list)