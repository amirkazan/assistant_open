import tkinter as tk
from tkinter import filedialog
import os
from langchain.schema import HumanMessage
import PyPDF2
from docx import Document

def upload_file(self):
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        file_type = os.path.splitext(file_path)[1]

        if file_type == ".pdf":
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page_obj = pdf_reader.pages[page_num]
                    text += page_obj.extract_text()

            # Создаем новое сообщение от пользователя с содержимым файла
            user_message = HumanMessage(content="Тебе передали файл " + file_name + ". Его содержимое: " + text)
            self.messages.append(user_message)

            # Передаем сообщение в нейросеть и получаем ответ
            res = self.chat.invoke(self.messages)
            self.messages.append(res)
            self.text_box.insert(tk.END, "Вы передали файл: " + file_name + "\n")
        elif file_type == ".docx":
            doc = Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text

            # Создаем новое сообщение от пользователя с содержимым файла
            user_message = HumanMessage(content="Тебе передали файл " + file_name + ". Его содержимое: " + text)
            self.messages.append(user_message)

            # Передаем сообщение в нейросеть и получаем ответ
            res = self.chat.invoke(self.messages)
            self.messages.append(res)
            self.text_box.insert(tk.END, "Вы передали файл: " + file_name + "\n")
        elif file_type == ".txt":
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            # Создаем новое сообщение от пользователя с содержимым файла
            user_message = HumanMessage(content="Тебе передали файл " + file_name + ". Его содержимое: " + text)
            self.messages.append(user_message)

            # Передаем сообщение в нейросеть и получаем ответ
            res = self.chat.invoke(self.messages)
            self.messages.append(res)
            self.text_box.insert(tk.END, "Вы передали файл: " + file_name + "\n")
        else:
            self.text_box.insert(tk.END, "Неподдерживаемый формат файла: " + file_type + "\n")
    else:
        # Пользователь отменил выбор файла
        pass
