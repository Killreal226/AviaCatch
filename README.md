# Avia_Catch

Данный бот представляет собой парсер + бот телеграм, который мониторит самые дешевые билеты на Avia sales на определенные рейсы в нужные даты. А так же в случае необходимости - бронирует их. Все взаимодействие между клиентом и ботом происходит через телеграм. Логика работы телеграм бота асинхронно реализована на основе библиотеке Aiogram, а также в свое работе использует базы данных SQL и машины состояний.

## Установка 
1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение 
3. Установите зависимости 
`pip install -r requirements.txt`

## Настройка бота телеграм:

### Регистрация бота
1. Создайте нового бота через BotFather В телеграме. Подробную инструкцию можно прочитать на этом сайте:
[BotFather](https://vc.ru/dev/530248-kak-sdelat-bota-v-telegram-poshagovaya-instrukciya)
2. Токен бота, который вы получите вставьте в файл __settings__
Пример:
`TOKEN = '6097413237:ASAD827KOdERxFg12ZFG8k0TftJ1Dre'`
3. Напишите боту в личные сообщения:
`/start`


### Запуск бота
1. Чтобы запустить бота телеграм перейдите в католог __Avia_Catch__ :
`cd Avia_Catch`
2. Запустите файл __bot_telegram__
`python bot_telegram.py`
3. Бот запущен, чтобы начать ваимодействовать с ним напишите и отправьте в группе:
`/start`

В слечае если что то ввели не верно во время бота, напишите ему:
`отмена`

## Возможности бота
Бот в телеграмме поддерживает несколько функций:
1. Регитрация новых пользователей в боте 
2. Подписка этими пользователями на рейсы (в том числе и не только на мониторинг, но и на бронирование)
3. Удаление активных рейсов
4. Просмотр всех своих активных подписок 
