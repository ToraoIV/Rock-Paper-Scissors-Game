import customtkinter as ctk
import tkinter as tk
from PIL import Image
import random

user_choice = ""
cmpt_sayi = ""


def random_sayi():
    global cmpt_sayi
    cmpt_sayi = random.randint(1, 3)
    print(cmpt_sayi)


random_sayi()


def rock_func():
    global user_choice
    user_choice = "1"


def paper_func():
    global user_choice
    user_choice = "2"


def scissors_func():
    global user_choice
    user_choice = "3"


window = ctk.CTk()
window.geometry("400x500")
window.title("Rock Paper Scissors")
window.resizable(False, False)

rock_img_big = ctk.CTkImage(Image.open("images/r.png"), size=(120, 120))
paper_img_big = ctk.CTkImage(Image.open("images/p.png"), size=(120, 120))
scissors_img_big = ctk.CTkImage(Image.open("images/s.png"), size=(120, 120))
restart_img = ctk.CTkImage(Image.open("images/restart.png"))


game_label = ctk.CTkLabel(window, text="Rock Paper Scissors", font=("Helvetica", 30, "bold"))
game_label.pack(pady=(20, 30))

player_frame = ctk.CTkFrame(window, fg_color="transparent")
player_frame.pack()

you_label = ctk.CTkLabel(player_frame, text="You", font=("Helvetica", 20, "bold"))
you_label.pack(side=tk.LEFT, padx=(50, 35))
computer_label = ctk.CTkLabel(player_frame, text="Computer", font=("Helvetica", 20, "bold"))
computer_label.pack(side=tk.LEFT, padx=(110, 20))

picture_frame = ctk.CTkFrame(window, fg_color="transparent")
picture_frame.pack(pady=(40, 20))

you_img = ctk.CTkImage(Image.open("images/profile.png"), size=(120, 120))
you_choice_label = ctk.CTkLabel(picture_frame, image=you_img, text="", font=("Helvetica", 40, "bold"))
you_choice_label.pack(side=tk.LEFT, padx=(10, 20))
vs_label = ctk.CTkLabel(picture_frame, text="VS", font=("Helvetica", 40, "bold"))
vs_label.pack(side=tk.LEFT)
comp_img = ctk.CTkImage(Image.open("images/comp.png"), size=(120, 120))
comp_choice_label = ctk.CTkLabel(picture_frame, image=comp_img, text="", font=("Helvetica", 40, "bold"))
comp_choice_label.pack(side=tk.LEFT, padx=(20, 10))

win_frame = ctk.CTkFrame(window, fg_color="transparent")
win_frame.pack()

win_label = ctk.CTkLabel(win_frame, text="Make your choice", font=("Helvetica", 30, "bold"))
win_label.pack(side=tk.LEFT, pady=10)

options_frame = ctk.CTkFrame(window, fg_color="transparent")
options_frame.pack(pady=20)


def change_rock(e):
    rock_img = ctk.CTkImage(Image.open("images/r2.png"), size=(80, 80))
    rock.configure(image=rock_img)
    rock.image = rock_img


def change_rock_back(e):
    rock_img = ctk.CTkImage(Image.open("images/r.png"), size=(80, 80))
    rock.configure(image=rock_img)
    rock.image = rock_img


rock_img = ctk.CTkImage(Image.open("images/r.png"), size=(80, 80))
rock = ctk.CTkButton(options_frame, image=rock_img, text="", width=50, state="normal", hover=False, fg_color="transparent", command= lambda : (rock_func(), game(), change_cmpt(), change_user(), switch()))
rock.pack(side=tk.LEFT, padx=10)

rock.bind("<Enter>", change_rock)
rock.bind("<Leave>", change_rock_back)


def change_paper(e):
    paper_img = ctk.CTkImage(Image.open("images/p2.png"), size=(80, 80))
    paper.configure(image=paper_img)
    paper.image = paper_img


def change_paper_back(e):
    paper_img = ctk.CTkImage(Image.open("images/p.png"), size=(80, 80))
    paper.configure(image=paper_img)
    paper.image = paper_img


paper_img = ctk.CTkImage(Image.open("images/p.png"), size=(80, 80))
paper = ctk.CTkButton(options_frame, image=paper_img, text="", width=50, state="normal", hover=False, fg_color="transparent", command= lambda : (paper_func(), game(), change_cmpt(), change_user(), switch()))
paper.pack(side=tk.LEFT, padx=10)

paper.bind("<Enter>", change_paper)
paper.bind("<Leave>", change_paper_back)


