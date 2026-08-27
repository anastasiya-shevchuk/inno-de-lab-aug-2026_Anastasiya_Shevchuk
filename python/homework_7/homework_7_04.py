# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin",
"developer", "guest"]

# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# Преобразовываем список во множество, удаляем все дубликаты
requested_roles_unique = set (requested_roles)

# Пересечение множеств
intersection_roles = requested_roles_unique.intersection(required_admin_roles)

# Разность множеств
difference_in_roles = required_admin_roles.difference(requested_roles_unique)

# Проверяем наличие роли security_officer с помощью оператора in
security_officer_status = "security_officer" in requested_roles_unique

print(f"Уникальные запрошенные роли: {requested_roles_unique}")
print(f"Общие административные роли: {intersection_roles}")
print(f"Недостающие административные роли: {difference_in_roles}")
print(f"Наличие роли security_officer в запросе: {security_officer_status}")