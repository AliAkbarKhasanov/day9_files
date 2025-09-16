✨ Этот проект — часть моего пути изучения Python (Day 9).


---

# 📘 Day 10 — Modules  

```markdown
# 📦 Модули в Python

Примеры использования стандартных модулей: `random`, `math`, `datetime`.

## 📌 Что делает программа
- 🎲 Генерирует случайное число (бросок кубика)
- 📐 Считает факториалы и корни
- 📅 Показывает сегодняшнюю дату и время

## ▶️ Пример запуска


🎲 Бросаем кубик...
Выпало: 4

Квадратный корень из 25 = 5.0
Факториал 5 = 120

Сегодняшняя дата: 2025-09-13
Точное время сейчас: 14:30:05


## 💻 Код
```python
import random
import math
import datetime

print("🎲 Бросаем кубик...")
print("Выпало:", random.randint(1, 6))

print("Квадратный корень из 25 =", math.sqrt(25))
print("Факториал 5 =", math.factorial(5))

today = datetime.date.today()
time_now = datetime.datetime.now()
print("Сегодняшняя дата:", today)
print("Точное время сейчас:", time_now.strftime("%H:%M:%S"))
