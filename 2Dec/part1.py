day_list = []
with open("input.txt") as inputs:
    for row in inputs:
        rows_list = row.split(' ')
        rows_list[-1] = rows_list[-1].strip()
        day_list.append(rows_list)
res_count = 0
for rows in day_list:
    sign_diff = int(rows[1])-int(rows[0])
    if sign_diff < 0:
        sign_diff = -1
    else:
        sign_diff = 1
    for i in range(0,len(rows)-1):
        '''
        Ensure consistency, check what is the diff prior
        Check that it decreases by at least 1 and at most 3
        '''
        diff = int(rows[i+1])-int(rows[i])
        if sign_diff < 0:
            if diff > 0:
                break
        if sign_diff > 0:
            if diff < 0:
                break
        if 1 <= abs(diff) <= 3:
            if i == len(rows)-2:
                res_count += 1
            else:
                continue
        break
print(res_count)
                
        
        
