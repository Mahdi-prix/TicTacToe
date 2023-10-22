
class TicTacToe:
    def player(self, state):                         #who will start the game/sıranın kimde olduğunu belirtiyor
        x_count = sum(row.count('X') for row in state)
        o_count = sum(row.count('O') for row in state)
        return 'X' if x_count <= o_count else 'O'

    def actions(self, state):               #all possible actions that can occur/gerçekleşebilecek tüm olası eylemler
        possible_actions = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    possible_actions.append((i+1, j+1))
        return possible_actions

    def result(self, state, action):                #achieves new status by adding actions to the ex board/varsayılan tahta üzerine eylemler ekliyerek yeni durum elde eder
        i, j = action
        player = self.player(state)
        new_state = [row.copy() for row in state]
        new_state[i-1][j-1] = player
        return new_state

    def winner(self, board):                #oyunu kazanan var mi/any player win
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]
        return None

    def terminal(self, board):              #If there is no winner or the game is not over, continue the game/kazanan yoksa veya oyun bitmediyse oyuna devam edilsin
        if self.winner(board) is not None:
            return True
        return all(board[i][j] != ' ' for i in range(3) for j in range(3))

    def utility(self, terminal_board):              #Define the concepts of win, lose and draw for players/kazanmak, kaybetmek ve berabere kalmak kavramlarını tanımlak
        winner = self.winner(terminal_board)
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        return 0

    def minimax(self, board):                #mechanism of making moves by looking at the consequences that may arise as a result of the moves to be made/yapılacak hamlelerin sonucunda ortaya çıkabilen sonuçlara bakarak hamle yapma mekanizması
        def max_value(state):
            if self.terminal(state):
                return self.utility(state)
            v = float('-inf')
            for action in self.actions(state):
                v = max(v, min_value(self.result(state, action)))
            return v

        def min_value(state):
            if self.terminal(state):
                return self.utility(state)
            v = float('inf')
            for action in self.actions(state):
                v = min(v, max_value(self.result(state, action)))
            return v

        if self.terminal(board):
            return None

        best_action = None
        if self.player(board) == 'X':
            v = float('-inf')
            for action in self.actions(board):
                temp_v = min_value(self.result(board, action))
                if temp_v > v:
                    v = temp_v
                    best_action = action
        else:
            v = float('inf')
            for action in self.actions(board):
                temp_v = max_value(self.result(board, action))
                if temp_v < v:
                    v = temp_v
                    best_action = action

        return best_action




