from my_code import append_to_list
from my_code import insert_to_list
from my_code import remove_from_list
from my_code import sort_ascending
from my_code import check_list


list = [3, 18, 2, 75, 8, 33]

def test_append_to_list():
    assert [3, 18, 2, 75, 8, 33, 123] == append_to_list(list)

def test_insert_to_list():
    assert [3, 18, 12, 2, 75, 8, 33, 123] == insert_to_list(list)


def test_remove_from_list():
    assert [3, 18, 12, 2, 75, 33, 123] == remove_from_list(list)


def test_sort_ascending():
    assert [2, 3, 12, 18, 33, 75, 123] == sort_ascending(list)


def test_check_list():
    assert True == check_list(list) 