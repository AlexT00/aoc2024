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
rectify_list = []
res_num = 0
res_list_1 = []
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
        rectify_list.append(seq)

def rectify_seq(seq):
    '''
    Naively swap violating elements in the sequence until we get a correct sequence
    '''
    while seq_eval(seq) != True:
        p1 = 0
        p2 = 0
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
                    element_swap = list(set_remainder_nums.intersection(set_order_list))
                    element_index = seq.index(element_swap[0])
                    seq[p1], seq[element_index] = seq[element_index], seq[p1]
                    break
                else:
                    p1 += 1
                    continue
    return seq

for rectify in rectify_list:
    res_list_1.append(rectify_seq(rectify))
    
for res in res_list_1:
    if len(res) % 2 != 0:
        res_num += int(res[((len(res)+1)//2)-1])
    else:
        res_num += int(res[(len(res)//2)-1])

print(res_num)

