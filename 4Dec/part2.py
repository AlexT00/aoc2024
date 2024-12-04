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
search_key = ["M","A","S"]
mas_count = 0
'''
X must be M.A.S
Calculate all cross diagonals and check if each pair contains MAS
'''

def cross_horizontals(grid):
    mas_pairs_counts = 0
    mas_arrays = []
    p1 = 0
    p2 = 1
    p3 = 2

    p1_rev = 2
    p2_rev = 1
    p3_rev = 0

    while p3 < len(grid[0]):
        mas_arrays.append([[grid[0][p1],grid[1][p2],grid[2][p3]],[grid[0][p1_rev],grid[1][p2_rev],grid[2][p3_rev]]])
        p1 += 1
        p2 += 1
        p3 += 1
        p1_rev += 1
        p2_rev += 1
        p3_rev += 1
    for mas_pair in mas_arrays:
        if mas_pair[0] == search_key or mas_pair[0] == search_key[::-1]:
            if mas_pair[1] == search_key or mas_pair[1] == search_key[::-1]:
                mas_pairs_counts += 1
    return mas_pairs_counts

p1 = 0
p2 = 3
while p2 <= len(grid_array):
    mas_count += cross_horizontals(grid_array[p1:p2])
    p1 += 1
    p2 += 1
print(mas_count)
