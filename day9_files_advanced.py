# 1. Sozdayom fail ili perezapisivaem ego 
with open("demo.txt", "w", encoding="utf-8") as file:
    file.write("Stroka 1\n")
    file.write("Stroka 2\n")

# 2. Dobavlenie novoy stroki v konech
with open("demo.txt", "a", encoding="utf-8") as file:
    file.write("Stroka 3 (Dobavleno pozje)\n")

# 3. chitaem ves file 
with open("demo.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Soderjimoe faila:")
    print(content)