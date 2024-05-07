from tkinter import*
from PIL import Image,ImageTk
import random


player_score = 0
computer_score = 0

def play():
    global player_score, computer_score

    player_choice = var.get()


    if player_choice == 1:
        player_choice = "rock"
    elif player_choice == 2:
        player_choice = "paper"
    else:
        player_choice = "scissors"

    computer_choice = random.choice(["rock", "paper", "scissors"])


    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You win!")
        player_score += 1
    else:
        result_label.config(text="You lose!")
        computer_score += 1


    user_label.config(text=f"Player: {player_score}")
    com_label.config(text=f" Computer: {computer_score}")
    
    com_choice_label.config(text=f"{computer_choice }")

def reset():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    user_label.config(text=f"Player: {player_score} ")
    com_label.config(text=f" Computer: {computer_score}")
    result_label.config(text="")
    com_choice_label.config(text="")


root = Tk()
root.title("Rock-Paper-Scissors")

root.configure(bg='#93FFFD')

user_var = StringVar()
head1=Label(root,text="ROCK",font=50,bg='#5DFFFC').grid(row=0,column=2)
head2=Label(root,text="PAPER ",font=50,bg='#5DFFFC').grid(row=0,column=3)
head3=Label(root,text="SCISSOR ",font=50,bg='#5DFFFC').grid(row=0,column=4)


#head=Label(root,text="rock paper and scissors ",font=80).grid(row=0,column=3)

#title 
user=Label(root,font=40,text="USER",bg='#5DFFFC')
user.grid(row=1,column=0)
com=Label(root,font=40,text="COMPUTER",bg='#5DFFFC')
com.grid(row=1,column=5)

#image
user_img=ImageTk.PhotoImage(Image.open("user.png"))
com_img=ImageTk.PhotoImage(Image.open("computer.png"))

#show 
user_img_label=Label(root,image=user_img)
user_img_label.grid(row=2,column=0)
com_img_label=Label(root,image=com_img)
com_img_label.grid(row=2,column=5)

#score
user_label = Label(root, text="Player: 0 ",font=30,bg='#5DFFFC')
user_label.grid(row=2,column=2)
com_label = Label(root, text=" Computer: 0",font=30,bg='#5DFFFC')
com_label.grid(row=2,column=4)

#choice heading
user_choice_label=Label(root,text="CHOOSE ANY",font=50,bg='#5DFFFC').grid(row=3,column=2)
com_choice_label1=Label(root,text="COMPUTER ",font=50,bg='#5DFFFC').grid(row=3,column=4)


#button
var = IntVar()
rock_button = Radiobutton(root, text="Rock", variable=var, value=1,font=30,bg='#5DFFFC')
rock_button.grid(row=4,column=2)
paper_button = Radiobutton(root, text="Paper", variable=var, value=2,font=30,bg='#5DFFFC')
paper_button.grid(row=5,column=2)
scissors_button = Radiobutton(root, text="Scissors", variable=var, value=3,font=30,bg='#5DFFFC')
scissors_button.grid(row=6,column=2)

#computer choice
com_choice_label = Label(root, text="",font=30,bg='#5DFFFC')
com_choice_label.grid(row=5,column=4)

#result 
result_label = Label(root, text="",font=30,bg='#5DFFFC')
result_label.grid(row=2,column=3)

#button
play_button = Button(root, text="Play", command=play,width=20,height=2,font=30,bg='#5DFFFC')
play_button.grid(row=7,column=2)

reset_button = Button(root, text="Reset", command=reset,width=20,height=2,font=30,bg='#5DFFFC')
reset_button.grid(row=7,column=4)

root.mainloop()
