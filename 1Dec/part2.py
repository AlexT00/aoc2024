master_list = []
list_1 = []
list_2 = []
res = ""
with open("input.txt") as input_file:
    for line in input_file:
        for char in line:
            if char.isnumeric():
                res += str(char)
            if not char.isnumeric() and res != "":
                master_list.append(int(res))
                res = ""
            else:
                continue
        if res != "":
            master_list.append(int(res))
for i in range(len(master_list)):
    if i % 2 == 0:
        list_1.append(master_list[i])
    else:
        list_2.append(master_list[i])
## Counting the number of instances in the left and right list
instances_hashmap = {}
for i in range(len(list_2)):
    if list_2[i] not in instances_hashmap:
        instances_hashmap[list_2[i]] = 1
    else:
        curr = instances_hashmap[list_2[i]]
        instances_hashmap[list_2[i]] =  curr + 1
res = 0
for num in list_1:
    if num in instances_hashmap:
        res += num * instances_hashmap[num]
    else:
        continue
print(res)
