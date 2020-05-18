x = ["10010", "11110", "00011"]

x = [int(i,2) for i in x]
print(x)

print(x[0] | x[1])
#  1 0 0 1 0
#  1 0 1 1 0

#  1 0 1 1 0
v = x[0] | x[1]
print(type(bin(v)))
print(bin(v))


x = [int(i,2) for i in x]
max_one_count = 0
for i in x:
    max_one_count = max(max_one_count,bin(i).count("1"))
print(max_one_count)

