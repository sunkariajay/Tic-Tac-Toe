from tkinter import *
from tkinter import messagebox


class Gui:
    """
        constructor which takes size as input and create a Tic Tac Toe board of size*size 
        """
    def __init__(self):
        self.root =Tk()
        self.root.title("Tic-Tac-Toe")
        self.player1Turn =False
        self.p1Clicked =False
        self.p2Clicked =False
        self.lastClicked =None
        self.b1 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b1))
        self.b2 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b2))
        self.b3 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b3))
        self.b4 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b4))
        self.b5 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b5))
        self.b6 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b6))
        self.b7 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b7))
        self.b8 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b8))
        self.b9 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b9))
        self.b10 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b10))
        self.b11 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b11))
        self.b12 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b12))
        self.b13 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b13))
        self.b14 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b14))
        self.b15 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b15))
        self.b16 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b16))
        self.b17 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b17))
        self.b18 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b18))
        self.b19 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b19))
        self.b20 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b20))
        self.b21 = Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b21))
        self.b22= Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b22))
        self.b23= Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b23))
        self.b24= Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b24))
        self.b25= Button(self.root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:self.drawOnBoard(self.b25))

        self.b1.grid(row=0,column=0)
        self.b2.grid(row=0,column=1)
        self.b3.grid(row=0,column=2)
        self.b4.grid(row=0,column=3)
        self.b5.grid(row=0,column=4)

        self.b6.grid(row=1,column=0)
        self.b7.grid(row=1,column=1)
        self.b8.grid(row=1,column=2)
        self.b9.grid(row=1,column=3)
        self.b10.grid(row=1,column=4)

        self.b11.grid(row=2,column=0)
        self.b12.grid(row=2,column=1)
        self.b13.grid(row=2,column=2)
        self.b14.grid(row=2,column=3)
        self.b15.grid(row=2,column=4)

        self.b16.grid(row=3,column=0)
        self.b17.grid(row=3,column=1)
        self.b18.grid(row=3,column=2)
        self.b19.grid(row=3,column=3)
        self.b20.grid(row=3,column=4)

        self.b21.grid(row=4,column=0)
        self.b22.grid(row=4,column=1)
        self.b23.grid(row=4,column=2)
        self.b24.grid(row=4,column=3)
        self.b25.grid(row=4,column=4)
        

        self.list =[
            self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9,self.b10,
            self.b11,self.b12,self.b13,self.b14,self.b15,self.b16,self.b17,self.b18,self.b19,self.b20,
            self.b21,self.b22,self.b23,self.b24,self.b25
            ]
                    
    def drawOnBoard(self,b):
        if b["text"]==" ":
            self.lastClicked = b
            if(self.player1Turn==True and self.p1Clicked ==False):
                self.player1Turn =False
                self.p1Clicked=True
                b["text"] = "X"
            elif (self.player1Turn==False and self.p2Clicked ==False):
                self.player1Turn =True
                self.p2Clicked=True
                b["text"] = "O"
            
        else:
            msg = "This node is \n already taken"
            messagebox.showerror(msg)

        