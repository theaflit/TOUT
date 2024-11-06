import speech_recognition as sr
from pydub import AudioSegment
import os


def convert_to_wav(audio_file):
    """Преобразование аудиофайла к общему формату"""
    audio = AudioSegment.from_mp3(audio_file)
    wav_file = audio_file.split('.')[0] + '.wav'
    audio.export(wav_file, format='wav')
    return wav_file


def split_audio(audio_file, segment_length=30):
    """Разделение аудио на части длиной segment_length секунд"""
    audio = AudioSegment.from_file(audio_file)
    segments = []
    for i in range(0, len(audio), segment_length * 1000):
        segments.append(audio[i:i + segment_length * 1000])
    return segments


def audio_to_text(audio_file):
    """Функция для выделения текста из аудио"""
    recognizer = sr.Recognizer()

    if not audio_file.endswith(".wav"):
        audio_file = convert_to_wav(audio_file)

    # Разделение файла на сегменты и распознавание каждого из них
    segments = split_audio(audio_file)
    full_text = []

    for segment in segments:
        with sr.AudioFile(segment.export(format="wav")) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="ru-RU")
                full_text.append(text)
            except sr.UnknownValueError:
                full_text.append("Текст не был распознан")
            except sr.RequestError:
                print("Ошибка запроса, проверьте соединение с интернетом")
                return None

    return " ".join(full_text)




