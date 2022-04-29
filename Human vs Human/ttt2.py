""" Tic Tac Toe Game Usuing Python"""

"""importing datetime ,Timer and random"""
import datetime
import imp
import random
import time
from tkinter import *
from tkinter import messagebox
from gui2 import *
import threading
import os

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
        self.GuiBoard = Gui()
        self.GuiBoard.root.update()
        self.mBoardSize = boardSize
        self.mNumberOfPlayers = numberOfPlayers
        self.mTurn = None
        self.mBestMove = 0
        self.TossA_coin()


    """this function decide who is starting the game by coin flip,
            if the computer won it choose random Move for the first move"""
    def TossA_coin(self):
        turn = random.choice(['player1', 'player2'])
        print("Desiding First Chance by Fliping Coin\n")
        if turn == 'player1':
            print("Player1 had won the Toss\n")
            messagebox.showinfo("Player1 had won the Toss")
            self.mTurn = 0
            self.GuiBoard.player1Turn =True
        else:
            print("Player2 had won the Toss\n")
            messagebox.showinfo("Player2 had won the Toss \n")
            self.mTurn = 1



         
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

        if self.mBoard.all_same(self.mBoard.getRow(row), char) or self.mBoard.all_same(self.mBoard.getColumn(col), char):
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
        def timeOut():
            messagebox.showinfo("Game Over OPPONENT WON: Out of time")
            print("Game Over OPPONENT WON: Out of time!")
            self.GuiBoard.root.destroy()
        
        while True:
            self.GuiBoard.root.update()
            self.mBoard.printTTTBoard()
            self.mTurn %= 2
            afterTask = self.GuiBoard.root.after(5000, lambda: timeOut())
            if self.mTurn % 2 == 0:
                while self.GuiBoard.p1Clicked ==False:
                    print("Player 1 Turn ")
                    self.GuiBoard.root.update()
                else:
                    position = str(self.GuiBoard.lastClicked)[8:]
                    if position =='':
                        x=0
                    else:
                        x=int(position)-1
                    self.mBoard.draw(x,'X')
                    self.GuiBoard.root.update()

                self.GuiBoard.p1Clicked = False
                self.GuiBoard.root.after_cancel(afterTask)

            elif self.mTurn % 2 == 1 :
                while self.GuiBoard.p2Clicked  ==False:
                    print("Player 2 Turn ")
                    self.GuiBoard.root.update()
                else:
                    position = str(self.GuiBoard.lastClicked)[8:]
                    if position =='':
                        x=0
                    else:
                        x=int(position)-1
                    self.mBoard.draw(x,'O')
                    self.GuiBoard.root.update()
                
                self.GuiBoard.p2Clicked = False
                self.GuiBoard.root.after_cancel(afterTask)
            
            gameResult = self.check_Game_State()
            if gameResult != 'notEnd':
                self.mBoard.printTTTBoard()
                if gameResult == 'Tie':
                    messagebox.showinfo("This game was a tie")
                    print('The game is tie')
                else:
                    if self.mTurn % 2 == 0:
                        messagebox.showinfo("Player 1 is the winner")
                        print('Player1 won the game')
                    else:
                        messagebox.showinfo("Player2 is the winner!!")
                        print('Player2 is the winner!!')

                break

            self.mTurn += 1

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




