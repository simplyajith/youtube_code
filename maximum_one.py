

string = "11111000011110"

starting_window = 0
count_continuous_ones = 0
count_list = []

for end_window in range(len(string)):

    if string[end_window] != "1":
        count = end_window - starting_window
        starting_window = end_window + 1
        count_continuous_ones = 0
        count_list.append(count)
        count_list.append(count_continuous_ones)

    else:
        count_continuous_ones += 1

count_list.append(count_continuous_ones)

print(max(count_list))


