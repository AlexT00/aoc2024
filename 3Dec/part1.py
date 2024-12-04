import re

file = open("input.txt")
input_text = file.read()
res = 0
mul = re.findall("mul\(\d{1,3},\d{1,3}\)", input_text)
for match in mul:
    nums = re.findall("\d+", match)
    res += int(nums[0]) * int(nums[1])
print(res)

