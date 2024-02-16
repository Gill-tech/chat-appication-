


import tkinter as tk
from tkinter import scrolledtext

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")

        self.chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.chat_history.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(root, width=40)
        self.message_entry.pack(pady=10)

        send_button = tk.Button(root, text="Send", command=self.send_message)
        send_button.pack()

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.chat_history.insert(tk.END, "You: " + message + "\n")
            self.message_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
app = ChatApplication(root)
root.mainloop()
