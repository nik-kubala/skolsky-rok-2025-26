def find_missing(sequence):
    difference = (sequence[-1] - sequence[0]) / len(sequence)
    for i in range(0, len(sequence) - 1):
        if difference != sequence[i + 1] - sequence[i]:
            return sequence[i] + difference