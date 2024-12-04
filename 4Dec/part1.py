import sys
file = open("input.txt",'r')
input_data = file.readlines()

grid_array = []
row_array = []
for row in input_data:
    row = row.strip()
    for char in row:
        row_array.append(char)
    grid_array.append(row_array)
    
    row_array = []
res_count = 0
search_key = ["X","M","A","S"]
'''
8 Different Directions:
1. Left to Right
2. Right to Left
3. Up to Down
4. Down to Up
5. Diagonal Top left to  Bottom right
6. Diagonal Bottom right to Top Left
7. Diagonal Top right to Bottom Left
8. Diagonal Bottom Left to Top right
'''
def horizontal(row):
    ## Left to Right
    p1 = 0
    p2 = 4
    xmas_count = 0
    while p2 <= len(row):
        if row[p1:p2] == search_key:
            xmas_count += 1
        p1 += 1
        p2 += 1
    ## Right to Left
    row = row[::-1]
    p1 = 0
    p2 = 4
    while p2 <= len(row):
        if row[p1:p2] == search_key:
            xmas_count += 1
        p1 += 1
        p2 += 1
    return xmas_count

def vertical(grid):
    # Up to down
    zipped = list(map(list,zip(*grid)))
    xmas_count = 0
    for strings in zipped:
        if strings == search_key:
            xmas_count += 1
    ## Down to Up
    reversed_zip = map(lambda x: x[::-1], zipped)
    for strings in reversed_zip:
        if strings == search_key:
            xmas_count += 1
    return xmas_count

def diagonals(grid):
    ## Left to Right Diagonal
    xmas_count = 0
    p1 = 0
    p2 = 1
    p3 = 2
    p4 = 3
    diagonal_tlbr = []
    while p4 < len(grid[0]):
        diagonal_tlbr.append([grid[0][p1], grid[1][p2], grid[2][p3], grid[3][p4]])
        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1
    diagonal_brtl = list(map(lambda x: x[::-1], diagonal_tlbr))
    ## Right to left Diagonal
    diagonal_trbl = []
    p1 = 3
    p2 = 2
    p3 = 1
    p4 = 0
    while p1 < len(grid[0]):
        diagonal_trbl.append([grid[0][p1],grid[1][p2],grid[2][p3],grid[3][p4]])
        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1
    diagonal_bltr = list(map(lambda x: x[::-1], diagonal_trbl))
    ## Counting:
    for seq in diagonal_tlbr:
        if seq == search_key:
            xmas_count += 1
    for seq in diagonal_brtl:
        if seq == search_key:
            xmas_count += 1
    for seq in diagonal_trbl:
        if seq == search_key:
            xmas_count += 1
    for seq in diagonal_bltr:
        if seq == search_key:
            xmas_count += 1
    return xmas_count
## Horizontal Counting
for row in grid_array:
    res_count += horizontal(row)

## Vertical Counting
r1 = 0
r2 = 4
while r2 <= len(grid_array):
    res_count += vertical(grid_array[r1:r2])
    r1 += 1
    r2 += 1
## Diagonal Counting
r1 = 0
r2 = 4
while r2 <= len(grid_array):
    res_count += diagonals(grid_array[r1:r2])
    r1 += 1
    r2 += 1
    
print(res_count)
