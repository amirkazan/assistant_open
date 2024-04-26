import tkinter as tk
from pyalex import Works
from langchain.schema import HumanMessage

def search_articles(query):
    works = Works().search(query).get()
    return works	
   

def display_article_summaries(root, messages, chat, articles, text_box):
    summary_window = tk.Toplevel(root)
    summary_window.title("Краткие выжимки статей")

    for article in articles[:3]:
        article_text = f"Название: {article['title']}\nСсылка: {article['doi']}"
        message = HumanMessage(content=f"Сделай краткую выжимку из данной статьи: {article_text}")
        article_summary = chat.invoke([message]).content
        article_summary_label = tk.Label(summary_window, text=article_summary, wraplength=600)
        article_summary_label.pack(pady=10)
        text_box.insert(tk.END, f"Название: {article['title']}\nСсылка: {article['doi']}" + "\n")





def search_and_display(self):
    query = self.entry_box.get()
    articles = search_articles(query)
    display_article_summaries(self.master, self.messages, self.chat, articles, self.text_box)



