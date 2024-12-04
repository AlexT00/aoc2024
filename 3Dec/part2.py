import re

file = open("input.txt")
input_text = file.read()
res = 0
flag = 1
mul_cmd = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input_text)
for match in mul_cmd:
    if match == "do()":
        flag = 1
    if match == "don't()":
        flag = 0
    if flag == 1 and match != "do()" and match != "don't()":
        nums = re.findall("\d+", match)
        res += int(nums[0]) * int(nums[1])
    else:
        continue
print(res)
