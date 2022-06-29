from datetime import time

time_1 = time(15, 15, 00)
time_2 = time(20, 00, 00)
time_3 = time(23, 00, 00)


# Не удаляйте код дальше, он нужен для проверки

format = "%H:%M"

print(time_1.strftime(format))
print(time_2.strftime(format))
print(time_3.strftime(format))