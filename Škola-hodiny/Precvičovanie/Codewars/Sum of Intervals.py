def sum_of_intervals(intervals):
    temp = []
    for index in range(1, len(intervals)):
        if min(intervals[index - 1]) in range(intervals[index][0], intervals[index][1]):
            temp.append([intervals[index][0], intervals[index - 1][1]])
    print(temp)

sum_of_intervals([(1, 4), (7, 10), (3, 5)])