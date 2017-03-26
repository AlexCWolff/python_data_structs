from ordered_list import OrderedList

my_list = OrderedList()

assert my_list.is_empty is True
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)
assert my_list.size is 6
assert my_list.search(93) is True
assert my_list.search(100) is False
