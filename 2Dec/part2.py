day_list = []
with open("input.txt") as inputs:
    for row in inputs:
        rows_list = row.split(' ')
        rows_list[-1] = rows_list[-1].strip()
        day_list.append(rows_list)

res_count = 0
def safe_check(list):
    sign_diff = int(list[1])-int(list[0])
    if sign_diff < 0:
        sign_diff = -1
    else:
        sign_diff = 1
    for i in range(0,len(list)-1):
        '''
        Ensure consistency, check what is the diff prior
        Check that it decreases by at least 1 and at most 3
        '''
        diff = int(list[i+1])-int(list[i])
        if sign_diff < 0:
            if diff > 0:
                return False
        if sign_diff > 0:
            if diff < 0:
                return False
        if 1 <= abs(diff) <= 3:
            if i == len(list)-2:
                return True
            else:
                continue
        return False
        

for rows in day_list:
    ## All possible combinations of each rows
    if safe_check(rows):
        res_count += 1
    else:
        permu_count = 0
        for i in range(len(rows)):
            combination = rows[:i] + rows[i + 1:]
            if safe_check(combination) and permu_count == 0:
                permu_count = 1
                res_count += 1
                break
print(res_count)
