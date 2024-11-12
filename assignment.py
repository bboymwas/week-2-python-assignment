my_list = []
# APPEND
my_list.append ("10")
my_list.append ("20")
my_list.append ("30")
my_list.append ("40")
print(my_list)
# INSERTION
my_list.insert(1,"15")
print(my_list)
# EXTEND
my_list.extend(["50","60","70"])
print(my_list)
# REMOVE
# my_list.remove("70")
# or 
del my_list[7]
print(my_list)
# Sorting List
my_list.sort()
print("Ascending sorted list:", my_list)
# Finding and printing an index value
index_30 =my_list.index("30")
print(index_30)
