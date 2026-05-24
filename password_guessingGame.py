import tkinter as tk
from tkinter import messagebox
import random

# ======================================================
#        NUMBER PASSWORD GUESSING GAME - UI VERSION
# ======================================================

# ---------------- PASSWORD LIST ---------------- #

easy_passwords = ['1234', '5678', '1111', '2025', '4321','2323','8786','1313','1006','8765','3456','7890','4321','5678','9009']

medium_passwords = ['45879', '93210', '78125', '65432', '98765','12346','45321','00009','43312','12121','32323','55555']

hard_passwords = ['847261', '915732', '628491', '753951', '482617','333333','654321','567765','131313','171717','090909','400004']

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Number Password Guessing Game")
root.geometry("900x650")
root.config(bg="#0f172a")

# Allow maximize button
root.resizable(True, True)

# ---------------- VARIABLES ---------------- #

secret_password = ""
max_attempts = 0
attempts = 0
game_started = False

# ---------------- FUNCTIONS ---------------- #

def start_game():

    global secret_password, max_attempts, attempts, game_started

    player_name = name_entry.get().strip()

    if player_name == "":
        messagebox.showwarning(
            "Warning",
            "Please Enter Your Name"
        )
        return

    difficulty = level_var.get()

    # Difficulty selection
    if difficulty == "Easy":
        secret_password = random.choice(easy_passwords)
        max_attempts = 10

    elif difficulty == "Medium":
        secret_password = random.choice(medium_passwords)
        max_attempts = 7

    else:
        secret_password = random.choice(hard_passwords)
        max_attempts = 5

    attempts = 0
    game_started = True

    # Update UI
    result_label.config(
        text=f"Welcome {player_name}! Game Started 🎮",
        fg="#22c55e"
    )

    hint_label.config(
        text="# " * len(secret_password),
        fg="#facc15"
    )

    attempts_label.config(
        text=f"Remaining Attempts: {max_attempts}"
    )

    difficulty_label.config(
        text=f"Difficulty: {difficulty}"
    )

    length_label.config(
        text=f"Password Length: {len(secret_password)} Digits"
    )

    guess_entry.delete(0, tk.END)
    guess_entry.focus()


# ------------------------------------------------ #

def check_guess(event=None):

    global attempts, game_started

    if not game_started:
        messagebox.showwarning(
            "Warning",
            "Please Click START GAME First"
        )
        return

    guess = guess_entry.get().strip()

    if guess == "":
        messagebox.showwarning(
            "Warning",
            "Please Enter Your Guess"
        )
        return

    if not guess.isdigit():
        messagebox.showwarning(
            "Invalid Input",
            "Please Enter Numbers Only"
        )
        return

    attempts += 1

    # ------------- CORRECT PASSWORD ------------- #

    if guess == secret_password:

        score = (max_attempts - attempts + 1) * 10

        result_label.config(
            text="🎉 PASSWORD MATCHED 🎉",
            fg="#22c55e"
        )

        messagebox.showinfo(
            "Congratulations",
            f"You guessed the password!\n\n"
            f"Password : {secret_password}\n"
            f"Attempts : {attempts}\n"
            f"Score : {score}"
        )

        reset_game()
        return

    # ------------- HINT SYSTEM ------------- #

    hint = ""

    for i in range(len(secret_password)):

        if i < len(guess) and guess[i] == secret_password[i]:
            hint += guess[i] + " "
        else:
            hint += "# "

    remaining = max_attempts - attempts

    hint_label.config(text=hint)

    attempts_label.config(
        text=f"Remaining Attempts: {remaining}"
    )

    result_label.config(
        text="❌ Wrong Password",
        fg="#ef4444"
    )

    # Extra hint
    if remaining == 2:
        extra_hint.config(
            text=f"💡 First Digit is : {secret_password[0]}"
        )

    # ------------- GAME OVER ------------- #

    if remaining <= 0:

        messagebox.showerror(
            "Game Over",
            f"You Lost!\n\nCorrect Password : {secret_password}"
        )

        result_label.config(
            text="💀 GAME OVER 💀",
            fg="red"
        )

        reset_game()

    guess_entry.delete(0, tk.END)


