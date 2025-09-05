def two_sum(numbers, target):
    for index1, cislo1 in enumerate(numbers):
        for index2 in range(index1 + 1, len(numbers)):
            cislo2 = numbers[index2]
            if cislo1 + cislo2 == target:
                return index1, index2