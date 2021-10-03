import logging
import os
import time
from logging import FileHandler

import requests
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

PRAKTIKUM_TOKEN = os.getenv('PRAKTIKUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

logger = logging.getLogger(__name__)
handler = FileHandler('my_logger.log')
logger.addHandler(handler)

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': f'OAuth {PRAKTIKUM_TOKEN}'}

bot = Bot(token=TELEGRAM_TOKEN)


def parse_homework_status(homework):
    homework_name = homework['homework_name']
    if homework['status'] == 'rejected':
        verdict = 'К сожалению, в работе нашлись ошибки.'
    else:
        verdict = 'Ревьюеру всё понравилось, работа зачтена!'
    return f'У вас проверили работу "{homework_name}"!\n\n{verdict}'


def get_homeworks(current_timestamp):
    homework_statuses = requests.get(
        url,
        headers=headers,
        params={'from_date': current_timestamp}
    )
    return homework_statuses.json()


def send_message(message):
    return bot.send_message(CHAT_ID, message)


def main():

    logger.debug('Бот запущен')
    current_timestamp = int(time.time())  # Начальное значение timestamp

    while True:
        try:
            homeworks = get_homeworks(current_timestamp)['homeworks']
            for homework in homeworks:
                message = parse_homework_status(homework)
                send_message(message)
                logger.info('Сообщение отправлено')
            time.sleep(5 * 60)

        except Exception as e:
            logging.error(e, exc_info=True)
            message = f'Бот упал с ошибкой: {e}'
            send_message(message)
            time.sleep(5)


if __name__ == '__main__':
    main()
