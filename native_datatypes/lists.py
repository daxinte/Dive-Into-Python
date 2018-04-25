my_list = ['Daniel', 36, ['Marius', 'Miha'], 0]
# print(my_list[0])
# print(my_list[-0])
# print(my_list[-3])
print(my_list[2][1])
print(my_list[0][0])
print(my_list[1:3])
print(my_list[:1])
my_list[0] = 'Test'
my_list.append(4)
my_list.extend([4, 6, "cinci"])
del my_list[1]
another_list = [3,4,6,2,3,4,5,78,]
another_list.sort()	
print(another_list)
another_list.reverse()
print(another_list)
last_list = enumerate(another_list)
print(type(last_list))
print(list(last_list))

# used for?
last_stand_list = enumerate(another_list, 10)
print(type(last_stand_list))
print(list(last_stand_list))