def change_scissors(e):
    scissors_img = ctk.CTkImage(Image.open("images/s2.png"), size=(80, 80))
    scissors.configure(image=scissors_img)
    scissors.image = scissors_img


def change_scissors_back(e):
    scissors_img = ctk.CTkImage(Image.open("images/s.png"), size=(80, 80))
    scissors.configure(image=scissors_img)
    scissors.image = scissors_img


scissors_img = ctk.CTkImage(Image.open("images/s.png"), size=(80, 80))
scissors = ctk.CTkButton(options_frame, image=scissors_img, text="", width=50, state="normal", hover=False, fg_color="transparent", command= lambda : (scissors_func(), game(), change_cmpt(), change_user(), switch()))
scissors.pack(side=tk.LEFT, padx=10)

scissors.bind("<Enter>", change_scissors)
scissors.bind("<Leave>", change_scissors_back)


def game():
    global cmpt_sayi, restart_but
    if int(user_choice) == int(cmpt_sayi):
        win_label.configure(text="Tie")
        restart_but = ctk.CTkButton(win_frame, text="Restart", image=restart_img, width=30, corner_radius=30, fg_color="#a100ff", hover_color="#C05AFC", command= lambda : restart())
        restart_but.pack(side=tk.RIGHT, padx=30)
    elif int(user_choice) == 1 and int(cmpt_sayi) == 2:
        win_label.configure(text="You Lose")
        restart_but = ctk.CTkButton(win_frame, text="Restart", image=restart_img, width=30, corner_radius=30, fg_color="#a100ff", hover_color="#C05AFC", command= lambda : restart())
        restart_but.pack(side=tk.RIGHT, padx=30)
    elif int(user_choice) == 1 and int(cmpt_sayi) == 3:
        win_label.configure(text="You Win")
        restart_but = ctk.CTkButton(win_frame, text="Restart", image=restart_img, width=30, corner_radius=30, fg_color="#a100ff", hover_color="#C05AFC", command= lambda : restart())
        restart_but.pack(side=tk.RIGHT, padx=30)
    elif int(user_choice) == 2 and int(cmpt_sayi) == 1:
        win_label.configure(text="You Win")
        restart_but = ctk.CTkButton(win_frame, text="Restart", image=restart_img, width=30, corner_radius=30, fg_color="#a100ff", hover_color="#C05AFC", command= lambda : restart())
        restart_but.pack(side=tk.RIGHT, padx=30)
    elif int(user_choice) == 2 and int(cmpt_sayi) == 3:
        win_label.configure(text="You Lose")
        restart_but = ctk.CTkButton(win_frame, text="Restart", image=restart_img, width=30, corner_radius=30, fg_color="#a100ff", hover_color="#C05AFC", command= lambda : restart())
        restart_but.pack(side=tk.RIGHT, padx=30)
    elif int(user_choice) == 3 and int(cmpt_sayi) == 1:
        win_label.configure(text="You Lose")
        restart_but = ctk.CTkButton(win_frame, text="Restart", image=restart_img, width=30, corner_radius=30, fg_color="#a100ff", hover_color="#C05AFC", command= lambda : restart())
        restart_but.pack(side=tk.RIGHT, padx=30)
    elif int(user_choice) == 3 and int(cmpt_sayi) == 2:
        win_label.configure(text="You Win")
        restart_but = ctk.CTkButton(win_frame, text="Restart", image=restart_img, width=30, corner_radius=30, fg_color="#a100ff", hover_color="#C05AFC", command= lambda : restart())
        restart_but.pack(side=tk.RIGHT, padx=30)
    else:
        print("?")


def change_cmpt():
    if int(cmpt_sayi) == 1:
        comp_choice_label.configure(image=rock_img_big)
    elif int(cmpt_sayi) == 2:
        comp_choice_label.configure(image=paper_img_big)
    elif int(cmpt_sayi) == 3:
        comp_choice_label.configure(image=scissors_img_big)
    else:
        pass


def change_user():
    if int(user_choice) == 1:
        you_choice_label.configure(image=rock_img_big)
    elif int(user_choice) == 2:
        you_choice_label.configure(image=paper_img_big)
    elif int(user_choice) == 3:
        you_choice_label.configure(image=scissors_img_big)
    else:
        pass


def switch():
    scissors.configure(state="disabled")
    rock.configure(state="disabled")
    paper.configure(state="disabled")


def restart():
    restart_but.pack_forget()
    win_label.configure(text="Make your choice")
    comp_choice_label.configure(image=comp_img)
    you_choice_label.configure(image=you_img)
    scissors.configure(state="normal")
    rock.configure(state="normal")
    paper.configure(state="normal")
    random_sayi()


window.mainloop()
