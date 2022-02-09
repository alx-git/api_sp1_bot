# TELEGRAM BOT ASSISTANT

ОПИСАНИЕ
---

Telegram-бот, который обращается к API сервиса Практикум.Домашка и узнает статус домашней работы: взята ли ваша домашка в ревью, проверена ли она, а если проверена — то принял её ревьюер или вернул на доработку. Упражнение в написании бота и логировании его работы.


ЗАВИСИМОСТИ
---
#certifi==2020.4.5.1

#cffi==1.14.0

chardet==3.0.4

#cryptography==2.9.2

decorator==4.4.2

future==0.18.2

idna==2.9

pycparser==2.20

PySocks==1.7.1

pytest==6.2.1

python-dotenv==0.13.0

python-telegram-bot==12.7

requests==2.23.0

six==1.15.0

tornado==6.0.4

urllib3==1.25.9

УСТАНОВКА
---

Клонировать репозиторий и перейти в него в командной строке:

git clone

cd api_sp1_bot

Cоздать и активировать виртуальное окружение:

python -m venv venv

source venv/Scripts/activate

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Добавить собственные ключи

Запустить проект:

python homework.py
