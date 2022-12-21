goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0
    result = []
    for item in items:
        dict_result = {}
        if len(args) == 1 and item[args[0]] is not None:
            result.append(item[args[0]])
        else:
            for key in args:
                if key in item and item[key] is not None:
                    dict_result[key] = item[key]
        if len(dict_result) > 0:
            result.append(dict_result)      
    return result


# print(field(goods, 'title'))
# print(field(goods, 'title', 'price'))
# print(field(goods, 'title', 'price', 'color'))
# print(field(goods, 'title', 'color'))