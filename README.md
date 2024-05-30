# bot_random_image

## 1. [Описание](#1)
## 2. [Стек технологий:](#2)
## 3. [Запустить проект](#3)
## 4. [Особенности](#4)
## 5. [Планы на доработку](#5)
## 6. [Об авторе](#6)

## Описание <a id=1></a>

бот отправляет по запросу рандомную картинку котика.

### Стек технологий: <a id=2></a>
[![Python](https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=092E20&labelColor=white
)](https://www.python.org/)


```bash
git clone git@github.com:Master1941/bot_random_image.git
```  
создайте файл .env азполните согласно .env.example
```bash
touch .env
```
пример заполнения файла .env
```python
TELEGRAM_TOKEN = '457892c45n65n2qwe9dfhwedfhnq9wr914239cefqhcn319creq'
CHAT_ID = 123456789
URL = "https://api.thecatapi.com/v1/images/search"
```
Создайте виртуальное окружение
```bash
python -m venv venv
```
Активируйте окружение
```bash
source venv/Scripts/activate
```
Установите библиотеки
```bash
pip install -r requirements.txt
```
Запустите приложение
```bash
python catbot.py
```
## Особенности <a id=4></a>


## Планы на доработку  <a id=5></a>
добавить логирование

## Автор <a id=6></a>
Буканов Александр Михайлович
Python-разработчик (Backend)
E-mail: abukanov89@bk.ru
Telegram: @Aleksandr_Bukanov