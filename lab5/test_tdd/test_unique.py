from features.steps.lab3_4.unique import Unique

def test_sort_ignore_case_true():
    data = ['a', 'A', 'B', 'a', 'b']
    assert list(Unique(data, ignore_case=True)) == ['a', 'b']

def test_sort_ignore_case_false():
    data = ['a', 'A', 'B', 'a', 'b']
    assert list(Unique(data, ignore_case=False)) == ['a', 'A', 'B', 'b']