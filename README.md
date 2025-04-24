# Sprints_factory

## Документация API (Swagger)

Для проекта "ФСТР Перевалы" реализована автоматическая документация API с использованием Swagger UI.

### Доступ к документации:

После запуска сервера документация будет доступна по адресам:
- **Swagger UI** (интерактивная документация):  
  `http://localhost:8000/swagger/`
- **ReDoc** (альтернативный формат):  
  `http://localhost:8000/redoc/`

### Основные эндпоинты API:

#### 1. Добавление нового перевала
```http
POST /pereval/submitData/
Content-Type: application/json

{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_title": "Триев",
  "content": "Описание перевала",
  "user": {
    "email": "user@example.com",
    "fam": "Иванов",
    "name": "Иван",
    "otc": "Иванович",
    "phone": "+79261234567"
  },
  "coord": {
    "latitude": "45.3842",
    "longitude": "7.1525",
    "height": "1200"
  },
  "level": {
    "winter": "1A",
    "summer": "1B",
    "autumn": "1A",
    "spring": "1A"
  },
  "images": [
    {
      "data": "https://example.com/photo1.jpg",
      "title": "Вид с севера"
    }
  ]
}
```

#### 2. Получение информации о перевале
```http
GET /pereval/{id}/submitData/
```

#### 3. Редактирование перевала
```http
PATCH /pereval/{id}/submitData/
Content-Type: application/json

{
  "title": "Новое название",
  "content": "Обновленное описание"
}
```

#### 4. Поиск перевалов по email пользователя
```http
GET /pereval/submitData/?user__email=user@example.com
```

### Примеры ответов:

**Успешное добавление:**
```json
{
  "status": 200,
  "message": null,
  "id": 42
}
```

**Ошибка валидации:**
```json
{
  "status": 400,
  "message": "Не заполнено обязательное поле: title",
  "id": null
}
```

**Статусы модерации:**
- `new` - новая запись
- `pending` - в процессе модерации
- `approved` - одобрено
- `rejected` - отклонено

Для тестирования API используйте Swagger UI, где доступны все эндпоинты с возможностью отправки тестовых запросов.
