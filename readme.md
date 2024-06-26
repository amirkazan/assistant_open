Документация для программы "Ассистент Морти"

## Общее описание
Программа "Ассистент Морти" представляет собой интерактивный чат-бот, который может помогать пользователям в различных задачах, таких как поиск и анализ научных статей, обработка текстовых файлов, распознавание речи и т.д. Программа построена на использовании библиотек Tkinter для создания графического интерфейса и GigaChain для взаимодействия с нейросетевой языковым моделью.

## Основные возможности
1. **Поиск и анализ научных статей**: Пользователь может ввести ключевое слово в поле ввода и нажать кнопку "Find articles". Программа выполнит поиск статей по заданному запросу, используя OpenAlex API, и отобразит название и ссылку на первые три найденные статьи в основном окне программы. Кроме того, в отдельном окне будут показаны краткие выжимки из этих статей, сгенерированные нейросетью.

2. **Обработка текстовых файлов**: Пользователь может загрузить текстовый файл (в форматах .txt, .pdf или .docx) с помощью кнопки "Upload File". Программа извлечет текст из файла и передаст его в нейросеть, которая сформирует ответ, отображаемый в основном окне программы.

3. **Обработка ссылок на веб-страницы**: Пользователь может ввести URL-адрес веб-страницы в поле ввода и нажать кнопку "Process URL". Программа загрузит содержимое веб-страницы, используя библиотеку BeautifulSoup, и передаст его в нейросеть для обработки. Ответ нейросети будет отображен в основном окне программы.

4. **Голосовой ввод**: Пользователь может нажать кнопку "Voice Input", чтобы записать голосовое сообщение. Программа использует библиотеку speech_recognition для распознавания речи и вставляет распознанный текст в поле ввода. Затем пользователь может отправить сообщение, нажав клавишу Enter.

## Структура проекта
Проект состоит из следующих файлов:

1. `main.py`: Точка входа в программу, создающая окно Tkinter и экземпляр класса `ChatApp`.
2. `chat_app.py`: Содержит определение класса `ChatApp`, который отвечает за создание и управление графическим интерфейсом программы.
3. `article.py`: Содержит функции для поиска и отображения информации о научных статьях.
4. `process_url.py`: Содержит функцию для обработки URL-адресов веб-страниц.
5. `upload_file.py`: Содержит функцию для обработки загруженных текстовых файлов.
6. `send_message.py`: Содержит функцию для отправки сообщений в чат.
7. `voice_input.py`: Содержит функцию для обработки голосового ввода.
8. `speech.py`: Содержит функции для записи и распознавания речи.

## Требования
Для работы программы необходимы следующие библиотеки:
- `tkinter`
- `langchain`
- `pyalex`
- `requests`
- `beautifulsoup4`
- `PyPDF2`
- `python-docx`
- `speech_recognition`
- `pyaudio`


## Использование
0. Добавьте свой токен в поле "token=*ваш токен*" в начале файла `chat_app.py`.
1. Запустите программу, выполнив `main.py`.
2. Используйте поле ввода, кнопки и другие элементы интерфейса для взаимодействия с программой.
3. Для поиска и анализа статей введите ключевое слово в поле ввода и нажмите кнопку "Find articles".
4. Для загрузки текстового файла нажмите кнопку "Upload File" и выберите файл.
5. Для обработки URL-адреса веб-страницы введите URL в поле ввода и нажмите кнопку "Process URL".
6. Для голосового ввода нажмите кнопку "Voice Input" и произнесите сообщение.

## Примечания
- Программа использует нейросетевую модель GigaChat для обработки сообщений пользователя. Для работы с этой моделью требуется наличие соответствующих учетных данных.
- Функциональность распознавания речи может работать некорректно в зависимости от качества микрофона и окружающей обстановки.
- Программа поддерживает только файлы в форматах .txt, .pdf и .docx.