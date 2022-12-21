from features.steps.lab3_4.field import field

def test_field():
    students = [
        {'name': 'Иван', 'age': 19, 'scores': [4, 5, 5, 5, 2, 3]},
        {'name': 'Мария', 'age': 17, 'scores': [3, 2, 3, 3, 3, 4]},
        {'name': 'Петр', 'age': 21, 'scores': [5, 5, 4, 4, 5, 5]},
        {'name': 'Илья', 'age': 18, 'scores': [3, 3, 3, 3, 2, 2]},
    ]

    assert field(students, 'name') == ['Иван', 'Мария', 'Петр', 'Илья']
