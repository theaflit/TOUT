# ТОУТ

## Содержание
- [Описание](#описание)
- [Структура проекта](#структура)

## Описание
ТОУТ - проект, которой поможет вам легко и эффективно учиьться.
1) Взаимодействие через телеграмм бота, который использует нейронную сеть созданную нами.
2) Реализовано скачивание видео лекций я яндекс диска и дальшейшее преобразование в текст для суммаризации.
3) Пользователя так же могут напрямую отправлять текст телеграмм бота, который вернет им краткое содержание

## Структура

- `main` - основной код для взаимодействия с Telegram-ботом.
- `interact_yadisk` - скрипт для взаимодействия с API яндекс диска.
- `summarization` - код для взаимодействия с моделью `t5-small-sum-tout` для генерации краткого содержания.
- `database` - разработанный модуль для работы с базой данных.
- `config` - файл конфигурации, в который нужно вставить ваши токены Yandex и Telegram бота.

