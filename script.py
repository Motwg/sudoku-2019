import numpy as np
from random import randint

solutions = []


def solve(matrix):
    global solutions
    for y, line in enumerate(matrix):
        for x, number in enumerate(line):
            if number == 0:
                for i in range(1, 10):
                    if check(matrix, y, x, i):
                        matrix[y][x] = i
                        solve(matrix)
                        matrix[y][x] = 0
                return False
    solutions.append(np.copy(matrix))


def check(matrix, y, x, number):
    for i in range(9):
        if matrix[y, i] == number:
            return False
        elif matrix[i, x] == number:
            return False
        elif matrix[y // 3 * 3 + i % 3, x // 3 * 3 + i // 3] == number:
            return False
    return True


def generate():
    new_sudoku = np.zeros((9, 9))
    while solve(new_sudoku):
        x = randint(0, 8)
        y = randint(0, 8)
        number = randint(1, 9)
        if check(new_sudoku, y, x, number):
            new_sudoku[y][x] = number
        print(new_sudoku)


def load(filename):
    def split(str_array):
        str_matrix = list(map(str.split, str_array))
        int_matrix = []
        for array in str_matrix:
            if len(array) == 9:
                int_matrix.append(list(map(int, array)))

        if len(int_matrix) == 9:
            return np.array(int_matrix)
        else:
            raise Exception('Sudoku is not valid')

    with open(filename) as f:
        lines = f.read().splitlines()
        lines = split(lines)
        return lines


def save_solutions(filename):
    global solutions

    with open(filename, 'w') as f:
        for solution in solutions:
            np.savetxt(f, [sol for sol in solution], fmt='%1d', footer=' ')
        f.write('# Made by Motwg')


if __name__ == '__main__':
    sudoku = load('sudoku.txt')
    solve(sudoku)
    save_solutions('solutions.txt')
