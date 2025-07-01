arr = [1,2,[3,4],[5,6]]

output_arr = []

for i in arr:
    if isinstance(i, list):
        output_arr.extend(i)
    else:
        output_arr.append(i)

print(output_arr)            