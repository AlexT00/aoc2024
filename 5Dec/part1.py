'''
Query each number from left to right, ensure that the remaining nums is not in the
list of numbers in the dict.
'''

file = open("input.txt", "r")
input_data = file.readlines()
## Test Case
dict_seq = {}
query_list = []
res_list = []
res_num = 0
for data in input_data:
    data = data.strip()
    if "|" in data:
        value = data[0:2]
        key = data[3:5]
        if key not in dict_seq:
            dict_seq[key] = [value]
        else:
            dict_seq[key].append(value)
    elif data != '':
        query_list.append(data.split(','))
def seq_eval(seq):
    p1 = 0
    print(seq)
    while p1 < len(seq):
        if seq[p1] not in dict_seq:
            p1 += 1
            continue
        else:
            order_list = dict_seq[seq[p1]]
            remainder_nums = seq[p1:len(seq)+1]
            set_order_list = set(order_list)
            set_remainder_nums = set(remainder_nums)
            if len(set_remainder_nums.intersection(set_order_list)) != 0:
                return False
        p1 += 1
    return True

              
for seq in query_list:
    if seq_eval(seq) == True:
        res_list.append(seq)
    else:
        continue
for res in res_list:
    if len(res) % 2 != 0:
        res_num += int(res[((len(res)+1)//2)-1])
    else:
        res_num += int(res[(len(res)//2)-1])
print(res_num)
