import tkinter as tk
from langchain.schema import HumanMessage
import requests
from bs4 import BeautifulSoup

def process_url(self):
    url = self.entry_box.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()

    # Создаем новое сообщение от пользователя с содержимым сайта
    user_message = HumanMessage(content="Тебе передана ссылка " + url + ". Его содержимое: " + text)
    self.messages.append(user_message)

    # Передаем сообщение в нейросеть и получаем ответ
    res = self.chat.invoke(self.messages)
    self.messages.append(res)
    self.text_box.insert(tk.END, "Вы передали ссылку: " + url + "\n")
