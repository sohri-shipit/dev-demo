numb = list(range(1,11))
cube_list = []
for num in numb:
	cube_list.append(num ** 3)

print(f"the cube list is {cube_list}")
comp_cube = [num1 ** 3 for num1 in numb]
print(f"the cube in comprehension is {comp_cube}")