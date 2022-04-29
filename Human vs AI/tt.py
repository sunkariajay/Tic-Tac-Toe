""" Tic Tac Toe Game Usuing Python"""

"""importing datetime ,Timer and random"""
import datetime
import imp
import random
import time
from tkinter import *
from tkinter import messagebox
from gui import *

"""defining Constants"""
EMPTY = " "
TIME =5

"""exception class, in case the user entered a none empty position"""
class NoneEmptyPosition(Exception):
    pass

"""exception class, in case the user entered number higher the board positions"""
class OutOfRange(Exception):
    pass


"""Tic Tac Toe Board Class to manage the actvity in board"""
class TTTBoard:
    """
        constructor which takes size as input and create a Tic Tac Toe board of size*size 
        """
    def __init__(self, size):
        self.mSize = size
        self.mBoard = [[EMPTY for x in range(size)] for y in range(size)]
        self.lastMove = None

    """this function prints the game board"""
    def printTTTBoard(self):
        for i in range(self.mSize):  # outer loop to print row
            for j in range(self.mSize):  # inner loop to print column
                if j < self.mSize-1:
                    print(self.mBoard[i][j], end='|')
                else:
                    print(self.mBoard[i][j], end='')
            print()

    """getBoardPosition function gets position (0-24) and convert it to a board position and return the match row and column"""
    def getBoardPosition(self,position):
        y = position%self.mSize
        x = position//self.mSize
        return x,y

    """this function return the last move on the board"""
    def getLastMove(self):
        return self.lastMove

    """this function gets row number in the board and return the match row"""
    def getRow(self, rowNum):
        return self.mBoard[rowNum]

    """this function gets column number in the board and return the match column"""
    def getColumn(self, ColumnNum):
        return [row[ColumnNum] for row in self.mBoard]

    """this function return the main diagonal of the board, left to right"""
    def getMainDiagonal(self):
        return [self.mBoard[i][i] for i in range(self.mSize)]

    """this function return the secondary diagonal of the board, right to left"""
    def getSecondaryDiagonal(self):
        diagonal = []
        j = 0
        for i in reversed(range(self.mSize)):
            diagonal.append(self.mBoard[i][j])
            j += 1
        return diagonal

    """this function return the diagonals of the board"""
    def getDiagonal(self):
        mainDiagonal = self.getMainDiagonal()
        secondDiagonal = self.getSecondaryDiagonal()
        return mainDiagonal,secondDiagonal

    """this function gets position and checking if the position is on the main/secondary diagonal or not"""
    def checkIfOnDiagonal(self, position,type):
        if(type=='Secondary'):
            return position % (self.mSize - 1) == 0
        else:
            return position % (self.mSize + 1) == 0
   
    """this function gets position and draw '_' on the match place on the board"""
    def drawEmpty(self, position):
        (row, column) = self.getBoardPosition(position)
        self.mBoard[row][column] = EMPTY

    """this function gets position and draw 'O' if player ='O' else 'X' on the match place on the board"""
    def draw(self, position,player):
        self.lastMove = position
        (row, column) =  self.getBoardPosition(position)
        self.mBoard[row][column] = player




    """this function gets position and checking if it empty"""
    def isBoardPositionEmpty(self, position):
        (row, column) = self.getBoardPosition(position)
        return self.mBoard[row][column] == EMPTY

    """this function gets 2 arguments:  listToBeChecked - line in the board 
            char - 'X' or 'Y' and checking if all the line filled with it"""
    def all_same(self, listToBeChecked, char):
        return all(x == char for x in listToBeChecked)


""" Game Class """

