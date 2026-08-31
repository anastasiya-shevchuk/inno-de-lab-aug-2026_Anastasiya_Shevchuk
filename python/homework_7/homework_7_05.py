#Для красивого вывода словаря
import pprint

# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]

max_ram = 0
total_cpu = 0.0
average_cpu = 0.0
active_connections = []

# Распаковка переменных кортежа
for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status == "online":
        active_connections.append(node_name)
        total_cpu += cpu_load
        # Максимальное значение RAM
        if ram_usage > max_ram:
            max_ram = ram_usage


# среднее значение CPU
average_cpu = total_cpu / len(active_connections)

#Создаем словарь со словарем внутри
result = {
    'active_nodes_count' : len(active_connections),
    'metrics' : {
        'average_cpu' : round(average_cpu,2),
        'max_ram' : max_ram,
    }
}

print('Активные узлы в сети: ', active_connections)
print('Итоговый отчет телеметрии: ')
pprint.pprint(result)

