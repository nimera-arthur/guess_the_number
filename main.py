import sqlite3
from random import randint

n = randint(1, 10)
k = input("Угадайте целое число от 1 до 10: ")
result = []
counter = 0
while True:

  counter += 1
  k = int(k)
  if k == n:
    break
  elif k > n:
    print("Ваше число, больше чем задумал компьютер")
  elif k < n:
    print("Ваше число, меньше чем задумал компьютер")

  k = input("Повторите попытку: ")

print(f"Вы угадали с попыток: {counter}. Загаданным числом было: {n}")
name_player = input('Введите ваше имя ')
result.append(name_player)
result.append(counter)

db = sqlite3.connect('sqlite_python.db')
cursor = db.cursor()

#cursor.execute("""CREATE TABLE score_players (name text, score int)""")

cursor.execute("INSERT INTO score_players(name, score) VALUES(?, ?)", result)
cursor.execute("SELECT * FROM score_players")
print(cursor.fetchall())
db.commit()
db.close()
