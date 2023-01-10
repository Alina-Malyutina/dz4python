list = [1,4,5,6,3,4,5,6,2,7,8]
print(f"First list: {list}")
last_list = []
[last_list.append(i) for i in list if i not in last_list]
print(f"Not repeated numbers is {last_list}")