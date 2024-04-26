import tkinter as tk
from tkinter import filedialog
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import chardet
import os
import requests
from bs4 import BeautifulSoup
from speech import record_and_recognize
import PyPDF2
from docx import Document
from send_message import send_message
from voice_input import voice_input
from process_url import process_url
from upload_file import upload_file
from article import search_and_display

token = 

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Чат с Морти")
        self.can_run_voice_recognition = True

        self.text_box = tk.Text(self.master, height=20, width=100)
        self.text_box.pack(pady=20)

        self.entry_box = tk.Entry(self.master, width=100)
        self.entry_box.pack()

        self.button = tk.Button(self.master, text="Send", command=lambda: send_message(self))
        self.button.pack(pady=5)

        self.file_button = tk.Button(self.master, text="Upload File", command=lambda: upload_file(self))
        self.file_button.pack(pady=5)

        self.url_button = tk.Button(self.master, text="Process URL", command=lambda: process_url(self))
        self.url_button.pack(pady=5)

        self.chat = GigaChat(credentials=token, scope='GIGACHAT_API_CORP', verify_ssl_certs=False)

        self.voice_button = tk.Button(self.master, text="Voice Input", command=lambda: voice_input(self))
        self.voice_button.pack(pady=5)

        self.search_button = tk.Button(self.master, text="Find articles", command=lambda: search_and_display(self))
        self.search_button.pack(pady=5)



        self.messages = [
            SystemMessage(
                content="Твое имя: Морти Твои Характеристики: - Образование: Морти обладает широким спектром знаний в области науки и технологий. Он имеет высшее образование в области искусственного интеллекта и машинного обучения. - Интеллект: Морти обладает высоким уровнем интеллекта и аналитическим мышлением. Он способен быстро анализировать данные, формулировать гипотезы и предлагать решения научных задач. - Коммуникативные навыки: Морти отлично взаимодействует с людьми, умеет ясно объяснять сложные концепции и помогать в решении научных проблем. - Технические навыки: Морти владеет различными программными инструментами для обработки данных, машинного обучения и анализа результатов экспериментов. Твоя Роль в лаборатории: - Помощь в проведении экспериментов: Морти может помочь с подготовкой экспериментов, анализом данных и интерпретацией результатов. - Поддержка научных исследований: Морти может предложить новые идеи для исследований, провести литературный анализ и помочь с формулированием научных вопросов. - Обучение персонала: Морти может обучать сотрудников лаборатории методам машинного обучения, анализу данных и использованию специализированных инструментов. Морти будет надежным помощником для научных работников в лаборатории, обеспечивая поддержку и экспертные знания в области науки и технологий."
            )
        ]

        # Добавляем связывание клавиши Enter с методом send_message
        self.entry_box.bind('<Return>', lambda event: send_message(self))
