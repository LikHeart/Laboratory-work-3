my_list = [10, 20, 30, 40, 50, 60]
my_tuple = (10, 20, 30, 40, 50, 60)

print(f"list: {my_list}, type: {type(my_list)}, id: {id(my_list)}")
print(f"tuple: {my_tuple}, type: {type(my_tuple)}, id: {id(my_tuple)}")

id_list_before = id(my_list)
my_list[0] = 999
id_list_after = id(my_list)

print(f"id list before: {id_list_before}")
print(f"id list after: {id_list_after}")

new_tuple = (999, 20, 30, 40, 50, 60)

print(f"old tuple: {my_tuple}, id: {id(my_tuple)}")
print(f"new tuple:  {new_tuple}, id: {id(new_tuple)}")