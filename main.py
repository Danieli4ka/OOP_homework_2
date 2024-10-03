def recipes_from_file(file_names):
    with open(file_names, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cook_book = {}
    i = 0

    while i < len(lines):
        dish_name = lines[i].strip()
        i += 1
        ingredient_count = int(lines[i].strip())
        i += 1
        ingredients = []
        for q in range(ingredient_count):
            ingredient_str = lines[i].strip().split(' | ')
            ingredient_name = ingredient_str[0]
            quantity = int(ingredient_str[1])
            measure = ingredient_str[2]
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
            i += 1
        cook_book[dish_name] = ingredients
        i += 1
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = recipes_from_file(file_name)
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
        else:
            print(f'Блюдо {dish} не найдено в книге рецептов')

    return shop_list


file_name = 'recipes.txt'
print(recipes_from_file(file_name))
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))