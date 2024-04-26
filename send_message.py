import tkinter as tk
from langchain.schema import HumanMessage

def send_message(self, event=None):
    user_input = self.entry_box.get()
    self.messages.append(HumanMessage(content=user_input))
    res = self.chat.invoke(self.messages)
    self.messages.append(res)
    self.text_box.insert(tk.END, "Вы: " + user_input + "\n")
    self.text_box.insert(tk.END, "Морти: " + res.content + "\n")
    self.entry_box.delete(0, tk.END)
