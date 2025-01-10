user_name = input("Введите имя: ")
title1 = input("Введите первый загловок заметки: ")
title2 = input("Введите второй загловок заметки: ")
title3 = input("Введите третий загловок заметки: ")
titles = [title1, title2, title3]
content = input("Введите описание заметки: ")
status = input("Введите текущий статус: ")
created_date = input("Дата создания: ")
issue_date = input("Дата выполнения: ")
note = [user_name, content, status, created_date, issue_date, titles]

print(note)