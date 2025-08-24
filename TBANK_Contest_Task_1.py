number = sorted(list(map(int, " ".join(input()).split())))
new_number = ""
zero_count = number.count(0)
if zero_count != 0:
    new_number += str(number[zero_count])
    del number[zero_count]

for i in range(len(number)):
    new_number += str(number[i])

print(new_number)
