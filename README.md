# Крестики-Нолики — Серверная часть
## Обзор
Сервер для игры в крестики-нолики с поддержкой игры против компьютера (алгоритм Минимакс) или другого игрока. Реализована полноценная JWT-авторизация, хранение данных в PostgreSQL, история игр и таблица лидеров.


## Технологии
Фреймворк: Flask  
База данных: PostgreSQL + SQLAlchemy ORM  
Аутентификация: JWT (flask_jwt_extended)  
Архитектура: Чистая слоистая архитектура (web → domain → datasource → di)


## Структура проекта

```text
src/
├── main.py                 # Точка входа
├── front.py                # Клиентская часть (для тестирования)
├── requirements.txt        # Зависимости
├── stats.sql              # SQL для статистики
│
├── web/                   # Слой представления
│   ├── route/            # Контроллеры (game_route, user_route)
│   ├── model/            # Web-модели
│   └── mapper/           # Мапперы domain ↔ web
│
├── domain/                # Бизнес-логика
│   ├── model/            # Доменные модели (игра, поле, пользователь, JWT)
│   ├── service/          # Сервисы (игровой, JWT, пользовательский)
│   └── constants.py      # Константы и исключения
│
├── datasource/            # Работа с данными
│   ├── database/         # PostgreSQL + SQLAlchemy схемы
│   ├── repository/       # Репозитории (игры, пользователи)
│   └── mapper/           # Мапперы domain ↔ datasource
│
└── di/                    # Внедрение зависимостей
    └── container/        # DI-контейнер (синглтоны)
```

## API Endpoints
### Аутентификация и пользователи
Метод |	Endpoint |	Описание
------|----------|-----------
POST |	/auth/register |	Регистрация пользователя
POST |	/auth/login |	Получение access/refresh токенов
POST |	/auth/refresh |	Обновление access токена
GET |	/user/<uid> |	Получить информацию о пользователе по UUID
GET |	/user/me	Получить информацию о текущем пользователе по access токену

### Игры (требуется авторизация)
Метод |	Endpoint |	Описание
------|----------|-----------
POST |	/game |	Создать новую игру (с компьютером или игроком)
GET |	/games/available |	Получить доступные игры для подключения
POST |	/<game_id>/join |	Подключиться к существующей игре
POST |	/<game_id> |	Сделать ход
GET |	/games/history |	Получить завершённые игры пользователя
GET |	/games/leaderboard |	Получить топ N игроков по соотношению побед
GET |	/ |	Проверка работы сервера (handshake)


## Основные возможности
### Игровая логика

Игра против компьютера (Минимакс)  
Игра против другого игрока  
Валидация ходов и состояний  
Параллельные игровые сессии  

### JWT-авторизация
Регистрация и вход  
Access + Refresh токены  
Bearer token аутентификация  
Защита эндпоинтов  

### История игр
Все завершённые игры с датой создания  
Фильтрация по UUID пользователя  
Состояния: победа, ничья, в процессе, ожидание  


### Таблица лидеров
Расчёт соотношения побед (победы / поражения + ничьи)  
Рейтинг топ N игроков (параметр передаётся в запросе)  
Вывод UUID и логина

## Установка и запуск
### Клонировать репозиторий

```bash
git clone https://github.com/Tatititata/Tic_tac_toe.git
cd Tic_tac_toe/src
```

### Установить зависимости
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Создать базу данных PostgreSQL

```sql
sudo -u postgres psql -l | grep tic_tac_toe
```

### Запустить сервер

```bash
python -m main
```

## Примеры запросов

### Регистрация

``` bash
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"login": "player1", "password": "123456"}'
```


### Вход

```bash
RESPONSE=$(curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"login": "player1", "password": "123456"}')
ACCESS_TOKEN=$(echo $RESPONSE  | jq -r '.access_token')
REFRESH_TOKEN=$(echo $RESPONSE  | jq -r '.refresh_token')
```

