import customtkinter
import subprocess
import mysql.connector
from datetime import datetime
from PIL import Image
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.geometry('500x500')
root.title("Tic-Tac-Toe")
def game():
    player1=e1.get()
    player2=e2.get()
    connection=mysql.connector.connect(
        host="localhost",
    	user="root",
		password="0909",
		database="project"
    )
    current_time=datetime.now()
    cursor=connection.cursor()
    insert_query='INSERT INTO result (player_1, player_2, gametime) VALUES (%s,%s,%s)'
    insert_values=(player1,player2,current_time)
    cursor.execute(insert_query,insert_values)
    connection.commit()
    connection.close()    
    subprocess.Popen(['python',"C:\\Users\\himan\\COMPUTER PROJECT 2023-24\\GameBoard.py"])    
def exit():
    root.destroy()    
def check_entry():
    if e1.get() and e2.get():
        b1.configure(state="normal")
    else:
        b1.configure(state="disabled")           
frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)
my_image = customtkinter.CTkImage(dark_image=Image.open("C:\\Users\\himan\\COMPUTER PROJECT 2023-24\\python logo1.png"),size=(120, 120))
l1=customtkinter.CTkLabel(frame,image=my_image,text="")
l1.pack()
l2=customtkinter.CTkLabel(frame,text="TIC-TAC-TOE",font=("Roboto",45,),text_color=("#4169E1"))
l2.pack()
l3=customtkinter.CTkLabel(frame,text="Strategize, Triumph, Tic Tac Toe: The Ultimate Battle of Xs and Os!!",font=("Roboto",12,"italic","underline"),text_color=("#FFD700"))
l3.pack()
e1=customtkinter.CTkEntry(frame, placeholder_text="Player 1(X)",width=200)
e1.pack(padx=12,pady=14)
e2=customtkinter.CTkEntry(frame, placeholder_text="Player 2(O)",width=200)
e2.pack(padx=12,pady=14)
e1.bind("<KeyRelease>", lambda event: check_entry())
e2.bind("<KeyRelease>", lambda event: check_entry())
b1=customtkinter.CTkButton(frame,text="PLAY GAME",hover=True,hover_color="green",command=game,state='disabled')
b1.pack(padx=14,pady=12)
b2=customtkinter.CTkButton(frame,text='EXIT GAME',hover=True,hover_color="#8B0000",command=exit)
b2.pack()
check_entry()
root.mainloop()