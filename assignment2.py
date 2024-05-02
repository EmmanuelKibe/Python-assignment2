my_list = []

# Since append() adds the items one by one, I decided to use extend instead
my_list.extend([10, 20, 30, 40])

my_list.insert(1, 15)

another_list = (50, 60, 70)

my_list.extend(another_list)

my_list.pop(-1)

my_list.sort()

index_thirty = my_list.index(30)
print(index_thirty)