### Обновление токена
```bash

RESPONSE=$(curl -X POST http://localhost:5000/auth/refresh \
  -H "Content-Type: application/json" \
  -d "{\"refresh_token\": \"$REFRESH_TOKEN\"}")


ACCESS_TOKEN=$(echo "$RESPONSE" | jq -r '.access_token')
REFRESH_TOKEN=$(echo "$RESPONSE" | jq -r '.refresh_token')

echo "New access token: $ACCESS_TOKEN"
echo "New refresh token: $REFRESH_TOKEN"
```

### Создание игры
```bash
RESPONSE=$(curl -X POST http://localhost:5000/game \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"opponent_type": "bot"}')

GAME_ID=$(echo $RESPONSE | jq -r '.uid')
echo "Game id: $GAME_ID"
echo $RESPONSE | jq '.'
```

### Получение списка доступных игр
```bash
curl -X GET http://localhost:5000/games/available \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

### Подключение к игре
```bash
curl -X POST http://localhost:5000/<game_id>/join \
  -H "Authorization: Bearer <access_token>"
```
### Ход в игре
```bash
curl -X POST http://localhost:5000/<game_id> \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{1}'
```
### Получение истории игр
```bash
curl -X GET http://localhost:5000/games/history \
  -H "Authorization: Bearer <access_token>"
```
### Получение таблицы лидеров
```bash
curl -X GET "http://localhost:5000/games/leaderboard?topN=10" \
  -H "Authorization: Bearer <access_token>"
```
### Информация о пользователе
```bash
####  По UUID
curl -X GET http://localhost:5000/user/<uid> \
  -H "Authorization: Bearer <access_token>"

####  О себе
curl -X GET http://localhost:5000/user/me \
  -H "Authorization: Bearer <access_token>"
```
Проверка работы сервера
```bash
curl -X GET http://localhost:5000/
```


## Клиентский интерфейс (Frontend)

Для удобного тестирования API без использования curl в проекте реализован консольный клиент (front.py).

### Запуск клиента

```bash
python front.py
```

#### Возможности консольного клиента

После запуска откроется интерактивное меню:

```text
=== Tic-Tac-Toe Console Client ===

    1. Register              # Регистрация нового пользователя
    2. Check available games # Просмотр доступных игр для подключения
    3. User info             # Информация о пользователе по UUID
    4. Play game             # Подключение к существующей игре и игровой процесс
    5. Login                 # Вход в систему (получение токенов)
    6. Create game           # Создание новой игры (против бота или человека)
    7. Refresh tokens        # Обновление access токена через refresh токен
    8. Game history          # Просмотр истории завершённых игр
    9. About me              # Информация о текущем пользователе
    0. Leaderboard           # Таблица лидеров (с указанием лимита)
    q to quit                # Выход
```

#### Игровой процесс

После создания или подключения к игре:

Вводите номер клетки от 1 до 9 (нумерация как на цифровой клавиатуре):

```text
1 2 3
4 5 6
7 8 9
```
Игра отображает поле в ASCII-формате:

```text
╔═══╦═══╦═══╗
║ X ║   ║ O ║
╠═══╬═══╬═══╣
║   ║ X ║   ║
╠═══╬═══╬═══╣
║   ║ O ║   ║
╚═══╩═══╩═══╝
```
Введите q для выхода из игры

#### Преимущества использования клиента

✅ Не нужно вручную формировать curl запросы  
✅ Автоматическое управление токенами (сохраняются в памяти)  
✅ Визуализация игрового поля  
✅ Удобный пошаговый игровой процесс  
✅ Быстрая смена пользователей  

Пример сессии
```bash
$ python front.py
=== Tic-Tac-Toe Console Client ===

    1. Register
    5. Login
    6. Create game
    ...

> 5
Login: player1
Password: 123456
Logged in: player1

> 6
1 = human, 2 = bot: 2
Game created: abc-123 status: IN_PROGRESS
╔═══╦═══╦═══╗
║   ║   ║   ║
╠═══╬═══╬═══╣
║   ║   ║   ║
╠═══╬═══╬═══╣
║   ║   ║   ║
╚═══╩═══╩═══╝
Enter move (1-9) or q to quit: 5
...
```
#### Примечание: Клиент предназначен только для тестирования и отладки. 



## Автор
Проект выполнен в рамках курса Python Bootcamp.