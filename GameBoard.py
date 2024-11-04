from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import tkinter as tk
root = tk.Tk()
root.title('Tic-Tac-Toe')
#getting player names
connection=mysql.connector.connect(
	host="localhost",
	user="root",
	password="0909",
	database="project"
)
cursor=connection.cursor()
q1='Select player_1 from result'
cursor.execute(q1)
p1=cursor.fetchall()
pl1=p1[-1]
player1=pl1[0]
q2='Select player_2 from result'
cursor.execute(q2)
p2=cursor.fetchall()
pl2=p2[-1]
player2=pl2[0]
player1=str(player1)
player2=str(player2)
connection.close()
# X starts so true
clicked = True
count = 0
# disable all the buttons
def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)
# Check to see if someone won
def winner_entry(player_name="Tie"):
	connection1=mysql.connector.connect(
		host="localhost",
    	user="root",
		password="0909",
		database="project"
	)
	cursor1=connection1.cursor()
	q3="update result set winner=%s where player_1=%s AND player_2=%s"
	q4="update result set winner=%s where player_1=%s AND player_2=%s"
	if count==9 and winner==False:
		cursor1.execute(q4,(player_name,player1,player2))
	else:	
		cursor1.execute(q3,(player_name,player1,player2))
	connection1.commit()
	connection1.close()
def checkifwon():
	global winner
	winner = False
	m1= f"\U0001F389 CONGRATULATIONS {player1} Wins!!"
	m2= f"\U0001F389 CONGRATULATIONS {player2} Wins!!"
	if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
		b1.config(bg="cyan")
		b2.config(bg="cyan")
		b3.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m1)
		winner_entry(player1)
		disable_all_buttons()
	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
		b4.config(bg="cyan")
		b5.config(bg="cyan")
		b6.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m1)
		winner_entry(player1)
		disable_all_buttons()
	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
		b7.config(bg="cyan")
		b8.config(bg="cyan")
		b9.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m1)
		winner_entry(player1)
		disable_all_buttons()
	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
		b1.config(bg="cyan")
		b4.config(bg="cyan")
		b7.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m1)
		winner_entry(player1)
		disable_all_buttons()
	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
		b2.config(bg="cyan")
		b5.config(bg="cyan")
		b8.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m1)
		winner_entry(player1)
		disable_all_buttons()
	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
		b3.config(bg="cyan")
		b6.config(bg="cyan")
		b9.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m1)
		winner_entry(player1)
		disable_all_buttons()
	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
		b1.config(bg="cyan")
		b5.config(bg="cyan")
		b9.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m1)
		winner_entry(player1)
		disable_all_buttons()
	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
		b3.config(bg="cyan")
		b5.config(bg="cyan")
		b7.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m1)
		winner_entry(player1)
		disable_all_buttons()
	#### CHECK FOR O's Win
	elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
		b1.config(bg="cyan")
		b2.config(bg="cyan")
		b3.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m2)
		winner_entry(player2)
		disable_all_buttons()
	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
		b4.config(bg="cyan")
		b5.config(bg="cyan")
		b6.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m2)
		winner_entry(player2)
		disable_all_buttons()
	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
		b7.config(bg="cyan")
		b8.config(bg="cyan")
		b9.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m2)
		winner_entry(player2)
		disable_all_buttons()
	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
		b1.config(bg="cyan")
		b4.config(bg="cyan")
		b7.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m2)
		winner_entry(player2)
		disable_all_buttons()
	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
		b2.config(bg="cyan")
		b5.config(bg="cyan")
		b8.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m2)
		winner_entry(player2)
		disable_all_buttons()
	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
		b3.config(bg="cyan")
		b6.config(bg="cyan")
		b9.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m2)
		winner_entry(player2)
		disable_all_buttons()
	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
		b1.config(bg="cyan")
		b5.config(bg="cyan")
		b9.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m2)
		winner_entry(player2)
		disable_all_buttons()
	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
		b3.config(bg="cyan")
		b5.config(bg="cyan")
		b7.config(bg="cyan")
		winner = True
		messagebox.showinfo("Tic Tac Toe",m2)
		winner_entry(player2)
		disable_all_buttons()
	#If tie
	if count == 9 and winner == False:
		messagebox.showinfo("Opss!!", "It's A Tie!\n No One Wins!")
		winner_entry()
		disable_all_buttons()
