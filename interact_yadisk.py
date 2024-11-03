import os
import yadisk

from config import Config
from moviepy.editor import AudioFileClip

token = Config.token_yadisk
y = yadisk.YaDisk(token=token)

dir_name = Config.dir_name


def get_all_files(dir_name):
    return list(y.listdir(dir_name))

video_file_path = 'video_files'
audio_file_path = 'audio_files'

os.makedirs(video_file_path, exist_ok=True)
os.makedirs(audio_file_path, exist_ok=True)


def video_to_audio(files):
    """Конвертация видео файлов в аудиофайлы."""
    for j, n in zip(files, range(1, len(files) + 1)):
        current_mp4 = os.path.join(video_file_path, j)
        current_mp3 = os.path.join(audio_file_path, f'file{n}.mp3')
        try:
            with AudioFileClip(current_mp4) as file_to_convert:
                file_to_convert.write_audiofile(current_mp3)
            print(f"Конвертирован {current_mp4} в {current_mp3}")
        except Exception as e:
            print(f"Ошибка при конвертации {current_mp4} в аудио: {e}")
def get_video(folder_path, raw_files):
    """Скачивание видео файлов с яндекс диска"""
    files = []
    for i in raw_files:
        if i["name"].lower().endswith(".mov"):
            print(f"Скачивается {i['name']}")
            try:
                y.download(f'{folder_path}/{i["name"]}', os.path.join(video_file_path, i["name"]))
                files.append(i["name"])
            except Exception as e:
                print(f"Ошибка при скачивании {i['name']}: {e}")
    return files
