import numpy as nmpy #module importing as nmpy
import random #module importing
from gui import *
from time import sleep as slp #module importing as slp
while(1): #starting a while loop
    g=int(input('''ENTER
            1: for ai vs ai 
            \n'''))
    if g==1: #condition checking
        def create_b_d(): #function defining
            return(nmpy.array([[0, 0, 0,0,0],
                            [0, 0, 0,0,0],
                            [0, 0, 0,0,0],
                            [0, 0, 0,0,0],
                            [0, 0, 0,0,0]]))

        # Check for empty places on b_d
        def pss_bl(b_d): #function defining
            l = []
            
            for i in range(len(b_d)):#starting loop
                for j in range(len(b_d)): #starting loop
                    
                    if b_d[i][j] == 0:
                        l.append((i, j))
            return(l)

        # Select a random place for the p_hm
        def random_place(b_d, p_hm): #function defining
            s_lc = pss_bl(b_d)
            cnt_loc = random.choice(s_lc)
            b_d[cnt_loc] = p_hm
            return(b_d)

        # Checks whether the p_hm has three
        # of their marks in a horizontal row
        def row_w_n(b_d, p_hm): #function defining
            for x_1 in range(len(b_d)): #starting loop
                w_n = True
                
                for y in range(len(b_d)): #starting loop
                    if b_d[x_1, y] != p_hm:
                        w_n = False
                        continue
                        
                if w_n == True: #condition checking
                    return(w_n)
            return(w_n)

        # Checks whether the p_hm has three
        # of their marks in a vertical row
        def col_w_n(b_d, p_hm): #function defining
            for x_1 in range(len(b_d)): #starting loop
                w_n = True
                
                for y_1 in range(len(b_d)): #starting loop
                    if b_d[y_1][x_1] != p_hm: #condition checking
                        w_n = False
                        continue
                        
                if w_n == True: #condition checking
                    return(w_n)
            return(w_n)

        # Checks whether the p_hm has three
        # of their marks in a diagonal row
        def diag_w_n(b_d, p_hm): #function defining
            w_n = True
            y_1 = 0
            for x_1 in range(len(b_d)): #starting loop
                if b_d[x_1, x_1] != p_hm: #condition checking
                    w_n = False
            if w_n: #condition checking
                return w_n
            w_n = True
            if w_n: #condition checking
                for x_1 in range(len(b_d)): #starting loop
                    y_1 = len(b_d) - 1 - x_1
                    if b_d[x_1, y_1] != p_hm: #condition checking
                        w_n = False
            return w_n

        # Evaluates whether there is
        # a vctor_y or a tie
        def evaluate(b_d): #function defining
            vctor_y = 0
            
            for p_hm in [5,7 ]:#starting loop
                if (row_w_n(b_d, p_hm) or
                    col_w_n(b_d,p_hm) or
                    diag_w_n(b_d,p_hm)): #condition checking
                        
                    vctor_y = p_hm
                    
            if nmpy.all(b_d != 0) and vctor_y == 0: #condition checking
                vctor_y = str("its a draw")
            return vctor_y

        # Main function to start the game
        def st_ply_game(): #function defining
            b_d, vctor_y, ctd = create_b_d(), 0, 1
            print(b_d)
            slp(2)
            
            while vctor_y == 0: #starting loop
                for p_hm in [5, 9]: #starting loop
                    b_d = random_place(b_d, p_hm)
                    print(f"board after {str(ctd)}  move")
                    print(b_d)
                    slp(2)
                    ctd += 1
                    vctor_y = evaluate(b_d)
                    if vctor_y != 0:
                        break
            return(vctor_y)
        
        # Driver Code
        print("winner is: " + str(st_ply_game()))
    elif g==2:
       

        from enum import Enum #module importing
        import datetime #module importing
        import random #module importing

        """Constants"""
        hman = 'X'
        A_I = 'O'
        EMPTY = '_'
        BOARD_SIZE = 5
        NUMBER_OF_hmanS = 1
        SEARCH_TIME = 5

        """exception class, in case the user entered a none empty position"""

        class NoneEmptyPosition(Exception): 
            pass


        """exception class, in case the user entered number higher the board positions"""


        class OutOfRange(Exception): 
            pass

        """ enum for game state"""

        class GameState(Enum):
            tie = 'Tie'
            notEnd = 'notEnd'
            o = 'O'  # A_I won
            x = 'X'  # hman won


        """
        this class managing the board game activities
        """


        class Board:

            """
                the constructor gets 1 argumnet size - the size of the board
                it initialized the game board to be empty board (size x size)
                and store the last move which been made in order to decide who won
                """
            def __init__(self, size): #function defining
                self.mSize = size
                self.mBoard = [[EMPTY for x in range(size)] for y in range(size)]
                self.lastMove = None

            """this function prints the game board"""
            def print(self): #function defining
                for i in range(self.mSize):
                    for j in range(self.mSize):
                        if j < self.mSize-1:
                            print(self.mBoard[i][j], end='|')
                        else:
                            print(self.mBoard[i][j], end='')
                    print()

            """this function gets position 0 - size x size
                    and convert it to a board position
                    and return the match row and column"""
            def getBoardPosition(self,position): #function defining
                column = position%self.mSize
                row = position//self.mSize
                return row, column

            """this function return the last move on the board"""
            def getLastMove(self): #function defining
                return self.lastMove

            """this function gets number of row in the board and return the match row"""
            def getRow(self, numberOfRow): #function defining
                return self.mBoard[numberOfRow]

            """this function gets number of column in the board and return the match column"""
            def getColumn(self, numberOFColumn): #function defining
                return [row[numberOFColumn] for row in self.mBoard]

            """this function return the diagonals of the board"""
            def getDiagonal(self): #function defining
                diagonal1 = [self.mBoard[i][i] for i in range(self.mSize)]
                diagonal2 = []
                j = 0
                for i in reversed(range(self.mSize)):
                    diagonal2.append(self.mBoard[i][j])
                    j += 1
                return diagonal1, diagonal2

            """this function return the main diagonal of the board, left to right"""
            def getMainDiagonal(self): #function defining
                return [self.mBoard[i][i] for i in range(self.mSize)]

            """this function return the secondary diagonal of the board, right to left"""
            def getSecondaryDiagonal(self): #function defining
                diagonal = []
                j = 0;
                for i in reversed(range(self.mSize)):
                    diagonal.append(self.mBoard[i][j])
                    j += 1
                return diagonal

            """this function gets position and checking if the position is on the main diagonal"""
            def checkIfOnMainDiagonal(self, position): #function defining
                return position % (self.mSize + 1) == 0

            """this function gets position and checking if the position is on the secondary diagonal"""
            def checkIfOnSecondaryDiagonal(self, position): #function defining
                return position % (self.mSize - 1) == 0

            """this function gets position and draw 'X' on the match place on the board"""
            def drawX(self, position): #function defining
                self.lastMove = position
                (row, column) = self.getBoardPosition(position)
                self.mBoard[row][column] = hman

            """this function gets position and draw '_' on the match place on the board"""
            def drawEmpty(self, position): #function defining
                (row, column) = self.getBoardPosition(position)
                self.mBoard[row][column] = EMPTY

            """this function gets position and draw 'O' on the match place on the board"""
            def drawO(self, position): #function defining
                self.lastMove = position
                (row, column) =  self.getBoardPosition(position)
                self.mBoard[row][column] = A_I

            """this function gets position and checking if it empty"""
            def checkIfRubricEmpty(self, position): #function defining
                (row, column) = self.getBoardPosition(position)
                return self.mBoard[row][column] == EMPTY

            """this function gets 2 arguments:  listToBeChecked - line in the board 
                    char - 'X' or 'Y' and checking if all the line filled with it"""
            def all_same(self, listToBeChecked, char): #function defining
                return all(x == char for x in listToBeChecked)


        """this class handling all the game Activities"""


        class Game:
            """the constructor gets 2 arguments: numberOfhmans, board size
                also, mNamesList - store the names of the hmans
                mTurn - says who have the turn to play, even -hman1, odd - hman2
                mA_IFirstPosition - store the random position of the A_I"""

            def __init__(self, numberOfhmans, boardSize): #function defining
                self.mBoard = Board(boardSize)
                self.mBoardSize = boardSize
                self.mNumberOfhmans = numberOfhmans
                self.mNamesList = [' ']*numberOfhmans
                self.mTurn = None
                self.mA_IFirstPosition = None
                self.coinFlip()
                self.mBestMove = 0


            """this function decide who is starting the game by coin flip,
                    if the A_I won it choose random Move for the first move"""
            def coinFlip(self): #function defining
                turn = random.choice(['A_I', 'hman'])
                if turn == 'A_I':
                    self.mA_IFirstPosition = random.randrange(self.mBoard.mSize ** 2)
                    self.mTurn = 1
                else:
                    self.mTurn = 0

            """this function gets the hmans names and stored them"""
            def gethmansNames(self):
                counter = 1
                while counter <= self.mNumberOfhmans:
                    try:
                        hmanName = input('please enter your name::')
                        if not hmanName:
                            raise ValueError("field cannot be empty, please enter name")
                        if not hmanName.isalpha():
                            raise ValueError("only letters are allowed")
                        if hmanName in self.mNamesList:
                            raise ValueError("name already chosen please choose different name")

                        self.mNamesList[counter - 1] = hmanName
                        counter += 1
                    except ValueError as e:
                        print(e)
                    except Exception:
                        print("unknown error")


            """this function gets the hman move from the user"""
            def gethmanMove(self):
                while True:
                    try:
                        hmanMove = int(input(self.mNamesList[self.mTurn] + ' please select position '))-1
                        if not (0 <= hmanMove <= (self.mBoardSize ** 2 - 1)):
                            raise OutOfRange("Wrong position, please choose position 0 - " + str(self.mBoardSize ** 2 - 1))

                        if not self.mBoard.checkIfRubricEmpty(hmanMove):
                            raise NoneEmptyPosition("position already filled please try again!")
                        return hmanMove

                    except (OutOfRange, NoneEmptyPosition) as e:
                        print(e)
                    except ValueError as e:
                        print("only numbers are allowed")
                    except Exception:
                        print("unknown error")

            """ this function gets a hman turn and check if the hman won
                based on his last move, it checking every line which including the last move"""
            def checkForWin(self, turn):
                char = ''
                if turn % 2 == 0:
                    char = 'X'
                else:
                    char = 'O'
                lastMove = self.mBoard.getLastMove()
                row, col = self.mBoard.getBoardPosition(lastMove)

                if self.mBoard.all_same(self.mBoard.getRow(row), char) or \
                        self.mBoard.all_same(self.mBoard.getColumn(col), char):
                    return True

                if self.mBoard.checkIfOnMainDiagonal(lastMove):
                    if self.mBoard.all_same(self.mBoard.getMainDiagonal(), char):
                        return True

                if self.mBoard.checkIfOnSecondaryDiagonal(lastMove):
                    if self.mBoard.all_same(self.mBoard.getSecondaryDiagonal(), char):
                        return True

                return False

            """this function check if the game is tie, which means the board is filled and there is no winner"""
            def checkForTie(self):  #function defining
                for i in range(self.mBoard.mSize ** 2):
                    if self.mBoard.checkIfRubricEmpty(i):
                        return False
                return True

            """this function compute all the valid moves on the game board and return them"""
            def genrate(self): #function defining
                possibleMoves = []
                for i in range(self.mBoard.mSize ** 2):
                    if self.mBoard.checkIfRubricEmpty(i):
                        possibleMoves.append(i)
                return possibleMoves

            """this function check the game state and return it"""
            def checkGameState(self):  #function defining
                if self.checkForWin(0):
                    return GameState.x

                if self.checkForWin(1):
                    return GameState.o

                if self.checkForTie():
                    return GameState.tie

                return GameState.notEnd

            """ this function is starting the game and managing it until it over"""
            def start(self):  #function defining
                self.gethmansNames()
                while True:
                    self.mBoard.print()
                    self.mTurn %= 2
                    if self.mTurn % 2 == 0:
                        hmanMove = self.gethmanMove()
                        self.mBoard.drawX(hmanMove)
                    else:
                        print('AI choosing:')
                        if self.mA_IFirstPosition is not None:
                            A_IMove = self.mA_IFirstPosition
                            self.mA_IFirstPosition = None
                        else:
                            A_IMove = self.iterativeDeepSearch()

                        self.mBoard.drawO(A_IMove)

                    gameResult = self.checkGameState()
                    if gameResult.value != 'notEnd':
                        self.mBoard.print()
                        if gameResult.value == 'Tie':
                            print('The game is tie')
                        else:
                            if self.mTurn % 2 == 0:
                                print(self.mNamesList[self.mTurn] + 'is the winner!')
                            else:
                                print('A_I is the winner!')
                        break

                    self.mTurn += 1

            """ this function gets 6 arguments: depth - the depth of the game tree
                isMax - tell which side are we, the maximizer or the minimizer
                alpha - store the best value for the maximizer
                beta - store the best value for the minimizer
                startTime - the time we started the search
                timeLimit - the time we will search for the best move
                the function tells if the moves I take is better or worse by compute the best score
                and position in the given depth, than it return them
                I used minmax algorithm with alpha beta pruning"""
            def minmax2(self, depth, isMax, alpha, beta, startTime, timeLimit):  #function defining

                moves = self.genrate()
                score = self.evaluate()
                position = None

                if datetime.datetime.now() - startTime >= timeLimit:
                    self.mTimePassed = True

                if not moves or depth == 0 or self.mTimePassed:
                    gameResult = self.checkGameState()
                    if gameResult.value == 'X':
                        return -10**(self.mBoard.mSize+1), position
                    elif gameResult.value == 'O':
                        return 10**(self.mBoard.mSize+1), position
                    elif gameResult.value == 'Tie':
                        return 0, position

                    return score, position

                if isMax:
                    for i in moves:
                            self.mBoard.drawO(i)
                            score, dummy = self.minmax2(depth-1, not isMax, alpha, beta, startTime, timeLimit)
                            if score > alpha:
                                alpha = score
                                position = i
                                self.mBestMove = i

                            self.mBoard.drawEmpty(i)
                            if beta <= alpha:
                                break

                    return alpha, position
                else:
                    for i in moves:
                        self.mBoard.drawX(i)
                        score, dummy = self.minmax2(depth-1, not isMax, alpha, beta, startTime, timeLimit)
                        if score < beta:
                            beta = score
                            position = i
                            self.mBestMove = i
                        self.mBoard.drawEmpty(i)
                        if alpha >= beta:
                            break

                    return beta, position

            """this function search the best move it find in 5 seconds.
            The function goes as deep as possible in 5 second in the game tree
            and return the best move"""
            def iterativeDeepSearch(self):  #function defining
                startTime = datetime.datetime.now()
                endTime = startTime + datetime.timedelta(0, SEARCH_TIME)
                depth = 1
                position = None
                self.mTimePassed = False
                while True:
                    currentTime = datetime.datetime.now()
                    if currentTime >= endTime:
                        break
                    best, position = self.minmax2(depth, True, -10000000, 10000000, currentTime, endTime-currentTime)
                    depth += 1

                if position is None:
                    position = self.mBestMove

                return position

            """this function gets a board line and calculate how many
                'X', 'O' and empty rubrics"""
            def calculateLine(self, line):  #function defining
                oSum = line.count(A_I)
                xSum = line.count(hman)
                EmptySum = line.count(EMPTY)
                return oSum, xSum, EmptySum

            """this function gets a board line and calculate it score"""
            def getScoreLine(self, line):  #function defining
                score = 0
                oSum, xSum, EmptySum = self.calculateLine(line)
                if xSum == 0 and oSum != 0:
                    if oSum == self.mBoard.mSize:
                        score += 11 ** (oSum - 1)
                    score += 10 ** (oSum - 1)
                if oSum == 0 and xSum != 0:
                    score += -(10 ** (xSum - 1))
                return score

            """this function evaluate the game board and return the score"""
            def evaluate(self):  #function defining
                score = 0
                for i in range(self.mBoard.mSize):
                    score += self.getScoreLine(self.mBoard.getRow(i))
                    score += self.getScoreLine(self.mBoard.getColumn(i))

                diagonals = self.mBoard.getDiagonal()
                for i in range(2):
                    score += self.getScoreLine(diagonals[i])
                return score


        game = Game(NUMBER_OF_hmanS, BOARD_SIZE)
        game.start()





    elif g==3: #condition checking
        exit()
    else:
        print("print 1 or 2")
        continue