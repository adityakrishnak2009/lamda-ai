import customtkinter as ctk
import brain 
import datetime
import os
import json

CHAT_FOLDER = "chats"

if not os.path.exists(CHAT_FOLDER):
    os.makedirs(CHAT_FOLDER)

current_chat=None

# ---------------- APP ----------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1100x700")
app.title("Lamda AI")

# ---------------- COLORS ----------------
BG = "#f4f7ff"
CARD = "#ffffff"
INPUT = "#eef2ff"
BUTTON = "#6366f1"

app.configure(fg_color=BG)

# ---------------- MAIN FRAME ----------------
main_frame = ctk.CTkFrame(
    app,
    fg_color=CARD,
    corner_radius=25
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=25
)

# ---------------- SIDEBAR ----------------
sidebar = ctk.CTkFrame(
    main_frame,
    width=250,
    fg_color="#edf2ff",
    corner_radius=20
)

sidebar.pack(side="left", fill="y", padx=(15, 10), pady=15)
sidebar.pack_propagate(False)


# ---------------- RIGHT FRAME ----------------
right_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

right_frame.pack(side="left", fill="both", expand=True)

# ---------------- HEADER ----------------
header = ctk.CTkFrame(
    right_frame,
    fg_color="transparent"
)

header.pack(fill="x", padx=25, pady=(20, 10))

title = ctk.CTkLabel(
    header,
    text="Lamda AI",
    font=("Segoe UI", 30, "bold"),
    text_color="#223150"
)

title.pack(anchor="w")

# ---------------- CHAT AREA ----------------
chat_frame = ctk.CTkFrame(
    right_frame,
    fg_color="#f8f9ff",
    corner_radius=20
)

chat_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=15
)

chat_area = ctk.CTkTextbox(
    chat_frame,
    font=("Segoe UI", 15),
    fg_color="#f8f9ff",
    text_color="#111827",
    corner_radius=20,
    border_width=0
)

chat_area.pack(fill="both", expand=True, padx=10, pady=10)

chat_area.insert(
    "end",
    "Lamda AI: Hello! How can I help you today?\n\n"
)

# ---------------- INPUT AREA ----------------
bottom_frame = ctk.CTkFrame(
    right_frame,
    fg_color="transparent"
)

bottom_frame.pack(
    fill="x",
    padx=25,
    pady=(0, 25)
)

# ---------------- MODERN INPUT ----------------
user_input = ctk.CTkEntry(
    bottom_frame,
    placeholder_text="Message Lamda AI...",
    height=55,
    corner_radius=30,
    font=("Segoe UI", 15),
    fg_color=INPUT,
    border_width=0,
    text_color="#111827"
)

user_input.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 15)
)

# ---------------- SEND BUTTON ----------------
send_button = ctk.CTkButton(
    bottom_frame,
    text="➜",
    width=55,
    height=55,
    corner_radius=100,
    font=("Segoe UI", 22, "bold"),
    fg_color=BUTTON,
    hover_color="#4f46e5",
    text_color="white",
    border_width=0
)

history_frame = ctk.CTkScrollableFrame(
    sidebar,
    fg_color="transparent"
)

history_frame.pack(fill="both", expand=True, padx=10, pady=(0,10))

send_button.pack(side="right")


#---------------------------------------------

def create_new_chat():
    global current_chat

    filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"

    current_chat = os.path.join(CHAT_FOLDER, filename)

    with open(current_chat, "w", encoding="utf-8") as f:
        json.dump([], f)

    chat_area.delete("1.0", "end")
    chat_area.insert("end", "Lamda AI: Hello! How can I help you today?\n\n")

#---------------------------------------------
def refresh_sidebar():

    for widget in history_frame.winfo_children():
        widget.destroy()

    files = sorted(os.listdir(CHAT_FOLDER), reverse=True)

    for file in files:

        btn = ctk.CTkButton(
            history_frame,
            text=file.replace(".json",""),
            anchor="w",
            fg_color="transparent",
            text_color="black"
        )

        btn.pack(fill="x", pady=2)

new_chat_button = ctk.CTkButton(
    sidebar,
    text="+ New Chat",
    height=40,
    corner_radius=15,
    command=create_new_chat
)

new_chat_button.pack(fill="x", padx=10, pady=(15,10))

#---------------------------------------------

def send_message(event=None):

    message = user_input.get()

    if message.strip() == "":
        return

    # show user text
    chat_area.insert(
        "end",
        f"You: {message}\n\n"
    )

    # clear textbox
    user_input.delete(0, "end")

    # get response from assistant
    response = brain.respond_to_command(message)
    

    # THIS PART IS IMPORTANT
    chat_area.insert(
        "end",
        f"Lamda AI: {response}\n\n"
    )

    # auto scroll
    chat_area.see("end")

# ---------------- BUTTON COMMAND ----------------
send_button.configure(command=send_message)

# ---------------- ENTER KEY ----------------
app.bind("<Return>", send_message)

# ---------------- RUN ----------------

create_new_chat()
refresh_sidebar()

app.mainloop()