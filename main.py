from calc import calc_salt
from read_file import read_file_timed
from invalid_age import age_check
from item import Item


def test_first_task():
    print("FIRST TASK TEST")
    print(calc_salt(2000))
    print(calc_salt('2000'))
    print(calc_salt('abc'))
    print("____________\n")


def test_second_task():
    print("SECOND TASK TEST")
    video_data = read_file_timed('smth.csv')
    video_data = read_file_timed('smth_else.csv')
    print("____________\n")


def test_third_task():
    print("THIRD TASK TEST")
    for i in range(3):
        age_check()
    print("____________\n")


def test_fourth_task():
    print("FOURTH TASK TEST")
    Item.instantiate_from_csv('items.csv')
    for item in Item.all:
        print(item)
    print("____________\n")


if __name__ == '__main__':
    #test_first_task()
    test_second_task()
    #test_third_task()
    test_fourth_task()
