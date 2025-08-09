my_list = []
print("Start:", my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appends:", my_list)

my_list.insert(1, 15)
print("After insert:", my_list)

my_list.extend([50, 60, 70])
print("After extend:", my_list)

my_list.pop()
print("After pop:", my_list)

my_list.sort()
print("After sort:", my_list)

print("Index of 30:", my_list.index(30))