# ------------------------------------------------ #

def reset_game():

    global game_started

    game_started = False

    guess_entry.delete(0, tk.END)


# ===================== TITLE ===================== #

title = tk.Label(
    root,
    text="NUMBER PASSWORD GUESSING GAME",
    font=("Poppins", 30, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=25)

# ===================== MAIN FRAME ===================== #

frame = tk.Frame(
    root,
    bg="#1e293b",
    padx=40,
    pady=40
)

frame.pack(pady=20)

# ===================== NAME ===================== #

name_label = tk.Label(
    frame,
    text="Player Name",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="white"
)

name_label.grid(row=0, column=0, pady=15, padx=15)

name_entry = tk.Entry(
    frame,
    font=("Arial", 15),
    width=25,
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief="flat"
)

name_entry.grid(row=0, column=1, pady=15)

# ===================== DIFFICULTY ===================== #

level_label = tk.Label(
    frame,
    text="Difficulty",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="white"
)

level_label.grid(row=1, column=0, pady=15)

level_var = tk.StringVar()
level_var.set("Easy")

level_menu = tk.OptionMenu(
    frame,
    level_var,
    "Easy",
    "Medium",
    "Hard"
)

level_menu.config(
    font=("Arial", 13),
    bg="#38bdf8",
    fg="black",
    width=20,
    relief="flat"
)

level_menu.grid(row=1, column=1)

# ===================== START BUTTON ===================== #

start_btn = tk.Button(
    frame,
    text="START GAME",
    font=("Arial", 14, "bold"),
    bg="#22c55e",
    fg="white",
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=start_game
)

start_btn.grid(row=2, column=0, columnspan=2, pady=25)

# ===================== GUESS ===================== #

guess_label = tk.Label(
    frame,
    text="Enter Number Password",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="white"
)

guess_label.grid(row=3, column=0, pady=15)

guess_entry = tk.Entry(
    frame,
    font=("Arial", 15),
    width=25,
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief="flat"
)

guess_entry.grid(row=3, column=1, pady=15)

# ===================== CHECK BUTTON ===================== #

check_btn = tk.Button(
    frame,
    text="CHECK PASSWORD",
    font=("Arial", 14, "bold"),
    bg="#3b82f6",
    fg="white",
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=check_guess
)

check_btn.grid(row=4, column=0, columnspan=2, pady=25)

# ENTER KEY SUPPORT
root.bind("<Return>", check_guess)

# ===================== RESULT LABEL ===================== #

result_label = tk.Label(
    root,
    text="Start the Game to Begin!",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="white"
)

result_label.pack(pady=10)

# ===================== PASSWORD LENGTH ===================== #

length_label = tk.Label(
    root,
    text="Password Length: 0",
    font=("Arial", 15),
    bg="#0f172a",
    fg="#cbd5e1"
)

length_label.pack()

# ===================== DIFFICULTY LABEL ===================== #

difficulty_label = tk.Label(
    root,
    text="Difficulty: None",
    font=("Arial", 15),
    bg="#0f172a",
    fg="#cbd5e1"
)

difficulty_label.pack()

# ===================== HINT LABEL ===================== #

hint_label = tk.Label(
    root,
    text="",
    font=("Courier", 28, "bold"),
    bg="#0f172a",
    fg="#facc15"
)

hint_label.pack(pady=20)

# ===================== ATTEMPTS LABEL ===================== #

attempts_label = tk.Label(
    root,
    text="Remaining Attempts: 0",
    font=("Arial", 16, "bold"),
    bg="#0f172a",
    fg="white"
)

attempts_label.pack()

# ===================== EXTRA HINT ===================== #

extra_hint = tk.Label(
    root,
    text="",
    font=("Arial", 15, "bold"),
    bg="#0f172a",
    fg="#22c55e"
)

extra_hint.pack(pady=10)

# ===================== FOOTER ===================== #

footer = tk.Label(
    root,
    text="Created with Python Tkinter ❤️",
    font=("Arial", 11),
    bg="#0f172a",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

# ===================== RUN APP ===================== #

root.mainloop()