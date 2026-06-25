import customtkinter as ctk
import math
# ---------- Appearance ----------
ctk.set_appearance_mode("light")

root = ctk.CTk()
root.title("🌸 Pink Calculator 🌸")
root.geometry("400x600")

# ---------- Variables ----------
expression = ""

# ---------- Functions ----------
def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, "end")
    display.insert(0, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, "end")


def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, "end")
        display.insert(0, result)
        expression = result
    except:
        display.delete(0, "end")
        display.insert(0, "Error")
        expression = ""



# ---------- Main Frame ----------
frame = ctk.CTkFrame(
    root,
    fg_color="#FFE4E8",
    corner_radius=20
)
frame.pack(fill="both", expand=True, padx=20, pady=20)

# ---------- Title ----------
title = ctk.CTkLabel(
    frame,
    text="🌷 Calculator 🌷",
    font=("Comic Sans MS", 24, "bold")
)
title.pack(pady=20)

# ---------- Display ----------
display = ctk.CTkEntry(
    frame,
    height=60,
    font=("Arial", 24),
    justify="right"
)
display.pack(fill="x", padx=20, pady=20)

# ---------- Button Frame ----------
button_frame = ctk.CTkFrame(frame, fg_color="transparent")
button_frame.pack(padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"]
]

# Create buttons
for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        btn = ctk.CTkButton(
            button_frame,
            text=button,
            width=70,
            height=60,
            corner_radius=15,
            fg_color="#FFB6C1",
            hover_color="#FF9EB5",
            text_color="black",
            font=("Arial", 18, "bold"),
            command=lambda value=button: button_click(value)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)

# Clear button
clear_btn = ctk.CTkButton(
    button_frame,
    text="C",
    width=150,
    height=60,
    fg_color="#FFC0CB",
    hover_color="#FF9EB5",
    text_color="black",
    font=("Arial", 18, "bold"),
    command=clear
)
clear_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Equal button
equal_btn = ctk.CTkButton(
    button_frame,
    text="=",
    width=150,
    height=60,
    fg_color="#FF69B4",
    hover_color="#FF1493",
    text_color="white",
    font=("Arial", 18, "bold"),
    command=calculate
)
equal_btn.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()

