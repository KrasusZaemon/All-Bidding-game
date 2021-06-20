from Algorithm import Unifom
from sys import argv
import tkinter as tk

import tkinter.messagebox
import random
from tkinter.constants import NO
from tkinter import Canvas, Scale, ttk
from Algorithm import *

rounds = 0
round_player1 = 0
round_player2 = 0
canvas = None
image_file = None
image_file1 = None
image = None
image1 =None
Money_p1, Money_p2 =None,None
Money_to_place,Money_to_place_2 = None,None
label_player1,label_player2 =None,None
choosen = 0
Player1_m,Player2_m = 0,0
label_player11,label_player22=None,None
label_val_q, r3, r4 = None,None,None
cmb,entry_player1,entry_player2 =None,None,None
game,homepage,root = None,None,None
def GameStart(event):
    global rounds,image_file,image_file1,image,image1,Money_p1,Money_p2,Money_to_place,canvas
    global label_player1,label_player2,mode_var,Money_to_place_2,root,homepage,Player1_m,Player2_m,label_player11,label_player22

    
    #firstclose.destroy()
    Money_p1 = int(entry_player1.get() )
    Money_p2 = int(entry_player2.get())
    Player1_m,Player2_m = 0,0

    rounds = int(cmb.get())
    homepage.destroy()
    root = tk.Frame(game)
    root.pack()
    
    #Canvas
    canvas  = tk.Canvas(root,bg='pink',height=420,width=800)
    coord = [10, 100, 60, 150]
    canvas.create_line(35+80,125,35+(rounds)*80,125)
    canvas.create_line(35+(rounds)*80,125,35+(rounds+1)*80,225)
    canvas.create_line(35+80,325,35+(rounds)*80,325)
    canvas.create_line(35+(rounds)*80,325,35+(rounds+1)*80,225)
    for i in range(rounds):
        coord[0]+=80
        coord[2]+=80
        canvas.create_oval(coord, fill='white')
    coord[0]+=80
    coord[1]+=100
    coord[2]+=80
    coord[3]+=100
    canvas.create_oval(coord, fill='white')

    coord = [10, 300, 60, 350]
    for i in range(rounds):
        coord[0]+=80
        coord[2]+=80
        canvas.create_oval(coord, fill='white')

    image_file = tk.PhotoImage(file='Player1.gif')
    
    image = canvas.create_image(115, 125, image=image_file)

    image_file1 = tk.PhotoImage(file='Player2.gif')
    
    image1 = canvas.create_image(115, 325, image=image_file1)
    canvas.pack()

    if(mode_var.get()==0):
        #第一行文字
        label_val_q = tk.Label(root,font=('Arial', 18),width = "80")
        label_val_q.pack(side = "top")
        label_val_q.config(label_val_q,text = "Please Enter the money Player1 want to place")

        #输入框
        Money_to_place = tk.Entry(root,width = "40")
        Money_to_place.pack()
        Money_to_place.bind('<Return>',StartoneRound)

        label_val_p2 = tk.Label(root,font=('Arial', 18),width = "80")
        label_val_p2.pack(side = "top")
        label_val_p2.config(label_val_p2,text = "Please Enter the money Player2 want to place")

        #输入框
        Money_to_place_2 = tk.Entry(root,width = "40")
        Money_to_place_2.pack()
        Money_to_place_2.bind('<Return>',StartoneRound)

        #下注按键
        btnGuess = tk.Button(root,text = "Place The Bet")
        btnGuess.bind('<Button-1>',StartoneRound)
        btnGuess.pack()
        label_player11 = tk.Label(root,font=('Arial', 12),width = "40")
        label_player11.place(x=-70,y=530,anchor='w')
        label_player11.config(label_player11,text = "Last Place: "+str(Player1_m))
        label_player1 = tk.Label(root,font=('Arial', 12),width = "40")
        label_player1.place(x=-70,y=560,anchor='w')
        label_player1.config(label_player1,text = "Player1's Current Money: "+str(Money_p1))

        label_player22 = tk.Label(root,font=('Arial', 12),width = "40")
        label_player22.place(x=580,y=530,anchor='w')
        label_player22.config(text = "Last Place: "+str(Player2_m))
        label_player2 = tk.Label(root,font=('Arial', 12),width = "40")
        label_player2.place(x=580,y=560,anchor='w')
        label_player2.config(text = "Player2's Current Money: "+str(Money_p2))
    else:
        #第一行文字
        label_val_q = tk.Label(root,font=('Arial', 18),width = "80")
        label_val_q.pack(side = "top")
        label_val_q.config(label_val_q,text = "\nPlease Enter the money you want to place")

        #输入框
        Money_to_place = tk.Entry(root,width = "40")
        Money_to_place.pack()
        Money_to_place.bind('<Return>',StartoneRound)

        #label_val_p2 = tk.Label(root,font=('Arial', 18),width = "80")
        #label_val_p2.pack(side = "top")
        #label_val_p2.config(label_val_p2,text = "Please Enter the money Player2 want to place")

        #输入框
        Money_to_place_2 = tk.Entry(root,width = "40")
        #Money_to_place_2.pack()
        #Money_to_place_2.bind('<Return>',StartoneRound)

        #下注按键
        btnGuess = tk.Button(root,text = "Place The Bet")
        btnGuess.bind('<Button-1>',StartoneRound)
        btnGuess.pack()
    

        label_player11 = tk.Label(root,font=('Arial', 12),width = "40")
        label_player11.place(x=-70,y=530,anchor='w')
        label_player11.config(label_player11,text = "Last Place: "+str(Player1_m))
        label_player1 = tk.Label(root,font=('Arial', 12),width = "40")
        label_player1.place(x=-70,y=550,anchor='w')
        label_player1.config(label_player1,text = "Player1's Current Money: "+str(Money_p1))

        label_player22 = tk.Label(root,font=('Arial', 12),width = "40")
        label_player22.place(x=580,y=530,anchor='w')
        label_player22.config(text = "Last Place: "+str(Player2_m))
        label_player2 = tk.Label(root,font=('Arial', 12),width = "40")
        label_player2.place(x=580,y=550,anchor='w')
        label_player2.config(text = "Player2's Current Money: "+str(Money_p2))

        #退出按键
    def quit(event):
        game.destroy()

    btnClose = tk.Button(root,text = "Quit")
    btnClose.bind('<Button-1>',quit)
    btnClose.pack()

    Money_to_place.focus_get()

    

