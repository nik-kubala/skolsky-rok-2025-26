def sudoku_def(vstup):
    with open(vstup, "r") as fr:
        nacitane_riadky = fr.readlines()
    
    sudoku = []
    for riadok in nacitane_riadky:
        temp = [int(i) for i in riadok.strip().split(",")]
        sudoku.append(temp)
    
    def checker(x, y, n):
        del_x = (x // 3) * 3
        del_y = (y // 3) * 3
        
        for index in range(9):
            if sudoku[x][index] == n or sudoku[index][y] == n:
                return False
        
        for index1 in range(del_x, del_x + 3):
            for index2 in range(del_y, del_y + 3):
                if sudoku[index1][index2] == n:
                    return False
        
        return True
    
    def rekurzia():
        nonlocal sudoku
        for x in range(9):
            for y in range(9):
                if sudoku[y][x] == 0:
                    for i in range(1, 10):
                        if checker(y, x, i):
                            sudoku[y][x] = i
                            if rekurzia():
                                return True
                            sudoku[y][x] = 0
                    return False
        return True
    
    if rekurzia():
        print("Sudoku vyriešené:")
        for riadok in sudoku:
            print(riadok)
    else:
        print("Sudoku nemá riešenie.")

vstup = "Hodiny/3.10.2025 - sudoku/sudoku.txt"
sudoku_def(vstup)