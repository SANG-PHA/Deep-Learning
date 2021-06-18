
game_board = ['','','',
              '','','',
              '','','']

def empty_cells(board):
    cells = []
    for x, cell in enumerate(board):
        if cell == '':
            cells.append(x)
    return cells

def valid_move(x):
    return x in empty_cells(game_board)

def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return  True
    return  False

def draw(board):
    for i, cell in enumerate(board):
        if i%3 == 0:
            print('\n---------------')
        print('|', cell, '|', end='' )
    print('\n---------------')

def evaluate(board):
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score

def check_win(board, player):
    win_conf = [
        [board[0],board[1],board[2]],
        [board[3],board[4],board[5]],
        [board[6],board[7],board[8]],
        [board[0],board[3],board[6]],
        [board[1],board[4],board[7]],
        [board[2],board[5],board[8]],
        [board[0],board[4],board[8]],
        [board[2],board[4],board[6]],
    ]
    return [player, player, player] in win_conf

def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')

def minimax(board, depth, maxPlayer):
    pos = -1
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)

    if maxPlayer:
        value = -10000
        for p in empty_cells(board):
            board[p] = 'X'

            x, score = minimax(board, depth-1, False)
            board[p] = ''
            if score > value:
                value = score
                pos = p

    else:
        value = +10000
        for p in empty_cells(board):
            board[p] = 'O'

            x,score = minimax(board, depth-1, True)
            board[p] = ''
            if score < value:
                value = score
                pos = p
    return pos, value

######################### MAIN #########################
player = 'O'

while True:
    draw(game_board)
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break

    flag = False # 사용자가 올바른 번호를 선택했는지에 대한 flag
    while not flag:
        if(player == 'O'): # 사용자 입력
            i = int(input('\n번호를 선택하시오 : '))
        else: # 컴퓨터 입력
            i, v = minimax(game_board, 9, player=='X')

        flag = move(i, player)
        if flag == False:
            print('\n이미 선택된 번호입니다.\n')

    if player== 'X':
        player = 'O'
    else:
        player = 'X'

if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')
