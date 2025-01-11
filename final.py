user_name = input("Введите имя: ")
title1 = input("Введите первый загловок заметки: ")
title2 = input("Введите второй загловок заметки: ")
title3 = input("Введите третий загловок заметки: ")
titles = [title1, title2, title3]
content = input("Введите описание заметки: ")
status = input("Введите текущий статус: ")
created_date = input("Дата создания (в формате DD-MM-YY): ")
issue_date = input("Дата выполнения (в формате DD-MM-YY): ")
note = [user_name, content, status, created_date, issue_date, titles]

print("Данные о заметке: ", "\nИмя пользователя: ", note [0], "\nОписание заметки: ", note [1], "\nТекущий статус: ", note [2], "\nДата создания: ", note [3], "\nДата выполнения: ", note [4], "\nЗаголовки заметки: ", note [5])