class Game:
    """the constructor gets 2 arguments: numberOfPlayers, board size
        also, mNamesList - store the names of the players
        mTurn - says who have the turn to play, even -player1, odd - player2
        mComputerFirstPosition - store the random position of the computer"""

    def __init__(self, numberOfPlayers, boardSize):
        self.mBoard = TTTBoard(boardSize)
        self.GuiBoard =Gui()
        self.GuiBoard.root.update()
        self.mBoardSize = boardSize
        self.mNumberOfPlayers = numberOfPlayers
        self.mTurn = None
        self.mComputerFirstPosition = None
        self.mBestMove = 0
        self.TossA_coin()


    """this function decide who is starting the game by coin flip,
            if the computer won it choose random Move for the first move"""
    def TossA_coin(self):
        turn = random.choice(['player', 'player'])
        print("Desiding First Chance by Fliping Coin\n")
        if turn == 'computer':
            print("Computer had won the Toss\n")
            messagebox.showinfo("Computer had won the Toss")
            self.mComputerFirstPosition = random.randrange(self.mBoard.mSize ** 2)
            self.mTurn = 1
            
        else:
            messagebox.showinfo("You had won the Toss")
            print("You had won the Toss \n")
            self.mTurn = 0


         
    """this function gets the player move from the user"""
    def getPlayerMove(self):
        return 3
        

    """ this function gets a player turn and check if the player won
        based on his last move, it checking every line which including the last move"""
    def check_For_Win(self, turn):
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

        if self.mBoard.checkIfOnDiagonal(lastMove,"Main"):
            if self.mBoard.all_same(self.mBoard.getMainDiagonal(), char):
                return True

        if self.mBoard.checkIfOnDiagonal(lastMove,"Secondary"):
            if self.mBoard.all_same(self.mBoard.getSecondaryDiagonal(), char):
                return True

        return False

    """this function check if the game is tie, which means the board is filled and there is no winner"""
    def checkForTie(self):
        for i in range(self.mBoard.mSize ** 2):
            if self.mBoard.isBoardPositionEmpty(i):
                return False
        return True

    """this function compute all the valid moves on the game board and return them"""
    def genrateAllValidMove(self):
        possibleMoves = []
        for i in range(self.mBoard.mSize ** 2):
            if self.mBoard.isBoardPositionEmpty(i):
                possibleMoves.append(i)
        return possibleMoves

    """this function check the game state and return it"""
    def check_Game_State(self):
        if self.check_For_Win(0):
            return 'X'

        if self.check_For_Win(1):
            return 'O'

        if self.checkForTie():
            return "Tie"

        return 'notEnd'

    """ this function is starting the game and managing it until it over"""
    def startGame(self):
        while True:
            self.GuiBoard.root.update()
            if self.GuiBoard.start ==True:
                self.GuiBoard.root.update()
                self.mBoard.printTTTBoard()
                self.mTurn %= 2
                if self.mTurn % 2 == 0:
                    print("Your Turn !!! waiting for 5 seconds")
                    time.sleep(5)
                    self.GuiBoard.root.update()
                    if self.GuiBoard.clicked == False:
                        messagebox.showinfo("Game over AIwon, time out .")
                        exit()
                    else:                    
                        
                        position = str(self.GuiBoard.lastClicked)[8:]
                        if position =='':
                            x=0
                        else:
                            x=int(position)-1
                        self.mBoard.draw(x,'X')
                        self.GuiBoard.computerTurn =True
                        self.GuiBoard.clicked =False
                        self.GuiBoard.root.update()
                    
                elif self.mTurn % 2 == 1 and self.GuiBoard.computerTurn==True:
                    self.GuiBoard.computerTurn=False
                    print('computer is selecting rubic')
                    
                    if self.mComputerFirstPosition is not None:
                        computerMove = self.mComputerFirstPosition
                        self.mComputerFirstPosition = None
                    else:
                        computerMove = self.iterative_Deep_Search()
                    self.mBoard.draw(computerMove,'O')
                    
                    pos = self.GuiBoard.list[computerMove]
                    self.GuiBoard.drawOnBoard(pos,'O')
                    self.GuiBoard.root.update()

            else:
                continue
            
            gameResult = self.check_Game_State()
            if gameResult != 'notEnd':
                self.mBoard.printTTTBoard()
                if gameResult == 'Tie':
                    messagebox.showinfo("This game was a tie")
                    print('The game is tie')
                else:
                    if self.mTurn % 2 == 0:
                        messagebox.showinfo("Congrulations!! you won the game")
                        print('Congrulations!! you won the game')
                    else:
                        messagebox.showinfo("computer is the winner!!")
                        print('computer is the winner!!')

                        
                break

            self.mTurn += 1

    """ this function gets 6 arguments: depth - the depth of the game tree
        beta - store the best value for the minimizer
        startTime - the time we started the search
        timeLimit - the time we will search for the best move
        the function tells if the moves I take is better or worse by compute the best score
        and position in the given depth, than it return them
        isMax - tell which side are we, the maximizer or the minimizer
        alpha - store the best value for the maximizer
        I used minmax algorithm with alpha beta pruning"""
    def minmax2(self, depth, isMax, alpha, beta, startTime, timeLimit):

        moves = self.genrateAllValidMove()
        score = self.evaluateGameBoard()
        position = None

        if datetime.datetime.now() - startTime >= timeLimit:
            self.mTimePassed = True

        if not moves or depth == 0 or self.mTimePassed:
            gameResult = self.check_Game_State()
            if gameResult == 'X':
                return -10**(self.mBoard.mSize+1), position
            elif gameResult == 'O':
                return 10**(self.mBoard.mSize+1), position
            elif gameResult == 'Tie':
                return 0, position

            return score, position

        if isMax:
            for i in moves:
                    self.mBoard.draw(i,'O')
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
                self.mBoard.draw(i,'X')
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
    def iterative_Deep_Search(self):
        startTime = datetime.datetime.now()
        endTime = startTime + datetime.timedelta(0,TIME)
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
    def calculateLine(self, line):
        oSum = line.count('O')
        xSum = line.count('X')
        EmptySum = line.count(EMPTY)
        return oSum, xSum, EmptySum

    """this function gets a board line and calculate it score"""
    def CalculateScoreLine(self, line):
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
    def evaluateGameBoard(self):
        score = 0
        for i in range(self.mBoard.mSize):
            score += self.CalculateScoreLine(self.mBoard.getRow(i))
            score += self.CalculateScoreLine(self.mBoard.getColumn(i))

        diagonals = self.mBoard.getDiagonal()
        for i in range(2):
            score += self.CalculateScoreLine(diagonals[i])
        return score


game = Game(1, 5)
game.startGame()




