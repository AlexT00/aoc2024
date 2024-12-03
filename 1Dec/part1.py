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
list_1_sorted = sorted(list_1)
list_2_sorted = sorted(list_2)
diff = 0
for i in range(len(list_1_sorted)):
    diff += abs(list_1_sorted[i] - list_2_sorted[i])
print(diff)
