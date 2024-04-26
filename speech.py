# -*- coding: utf-8 -*-
import speech_recognition as sr
import pyaudio
import wave
import os
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
REC_SEC = 5
OUTPUT = "output.wav"

import time

def record_and_recognize():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Record")
    frames = []
    for i in range(0, int(RATE / CHUNK * REC_SEC)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Done")

    stream.stop_stream()
    stream.close()
    p.terminate()

    w = wave.open(OUTPUT, 'wb')
    w.setnchannels(CHANNELS)
    w.setsampwidth(p.get_sample_size(FORMAT))
    w.setframerate(RATE)
    w.writeframes(b''.join(frames))
    w.close()

    if os.path.isfile(OUTPUT):
        sample = sr.WavFile(OUTPUT)
        r = sr.Recognizer()

        with sample as audio:
            r.adjust_for_ambient_noise(audio)
            content = r.record(audio)

        try:
            recognized_text = r.recognize_google(content, language="ru-RU")
            return recognized_text
        except sr.UnknownValueError:
            print("Распознавание речи не удалось: неизвестное значение")
        except sr.RequestError as e:
            print(f"Ошибка при запросе к сервису Google: {e}")
            # Добавляем задержку перед следующей попыткой
            time.sleep(5)
            return record_and_recognize()
    else:
        print("Файл output.wav не найден или недоступен")
    
    return None


