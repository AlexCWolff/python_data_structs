from unordered_list import UnorderedList

my_list = UnorderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

assert my_list.size() is 6
assert my_list.search(93) is True
assert my_list.search(100) is False

my_list.add(100)
assert my_list.search(100) is True
assert my_list.size() is 7

my_list.remove(54)
assert my_list.size() is 6
my_list.remove(93)
assert my_list.size() is 5
my_list.remove(31)
assert my_list.size() is 4
assert my_list.search(93) is False
my_list.append(123)
assert my_list.index(123) is 4
my_list.insert(3, 69)
assert my_list.index(69) is 3
my_list.insert(5, 33)
assert my_list.index(33) is 5
my_list.pop()
assert(my_list.index(77)) is 4
my_list.pop()
assert(my_list.index(69)) is my_list.size()-1
my_list.add(50)
assert(my_list.index(50)) is 0
my_list.pop()
assert(my_list.index(17)) is my_list.size()-1
