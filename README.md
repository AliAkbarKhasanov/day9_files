✨ Этот проект — часть моего пути изучения Python (Day 9).
# 📘 Day 9 — Files  

```markdown
# 📂 Работа с файлами

Программа создаёт файл, записывает туда текст и потом читает его обратно.

## 📌 Что делает программа
1. Создаёт файл `notes.txt`
2. Записывает туда заметки
3. Считывает содержимое и выводит в консоль

## ▶️ Пример запуска
Содержимое файла:
Это моя первая заметка в Python!
Python умеет работать с файлами.

python
Copy code

## 💻 Код
```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Это моя первая заметка в Python!\n")
    file.write("Python умеет работать с файлами.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)
