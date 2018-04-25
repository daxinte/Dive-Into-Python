# A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).

# my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)


my_new_set = set([1,2,3,2])
print(my_new_set)

a = set()
print(type(a))

a.add(5)
print(a)
a.update([2,3,4])
print(a)
a.discard(2)
print(a)
a.pop()
print(a)


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A|B)

print(A & B)
print(A - B)
print(A ^ B)