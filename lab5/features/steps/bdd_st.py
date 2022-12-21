from lab3_4.field import field
from lab3_4.unique import Unique
from behave import given, then, when

@given('a list of people')
def step_field(context):
    context.list_of_people = [
        {'name': 'Иван', 'age': 19, 'scores': [4, 5, 5, 5, 2, 3]},
        {'name': 'Мария', 'age': 17, 'scores': [3, 2, 3, 3, 3, 4]},
        {'name': 'Петр', 'age': 21, 'scores': [5, 5, 4, 4, 5, 5]},
        {'name': 'Илья', 'age': 18, 'scores': [3, 3, 3, 3, 2, 2]},
    ]

@when('I get the names')
def step_field(context):
    context.names = field(context.list_of_people, 'name')

@then('I should get a list of names')
def step_field(context):
    assert context.names == ['Иван', 'Мария', 'Петр', 'Илья']

@given('a list of str data')
def step_field(context):
    context.data = ['a', 'A', 'B', 'a', 'b']

@when('I call Unique with key ignore_case=True')
def step_field(context):
    context.unique_data = list(Unique(context.data, ignore_case=True))

@then('I get list of unique str data without big letters')
def step_field(context):
    assert context.unique_data == ['a', 'b']

@given('a list of str data2')
def step_field(context):
    context.data = ['a', 'A', 'B', 'a', 'b']

@when('I call Unique with key ignore_case=False')
def step_field(context):
    context.unique_data = list(Unique(context.data, ignore_case=False))

@then('I get list of unique str data without all letters')
def step_field(context):
    assert context.unique_data == ['a', 'A', 'B', 'b']
