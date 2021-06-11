# 상태 클래스 정의
class State:
    def __init__(self, board, goal, moves = 0):
        self.board = board
        self.moves = moves
        self.goal = goal

    def expand(self, moves):
        result = []
        i = self.board.index(0) # 숫자 0의 위치
        if not i in [0,1,2,3]: # UP
            result.append(self.get_new_board(i, i-4, moves))
        if not i in [0,4,8,12]: # LEFT
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [3,7,11,15]: # RIGHT
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [12,13,14,15]: # DOWN
            result.append(self.get_new_board(i, i+4, moves))
        return result

    # i1, i2를 교환한 후 상태 반환
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    # 객체 출력
    def __str__(self):
        return str(self.board[:4]) + "\n" + \
        str(self.board[4:8]) + "\n" + \
        str(self.board[8:12]) + "\n" + \
        str(self.board[12:]) + "\n" + \
        "--------------------"

# 현재 상태
puzzle = [1,2,3,4,
          5,6,0,7,
          8,9,10,11,
          12,13,14,15]

# 목표 상태
goal = [1,2,0,4,
        5,6,3,7,
        8,9,10,11,
        12,13,14,15]

# open, closed 리스트
open = []
open.append(State(puzzle,goal))

closed = []
moves = 0
while len(open) != 0:
    current = open.pop(0) # open 리스트의 앞에서 삭제
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    moves = current.moves + 1
    closed.append(current)
    for state in current.expand(moves):
        if(state in closed) or (state in open): # 이미 거쳐간 노드이면
            continue # 노드 버림
        else:
            open.append(state) # open 리스트 끝에 추가


