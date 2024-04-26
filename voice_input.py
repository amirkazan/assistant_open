import tkinter as tk
from speech import record_and_recognize
from send_message import send_message

def voice_input(self):
    if self.can_run_voice_recognition:
        self.can_run_voice_recognition = False
        recognized_text = record_and_recognize()
        if recognized_text:
            self.entry_box.delete(0, tk.END)
            self.entry_box.insert(0, recognized_text)
            send_message(self)
        else:
            self.text_box.insert(tk.END, "Извините, я не смог распознать ваш голос. Пожалуйста, попробуйте еще раз.\n")
        self.can_run_voice_recognition = True
    else:
        self.text_box.insert(tk.END, "Пожалуйста, подождите, пока завершится предыдущее распознавание речи.\n")