def StartoneRound(eent):
    global Money_to_place,rounds,round_player1,round_player2,Money_p1,Money_p2,canvas,image,image1
    global label_player1,label_player2,mode_var,Money_to_place_2,homepage,root,game,label_player11,label_player22,Algori_var,type_var
    Player1_m = int(Money_to_place.get())
    if(mode_var.get()==0):
        Player2_m = int(Money_to_place_2.get())
    else:
        if(Algori_var.get()==0):
            Player2_m = Unifom(Money_p2,rounds - round_player2)
        elif(Algori_var.get()==1):
            Player2_m = Random(Money_p2,rounds - round_player2)

    if(Player1_m>Money_p1):
        label_player11.config(text = "Money not Enough, Place again")
        label_player22.config(text = "Stupid enemy, Place again")
        return
    

    if(Player2_m>Money_p2):
        label_player22.config(text = "Money not Enough, Place again")
        label_player11.config(text = "Stupid enemy, Place again")
        return    
    

    if(Player1_m>Player2_m):
        if(type_var.get()==0):
            Money_p1-=Player1_m
            Money_p2-=Player2_m
        elif(type_var.get()==1):
            Money_p1-=Player1_m
            Money_p2+=Player1_m
        elif(type_var.get()==2):
            Money_p1-=Player1_m

        round_player1+=1
        if(round_player1==rounds):
            canvas.move(image,80,100)
        else:
            canvas.move(image,80,0)
    elif(Player2_m>Player1_m):
        if(type_var.get()==0):
            Money_p1-=Player1_m
            Money_p2-=Player2_m
        elif(type_var.get()==1):
            Money_p1+=Player2_m
            Money_p2-=Player2_m
        elif(type_var.get()==2):
            Money_p2-=Player2_m

        round_player2+=1
        if(round_player2==rounds):
            canvas.move(image1,80,-100)
        else:
            canvas.move(image1,80,0)
    label_player1.config(text = "Player1's Current Money: "+str(Money_p1))
    label_player11.config(text = "Last Place: "+str(Player1_m))
    label_player2.config(text = "Player2's Current Money: "+str(Money_p2))
    label_player22.config(text = "Last Place: "+str(Player2_m))
    if(round_player1==rounds):
        print("Player 1 Wins!!")
        tk.messagebox.showinfo(title='Result', message='Player1 Wins！') 
        root.destroy()
        Start()
        pass
    elif(round_player2==rounds):
        print("Player 2 Wins!!")
        tk.messagebox.showinfo(title='Result', message='Player2 Wins！') 
        root.destroy()
        Start()
        pass

    pass