# Button clicked function
def b_click(b):
	global clicked, count
	if b["text"] == " " and clicked == True:
		b["text"] = "X"
		clicked = False
		count += 1
		checkifwon()
	elif b["text"] == " " and clicked == False:
		b["text"] = "O"
		clicked = True
		count += 1
		checkifwon()
	else:
		messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )
# Start the game over!
def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global clicked, count
	clicked = True
	count = 0
	#Buttons
	b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
	b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
	b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
	b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
	b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
	b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
	b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
	b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
	b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
	#Button grid
	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)
	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)
	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)
#Functions of option menu	
def end_game():
	root.destroy()	
#result window
def show_result():
	result_window=tk.Toplevel(root)
	result_window.title('Result')
	table = ttk.Treeview(result_window, columns=('Player1', 'Player2', 'Winner', 'GameTime'),show="headings")
	table.heading('Player1', text='Player 1')
	table.heading('Player2', text='Player 2')
	table.heading('Winner', text='Winner')
	table.heading('GameTime', text='Game Time')
	table.pack()
	style = ttk.Style()
	style.theme_use("classic")
	style.configure("Treeview",font=("Roboto", 12),rowheight=25)
	style.configure("Treeview.Heading",font=("Roboto", 14, "bold"))
	connection=mysql.connector.connect(
		host="localhost",
    	user="root",
		password="0909",
		database="project"
	)
	cursor=connection.cursor()
	query='SELECT * FROM result'
	cursor.execute(query)
	r=cursor.fetchall()
	for i in reversed(r):
		table.insert('','end',values=i)
	connection.close()
#instruction window
def instruction():
	instruction_window=tk.Toplevel(root)
	instruction_window.title('Instructions')
	instruction_window.configure(bg="#ADD8E6")
	L1=tk.Label(instruction_window,text="INSTRUCTIONS:-",font=("Roboto",22,"bold","italic","underline"),justify="center",bg="#ADD8E6")
	L1.pack()
	L2=tk.Label(instruction_window,text="1. The game is played on a grid that's 3 squares by 3 squares. \n2. You are X , your friend is O . \n3. Players take turns putting their marks in empty squares. \n4. The first player to get 3 of his/her marks in a row (up, down, across, or diagonally) is the winner. \n5. When all 9 squares are full, the game is over. \n6. If no player has 3 marks in a row, the game ends in a tie.",font=("Arial",13),justify="left",bg="#ADD8E6")
	L2.pack()
	L3=tk.Label(instruction_window,text="Some Tips ^_~",font=("Roboto",15,"bold","italic"),justify="left",bg="#ADD8E6")
	L3.pack()
	t="""Tic Tac Toe is a classic game of strategy. Here are some tips to help you play your best game:
1. Start in the center if you go first. It offers the most winning opportunities.
2. If your opponent starts in a corner, take the center to block potential winning moves.
3. Watch for opportunities to create forks (two winning paths).
4. Always block your opponent from creating forks.
5. Prioritize completing winning combinations when you have two in a row.
6. Be wary of falling into traps set by your opponent.
7. Pay attention to patterns that can lead to victory.
8. When neither player is close to winning, aim for a draw (a 'cat's game').
9. Practice and learn from each game to improve your skills.
Enjoy the game of Tic Tac Toe and have fun strategizing!"""
	L4=tk.Label(instruction_window,text=t,font=("Arial",13),justify="left",bg="#ADD8E6")
	L4.pack()
#Menue
my_menu = Menu(root)
root.config(menu=my_menu)
#OPtion menu
my_menu.add_cascade(label='Result',command=show_result)
my_menu.add_cascade(label="Instructions",command=instruction)
my_menu.add_cascade(label="Reset Game", command=reset)
my_menu.add_cascade(label="Exit",command=end_game)
reset()
root.mainloop()