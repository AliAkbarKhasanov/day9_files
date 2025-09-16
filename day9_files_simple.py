# Den 9 rabota s failami
#О сновные режимы:

#"w" → запись (если файл существует, он перезапишется)

#"a" → добавление (дописываем в конец)

#"r" → чтение (открыть и прочитать)

#👉 encoding="utf-8" нужно, чтобы работали русские буквы

# Zapis v fail

with open("notes.txt", "w", encoding="utf-8 ") as file:
    file.write("Eto moya pervaya zametka v Pythone!\n")
    file.write("Pythone umeet rabotat s failami!\n")

#chitenie iz faila 
with open("notes.txt", "r", encoding="utf-8") as file:
    content=file.read()
    print("Soderjimoe faila:")
    print(content)