game = tk.Tk(className=" All-Pay Bidding Game")
game.geometry("900x600")
mode_var = tk.IntVar()
Algori_var = tk.IntVar()
type_var = tk.IntVar()


def mode():

    global choosen,mode_var,label_val_q,r3,r4,Algori_var,type_var
    #print('choosen: '+str(choosen))
    #print('mode_var: '+str(mode_var.get()))
    if choosen==0 :

        label_val_q = tk.Label(homepage,font=('Arial', 18),width = "80")
        label_val_q.config(text='Choose the AI You want to play with: ')
        label_val_q.pack()

        
        r3 = tk.Radiobutton(homepage, text='Uniform Algorithm', variable=Algori_var, value=0)
        r3.pack()
        r4 = tk.Radiobutton(homepage, text='Random Algorithm', variable=Algori_var, value=1)
        r4.pack()
        choosen = 1
    if(mode_var.get()==0):
        print("destroy")
        label_val_q.destroy()
        r3.destroy()
        r4.destroy()
        choosen = 0

        
    pass#l.config(text='you have selected ' + var.get())
def PVP_mode():
    pass

def Start():
    global cmb,entry_player1,entry_player2,homepage,rounds,round_player1,round_player2,choosen,mode_var

    rounds = 0
    round_player1 = 0
    round_player2 = 0
    choosen = 0
    homepage = tk.Frame(game)
    homepage.pack()
    label_val_round = tk.Label(homepage,font=('Arial', 18),width = "80")
    label_val_round.config(text='Choose the number of round to Win: ')
    label_val_round.pack()


    cmb = ttk.Combobox(homepage)
    cmb.pack()
    # 设置下拉菜单中的值
    cmb['value'] = (2,3,4,5,6,7)
    cmb.current(2)


    label_val_qp = tk.Label(homepage,font=('Arial', 18),width = "80")
    label_val_qp.config(text='Choose the Mode You want to play: ')
    label_val_qp.pack()

    PVP_mode_button = tk.Radiobutton(homepage, text='Player Vs Player', variable=mode_var, value=0, command=mode)
    PVP_mode_button.pack()
    PVE_mode_button = tk.Radiobutton(homepage, text='Player Vs AI', variable=mode_var, value=1, command=mode)
    PVE_mode_button.pack()

    label_val_game_mode = tk.Label(homepage,font=('Arial', 18),width = "80")
    label_val_game_mode.config(text='Choose the Type of Game You want to play: ')
    label_val_game_mode.pack()

    Poor_mode_button = tk.Radiobutton(homepage, text='All-pay (The bank gets both bids)', variable=type_var, value=0)
    Poor_mode_button.pack()
    Rich_mode_button = tk.Radiobutton(homepage, text='Richman (The loser in this round will get the winner\'s bid)', variable=type_var, value=1)
    Rich_mode_button.pack()
    All_pay_mode_button = tk.Radiobutton(homepage, text='Poorman (The bank only gets the winner\s bid)', variable=type_var, value=2)
    All_pay_mode_button.pack()


    label_val_player1 = tk.Label(homepage,font=('Arial', 18),width = "80")
    label_val_player1.pack()
    label_val_player1.config(text = "Please Enter the money Player1 (you) have:")
    var_player1 = tk.StringVar(value='100')
    entry_player1 = tk.Entry(homepage,width = "40",textvariable=var_player1)
    entry_player1.pack()
    label_val_player2 = tk.Label(homepage,font=('Arial', 18),width = "80")
    label_val_player2.pack()
    label_val_player2.config(text = "Please Enter the money Player2 have:")
    var_player2 = tk.StringVar(value='100')
    entry_player2 = tk.Entry(homepage,width = "40",textvariable=var_player2)
    entry_player2.pack()

    def quit(event):
        game.destroy()
    btnClose = tk.Button(homepage,text = "Quit")
    btnClose.bind('<Button-1>',quit)
    btnClose.pack(side='bottom')
    #退出按键
    firstclose = tk.Button(homepage,text = "Next")
    firstclose.bind('<Button-1>',GameStart)
    firstclose.pack(side='bottom')
    

Start()

game.mainloop()
