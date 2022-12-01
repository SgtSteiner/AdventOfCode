def read_input():
    with open("input.txt", 'r') as f:
        return f.readlines()


def gen_bingo():
    data = [item.rstrip('\n').split() for item in read_input()]
    numbers_ = list(data[0])  # La primera línea contiene los número del bingo
    del data[0]
    del data[0]

    boards_ = []
    board = []
    i = 1
    for line in data:
        if len(line) > 0:
            board.append(list(map(int, line)))
            if i % 5 == 0:
                boards_.append(board)
                board = []
            i += 1
        else:
            i = 1
    return list(map(int, numbers_[0].split(sep=","))), boards_


def verifica_boards(first_board=True, num=0):
    line_bingo = column_bingo = False
    n_board = None
    for board_ in range(len(boards)):
        # Se busca si alguna línea del tablero se ha completado
        for line in boards[board_]:
            premiados = list(set(line) & set(current_numbers))
            if len(premiados) == len(boards[board_][0]) and first_board:
                line_bingo = True
                n_board = board_
            elif len(premiados) == len(boards[board_][0]) and num in premiados:
                line_bingo = True
                n_board = board_

        # Se busca si alguna columna del tablero se ha completado
        for col in range(len(boards[board_][0])):
            col_board = [line[col] for line in boards[board_]]
            premiados = list(set(col_board) & set(current_numbers))
            if len(premiados) == len(col_board) and first_board:
                column_bingo = True
                n_board = board_
            elif len(premiados) == len(col_board) and num in premiados:
                line_bingo = True
                n_board = board_

        if line_bingo or column_bingo:  # Si hay una línea o columna completada se deja de buscar
            break

    return n_board


def sum_unmarked_board(n_board):
    res = []
    for line in boards[n_board]:
        for n in line:
            if n not in current_numbers:
                res.append(n)
    return sum(res)


if __name__ == "__main__":
    numbers, boards = gen_bingo()
    # numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    # boards = [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]], [
    #     [3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]], [
    #              [14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]

    # Part One
    current_numbers = []
    for number in numbers:
        current_numbers.append(number)
        board_win = verifica_boards()
        if board_win:
            print(f"Part one: {sum_unmarked_board(board_win) * number}")
            break

    # Part Two
    current_numbers = []
    winner_boards = []
    for number in numbers:
        current_numbers.append(number)
        board_win = verifica_boards(False, number)
        if board_win is not None:
            print(f"Board {board_win} won!!")
            if board_win not in winner_boards:
                last_board_win = board_win
                last_number = number
                winner_boards.append(board_win)
                score = sum_unmarked_board(last_board_win) * last_number
                print(">>>>", board_win, number, score, len(winner_boards))
        if len(winner_boards) == len(boards):
            break

    print(f"\nUltimo board: {last_board_win}, último número: {last_number}")
    print(winner_boards, len(boards))
    print(f"Part two: {score}")
