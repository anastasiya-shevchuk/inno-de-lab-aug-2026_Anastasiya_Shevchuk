# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

#Извлекаем host и port из вложенного словаря connection
connection = db_config.get("connection", {})
host = connection.get("host")
port = connection.get("port")

#Безопасно проверяем наличие ключа ssl_settings
#Если его нет - вернем "verify-full"
ssl_settings = connection.get("ssl_settings", "verify-full")

print(f"SSL Mode: {ssl_settings}")

# Изменяем значение user на admin
connection['user'] = 'admin'
user = connection.get("user")

#Добавляем новый параметр max_connections со значением 100 в connection
connection['max_connections'] = 100

#Выводим обновленное содержимое конфигурации connection по парам ключ: значение
print("Параметры соединения: ")
for key, value in connection.items():
    print(f"*{key}: {value}")





